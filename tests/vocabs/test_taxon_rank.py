"""Taxon-rank display labels must not change accepted tabular values."""

# Standard
import datetime
import json
from pathlib import Path

# Third-Party
import pytest
import rdflib

# Local
from abis_mapping.utils.vocabs import Term
from abis_mapping.vocabs import taxon_rank


@pytest.mark.parametrize(
    ("value", "iri"),
    (
        ("SUBFAMILY", "http://linked.data.gov.au/def/tern-cv/49849796-fc73-444f-a375-32fc0048a18b"),
        ("subfamily", "http://linked.data.gov.au/def/tern-cv/49849796-fc73-444f-a375-32fc0048a18b"),
        ("SubFamily", "http://linked.data.gov.au/def/tern-cv/49849796-fc73-444f-a375-32fc0048a18b"),
        ("INFRAGENERIC NAME", "http://linked.data.gov.au/def/tern-cv/8d227e73-f906-4d5f-9f15-8ae8bf29b2ce"),
        ("infra-generic name", "http://linked.data.gov.au/def/tern-cv/8d227e73-f906-4d5f-9f15-8ae8bf29b2ce"),
        ("INFRAORDER", "http://linked.data.gov.au/def/tern-cv/b49af045-88c2-44c0-ad34-901d1ff46d7a"),
        ("infra-order", "http://linked.data.gov.au/def/tern-cv/b49af045-88c2-44c0-ad34-901d1ff46d7a"),
        ("GREX", "http://linked.data.gov.au/def/tern-cv/45d214c6-894b-4fe5-a9ce-2db3a1fc3a7d"),
        ("SPECIES COMPLEX", "http://linked.data.gov.au/def/tern-cv/bc6b552f-5ab0-4d46-a236-a99fc2005c93"),
        ("SUBKINGDOM", "http://rs.gbif.org/vocabulary/gbif/rank/subkingdom"),
        ("subkingdom", "http://rs.gbif.org/vocabulary/gbif/rank/subkingdom"),
        ("SUBVARIETAS", "http://linked.data.gov.au/def/tern-cv/cb2627f0-e121-474b-a354-dd0e392daa84"),
    ),
)
def test_legacy_and_display_values_resolve_to_the_same_iri(value: str, iri: str) -> None:
    vocab = taxon_rank.TaxonRank(
        graph=rdflib.Graph(),
        source=rdflib.URIRef("urn:test:dataset"),
        submitted_on_date=datetime.date(2026, 11, 9),
    )
    assert vocab.get(value) == rdflib.URIRef(iri)


def test_export_uses_display_labels(tmp_path: Path) -> None:
    graph = rdflib.Graph().parse(taxon_rank.TaxonRank.export_as_rdf(tmp_path / "taxon_rank.ttl"))
    assert graph.value(taxon_rank.SUBFAMILY.iri, rdflib.SKOS.prefLabel) == rdflib.Literal("subfamily", lang="en")
    assert graph.value(taxon_rank.INFRAGENERICNAME.iri, rdflib.SKOS.prefLabel) == rdflib.Literal(
        "infra-generic name", lang="en"
    )
    assert graph.value(taxon_rank.CULTIVARGROUP.iri, rdflib.SKOS.altLabel) == rdflib.Literal("grex", lang="en")
    assert all(not str(label).isupper() for label in graph.objects(None, rdflib.SKOS.prefLabel))
    assert len(set(graph.subjects(rdflib.RDF.type, rdflib.SKOS.Concept))) == 34


def test_export_preserves_cultivar_editorial_metadata(tmp_path: Path) -> None:
    graph = rdflib.Graph().parse(taxon_rank.TaxonRank.export_as_rdf(tmp_path / "taxon_rank.ttl"))
    cultivar = taxon_rank.CULTIVAR.iri
    assert set(graph.objects(cultivar, rdflib.SKOS.definition)) == {
        rdflib.Literal(
            "A group of plants selected for particular characteristics that remain distinct, uniform and stable "
            "when the plants are propagated by appropriate means.",
            lang="en",
        )
    }
    assert "not equivalent" in str(graph.value(cultivar, rdflib.SKOS.scopeNote))
    assert set(graph.objects(cultivar, rdflib.SKOS.example)) == {
        rdflib.Literal("Taxus baccata 'Variegata'.", lang="en")
    }
    assert not list(graph.objects(taxon_rank.SUBFAMILY.iri, rdflib.SKOS.scopeNote))
    assert not list(graph.objects(taxon_rank.SUBFAMILY.iri, rdflib.SKOS.example))


@pytest.mark.parametrize(
    ("term", "definition", "scope_fragment"),
    (
        (taxon_rank.SPECIESAGGREGATE, "A loosely defined group of species.", "genus or subgenus"),
        (
            taxon_rank.SUBSPECIFICAGGREGATE,
            "A loosely defined group of subspecies within a species.",
            "not counted as a word of the trinomen",
        ),
    ),
)
def test_export_separates_aggregate_definitions_from_scope(
    tmp_path: Path, term: Term, definition: str, scope_fragment: str
) -> None:
    graph = rdflib.Graph().parse(taxon_rank.TaxonRank.export_as_rdf(tmp_path / "taxon_rank.ttl"))
    assert set(graph.objects(term.iri, rdflib.SKOS.definition)) == {rdflib.Literal(definition, lang="en")}
    scope = graph.value(term.iri, rdflib.SKOS.scopeNote)
    assert scope == rdflib.Literal(term.scope_note, lang="en")
    assert "ICZN Article 6.2" in str(scope)
    assert scope_fragment in str(scope)


def test_subkingdom_export_replaces_placeholder(tmp_path: Path) -> None:
    graph = rdflib.Graph().parse(taxon_rank.TaxonRank.export_as_rdf(tmp_path / "taxon_rank.ttl"))
    gbif = rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subkingdom")
    placeholder = rdflib.URIRef("http://example.com/subkingdom")
    assert (gbif, rdflib.RDFS.isDefinedBy, rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank")) in graph
    assert len(set(graph.objects(gbif, rdflib.RDFS.isDefinedBy))) == 1
    assert (gbif, rdflib.RDF.type, rdflib.SKOS.Concept) in graph
    assert (gbif, rdflib.DCTERMS.replaces, placeholder) in graph
    assert not list(graph.triples((placeholder, None, None)))
    assert graph.value(gbif, rdflib.SKOS.definition) == rdflib.Literal(
        "A taxonomic rank below kingdom and above phylum (division).", lang="en"
    )


def test_export_carries_only_reviewed_exact_matches(tmp_path: Path) -> None:
    # Frozen reviewed mapping set, copied from the BDR scheme; no label matching.
    reviewed = json.loads((Path(__file__).parent / "data/taxon_rank_exact_matches.json").read_text())
    expected = {
        (rdflib.URIRef(subject), rdflib.SKOS.exactMatch, rdflib.URIRef(target))
        for subject, targets in reviewed.items()
        for target in targets
    }
    graph = rdflib.Graph().parse(taxon_rank.TaxonRank.export_as_rdf(tmp_path / "taxon_rank.ttl"))
    scheme = rdflib.URIRef("https://linked.data.gov.au/dataset/bdr/bdr-cv/attribute/taxonRank")
    assert graph.value(scheme, rdflib.SKOS.historyNote) == taxon_rank.TaxonRank.history_note
    assert "copied unchanged" in str(taxon_rank.TaxonRank.history_note)
    assert len(expected) == 33
    assert set(graph.triples((None, rdflib.SKOS.exactMatch, None))) == expected
    assert not list(graph.triples((None, rdflib.SKOS.closeMatch, None)))
    assert not list(graph.objects(taxon_rank.SUBKINGDOM.iri, rdflib.SKOS.exactMatch))
    assert all(subject != target for subject, _, target in expected)
