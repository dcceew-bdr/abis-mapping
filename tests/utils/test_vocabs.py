"""Provides Unit Tests for the `abis_mapping.utils.vocabs` module"""

# Standard
import textwrap

# Third-Party
import pytest
import rdflib

# Local
import abis_mapping.utils.namespaces
import abis_mapping.utils.vocabs
import abis_mapping.utils.rdf
from tests import helpers

# Typing
from typing import assert_type


def test_vocabs_term() -> None:
    """Tests the Term Class"""
    # Create Term
    term = abis_mapping.utils.vocabs.Term(
        labels=("A", "B", "C"),
        iri=rdflib.URIRef("D"),
        description="E",
    )

    # Test Mapping
    assert term.to_mapping() == {
        "A": rdflib.URIRef("D"),
        "B": rdflib.URIRef("D"),
        "C": rdflib.URIRef("D"),
    }

    # Test Match
    assert term.match("a")
    assert term.match("A")
    assert term.match("b")
    assert term.match("B")
    assert term.match("c")
    assert term.match("C")
    assert not term.match("X")


def test_vocabs_restricted_vocab() -> None:
    """Tests the RestrictedVocab Class"""

    # Create Vocab
    class Vocab(abis_mapping.utils.vocabs.RestrictedVocabulary):
        vocab_id = "TEST_RESTRICT"
        terms = (
            abis_mapping.utils.vocabs.Term(
                labels=("A",),
                iri=rdflib.URIRef("A"),
                description="A",
            ),
            abis_mapping.utils.vocabs.Term(
                labels=("B",),
                iri=rdflib.URIRef("B"),
                description="B",
            ),
        )

    vocab = Vocab()

    # Assert Existing Values
    assert vocab.get("a") == rdflib.URIRef("A")
    assert vocab.get("A") == rdflib.URIRef("A")
    assert vocab.get("b") == rdflib.URIRef("B")
    assert vocab.get("B") == rdflib.URIRef("B")

    # Assert Invalid Values
    with pytest.raises(abis_mapping.utils.vocabs.VocabularyError):
        vocab.get("C")


def test_vocabs_flexible_vocab() -> None:
    """Tests the FlexibleVocab Class"""

    # Create Vocab
    class Vocab(abis_mapping.utils.vocabs.FlexibleVocabulary):
        vocab_id = "TEST_FLEX"
        definition = rdflib.Literal("definition")
        base = "base/"
        proposed_scheme = rdflib.URIRef("http://proposed_scheme")
        broader = rdflib.URIRef("broader")
        default = None
        terms = (
            abis_mapping.utils.vocabs.Term(
                labels=("A",),
                iri=rdflib.URIRef("A"),
                description="A",
            ),
            abis_mapping.utils.vocabs.Term(
                labels=("B",),
                iri=rdflib.URIRef("B"),
                description="B",
            ),
        )

    # Create graph
    graph = abis_mapping.utils.rdf.create_graph()

    # Initialize vocab
    vocab = Vocab(graph=graph, source=helpers.TEST_DATASET_IRI, submitted_on_date=helpers.TEST_SUBMITTED_ON_DATE)

    # Assert Existing Values
    assert vocab.get("a") == rdflib.URIRef("A")
    assert vocab.get("A") == rdflib.URIRef("A")
    assert vocab.get("b") == rdflib.URIRef("B")
    assert vocab.get("B") == rdflib.URIRef("B")

    # Assert New Values
    assert vocab.get("C") == rdflib.URIRef("https://linked.data.gov.au/dataset/bdr/base/C")
    assert (
        graph.serialize(format="ttl").strip()
        == textwrap.dedent(
            """
        @prefix reg: <http://purl.org/linked-data/registry#> .
        @prefix schema: <https://schema.org/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <https://linked.data.gov.au/dataset/bdr/base/C> a skos:Concept ;
            reg:status <https://linked.data.gov.au/def/reg-statuses/submitted> ;
            skos:broader <broader> ;
            skos:definition "definition" ;
            skos:historyNote "This concept was used in data submitted to the BDR on 2025-05-04" ;
            skos:inScheme <https://linked.data.gov.au/def/bdr/bdr-cv/pending> ;
            skos:prefLabel "C" ;
            skos:scopeNote "This concept is proposed as a member of this scheme: http://proposed_scheme" ;
            schema:citation "https://linked.data.gov.au/dataset/bdr/00000000-0000-0000-0000-000000000000"^^xsd:anyURI .
        """
        ).strip()
    )

    # Assert Invalid Values
    with pytest.raises(abis_mapping.utils.vocabs.VocabularyError):
        vocab.get(None)  # No Default


def test_vocab_register_id() -> None:
    """Tests that vocabs get registered at import."""
    assert len(abis_mapping.utils.vocabs._id_registry) > 0


def test_get_vocab() -> None:
    """Tests get_vocab function."""
    # Retrieve vocab
    datum = abis_mapping.utils.vocabs.get_vocab("GEODETIC_DATUM")

    # Assert exists
    assert datum is not None
    assert issubclass(datum, abis_mapping.utils.vocabs.Vocabulary)


def test_get_vocab_invalid() -> None:
    """Tests get_vocab function with an invalid vocab."""
    # Should raise key error
    with pytest.raises(ValueError):
        abis_mapping.utils.vocabs.get_vocab("NOT_A_VOCAB")


def test_get_flexible_vocab() -> None:
    """Tests get_flexible_vocab function."""
    # Retrieve vocab
    habitat = abis_mapping.utils.vocabs.get_flexible_vocab("TARGET_HABITAT_SCOPE")

    # Assert exists
    assert habitat is not None
    assert issubclass(habitat, abis_mapping.utils.vocabs.FlexibleVocabulary)
    # Check mypy sees the right return type
    assert_type(habitat, type[abis_mapping.utils.vocabs.FlexibleVocabulary])


def test_get_flexible_vocab_with_fixed_vocab() -> None:
    """Tests get_flexible_vocab function with a non-flexible vocab."""
    # Retrieve vocab
    with pytest.raises(
        ValueError,
        match=r"Key GEODETIC_DATUM is not a subclass of FlexibleVocabulary.",
    ):
        abis_mapping.utils.vocabs.get_flexible_vocab("GEODETIC_DATUM")


def test_get_flexible_vocab_with_unknown_vocab() -> None:
    """Tests get_flexible_vocab function with an unknown vocab."""
    # Retrieve vocab
    with pytest.raises(
        ValueError,
        match=r"Key UNKNOWN not found in registry.",
    ):
        abis_mapping.utils.vocabs.get_flexible_vocab("UNKNOWN")


@pytest.mark.parametrize("flexible", [True, False])
def test_export_as_rdf(tmp_path, flexible):
    """Export both kinds without leaking runtime data or lookup settings."""
    import datetime

    vocabs = abis_mapping.utils.vocabs
    term = vocabs.Term(("Preferred", "Alias"), rdflib.URIRef("https://example.org/term"), "Term definition")
    parent = vocabs.FlexibleVocabulary if flexible else vocabs.RestrictedVocabulary
    cls = type(
        "ExportVocabulary",
        (parent,),
        {
            "vocab_id": "EXPORT_TEST",
            "base": "test/export/",
            "terms": (term,),
            "definition": rdflib.Literal("Scheme definition"),
            "default": term,
            "broader": rdflib.URIRef("https://example.org/broader"),
            "proposed_scheme": rdflib.URIRef("https://example.org/ignored"),
        },
    )
    runtime = rdflib.Graph()
    instance = (
        cls(graph=runtime, source=rdflib.URIRef("https://example.org/source"), submitted_on_date=datetime.date.today())
        if flexible
        else cls()
    )
    path = instance.export_as_rdf(tmp_path / "export.ttl")
    graph = rdflib.Graph().parse(path)
    scheme = rdflib.URIRef("https://linked.data.gov.au/dataset/bdr/test/export/")
    assert (scheme, rdflib.RDF.type, rdflib.SKOS.ConceptScheme) in graph
    assert (scheme, rdflib.SKOS.hasTopConcept, term.iri) in graph
    for predicate in (rdflib.RDFS.isDefinedBy, rdflib.SKOS.topConceptOf, rdflib.SKOS.inScheme):
        assert (term.iri, predicate, scheme) in graph
    assert (term.iri, rdflib.SKOS.prefLabel, rdflib.Literal("Preferred", lang="en")) in graph
    assert (term.iri, rdflib.SKOS.altLabel, rdflib.Literal("Alias", lang="en")) in graph
    definition = str(graph.value(scheme, rdflib.SKOS.definition))
    assert ("This is an open-ended vocabulary" if flexible else "This is a closed vocabulary") in definition
    assert "\n\nProposed as narrower terms of https://example.org/broader" in definition
    assert graph.value(scheme, rdflib.SDO.dateCreated) == rdflib.Literal(datetime.date(2026, 9, 20))
    assert graph.value(scheme, rdflib.SDO.dateModified) == rdflib.Literal(datetime.date.today())
    assert cls.proposed_scheme not in set(graph.all_nodes())
    assert len(runtime) == 0
    assert rdflib.Graph().parse(instance.export_as_rdf(path)).isomorphic(graph)
