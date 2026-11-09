"""Provides taxon rank vocabulary for the package.

Display labels follow the BDR rank scheme. Input matching normalises case and
punctuation, so legacy uppercase input values still resolve to the same IRIs.
Exact matches are carried from the reviewed BDR/TERN publication, not inferred
from matching labels. GBIF subkingdom is used directly and has no self-mapping.
"""

# Third-Party
import rdflib

# Local
from abis_mapping import utils


# Terms
CLASS = utils.vocabs.Term(
    labels=("class",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/db985a35-6edb-4ba1-8939-b0a7b1efa287"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/class"),),
    description="Class",
)
CULTIVAR = utils.vocabs.Term(
    labels=("cultivar",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/892fed0b-70cc-48d4-ac3f-0b0b495cc0c0"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/cultivar"),),
    # Paraphrased from ICNCP (2016), Art. 2.3; scope: Art. 2.1 Note 1.
    # https://dafflibrary.com/wp-content/uploads/The-International-Code-of-Nomenclature-for-Cultivated-Plants-Ninth-Edition-2016.pdf#page=25
    description="A group of plants selected for particular characteristics that remain distinct, uniform and stable when the plants are propagated by appropriate means.",
    scope_note="Used here for the cultivar category governed by the International Code of Nomenclature for Cultivated Plants (ICNCP), rather than a botanical rank under the ICN. Cultivar is not equivalent to the botanical ranks variety (varietas) or form (forma).",
    examples=("Taxus baccata 'Variegata'.",),
)
CULTIVARGROUP = utils.vocabs.Term(
    labels=(
        "cultivar group",
        "grex",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/45d214c6-894b-4fe5-a9ce-2db3a1fc3a7d"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/cultivarGroup"),),
    description="Cultivar group",
)
FAMILY = utils.vocabs.Term(
    labels=("family",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/f2e2f14f-56d4-4d2f-9a37-7e140133cbd2"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/family"),),
    description="Family",
)
FORM = utils.vocabs.Term(
    labels=(
        "form",
        "forma",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/dae4d56e-7440-4ddd-90e7-9924b455ca40"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/form"),),
    description="Form",
)
GENUS = utils.vocabs.Term(
    labels=("genus",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/5fb9982c-8249-4d58-9f38-659e8c7c6daf"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/genus"),),
    description="Genus",
)
INFORMAL = utils.vocabs.Term(
    labels=("informal",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/d43fd16c-73c3-4578-a359-7168a0876aaf"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/informal"),),
    description="Informal",
)
INFRAGENERICNAME = utils.vocabs.Term(
    labels=("infra-generic name",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/8d227e73-f906-4d5f-9f15-8ae8bf29b2ce"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/infragenericname"),),
    description="Used for any other unspecific rank below genera and above species.",
)
INFRAORDER = utils.vocabs.Term(
    labels=("infra-order",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/b49af045-88c2-44c0-ad34-901d1ff46d7a"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/infraorder"),),
    description="Infraorder",
)
INFRASPECIFICNAME = utils.vocabs.Term(
    labels=("infra-specific name",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/445b6830-8e31-4fab-889b-f18f88f382c0"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/infraspecificname"),),
    description="Used for any other unspecific rank below genera and above species.",
)
INFRASUBSPECIFICNAME = utils.vocabs.Term(
    labels=("infra-subspecific name",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/b06ee648-55e2-435f-b453-2f6639addbcb"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/infrasubspecificname"),),
    description="Used for any other unspecific rank below subspecies.",
)
KINGDOM = utils.vocabs.Term(
    labels=(
        "kingdom",
        "regnum",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/a27dc8c9-25ed-4a82-b797-b9dd0add6da2"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/kingdom"),),
    description="Kingdom",
)
ORDER = utils.vocabs.Term(
    labels=(
        "order",
        "alliance",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/6605eecb-e8ba-47fc-a364-81aa3ba5ce69"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/order"),),
    description="Order",
)
PHYLUM = utils.vocabs.Term(
    labels=(
        "phylum",
        "division",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/3ade9854-d90f-4709-bb5a-260d62a2c647"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/phylum"),),
    description="Phylum",
)
SECTION = utils.vocabs.Term(
    labels=("section",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/22829f2d-461d-4cf6-acbc-5b8f7d2d9c77"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/section"),),
    description=(
        "Section within a genus. In Zoology a section sometimes refers to a group above family level, this is NOT meant"
    ),
)
SERIES = utils.vocabs.Term(
    labels=("series",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/d3f48baa-7a29-4b4f-9d92-bb5276ab8710"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/series"),),
    description="Series within a genus.",
)
SPECIES = utils.vocabs.Term(
    labels=("species",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/2b6fae57-f28e-4f24-b6f9-19f114dbb61e"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/species"),),
    description="Species",
)
SPECIESAGGREGATE = utils.vocabs.Term(
    labels=(
        "species aggregate",
        "aggregate",
        "species group",
        "species complex",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/bc6b552f-5ab0-4d46-a236-a99fc2005c93"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/speciesAggregate"),),
    # Definition retained from the existing term; zoological scope: ICZN Art. 6.2.
    # https://code.iczn.org/chapter-2-the-number-of-words-in-the-scientific-names-of-animals/article-6-interpolated-names/
    description="A loosely defined group of species.",
    scope_note="In zoological nomenclature, an aggregate groups species within a genus or subgenus; the aggregate is not itself a subgenus. Under ICZN Article 6.2, a species name in parentheses can denote the aggregate after the genus-group name. Distinguish this grouping of species from a subspecific aggregate, which groups subspecies within one species.",
)
SUBFAMILY = utils.vocabs.Term(
    labels=("subfamily",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/49849796-fc73-444f-a375-32fc0048a18b"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subfamily"),),
    description="Subfamily",
)
SUBFORM = utils.vocabs.Term(
    labels=(
        "subform",
        "subforma",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/9eeb2dcf-ec0c-4541-a409-28722e9b4f26"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subform"),),
    description="Subform",
)
SUBGENUS = utils.vocabs.Term(
    labels=("subgenus",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/86a64fd0-7aa6-4ef1-93cc-45ae722ec6a7"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subgenus"),),
    description="Subgenus",
)
SUBKINGDOM = utils.vocabs.Term(
    labels=("subkingdom",),
    iri=rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subkingdom"),
    defined_by=rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank"),
    # GBIF supplies the identifier; definition paraphrased from ICN Article 4.2:
    # https://www.iapt-taxon.org/nomen/pages/main/art_4.html
    description="A taxonomic rank below kingdom and above phylum (division).",
    replaces=(rdflib.URIRef("http://example.com/subkingdom"),),
)
SUBORDER = utils.vocabs.Term(
    labels=("suborder",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/a68fa217-969b-48ea-a08a-bb7618079edb"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/suborder"),),
    description="Suborder",
)
SUBSECTION = utils.vocabs.Term(
    labels=("subsection",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/367a27ee-7c6f-48a0-ba50-ff137ed1fe0c"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subsection"),),
    description="Subsection within a genus.",
)
SUBSERIES = utils.vocabs.Term(
    labels=("subseries",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/61a34b22-555e-431d-848c-95bb6a364a9a"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subseries"),),
    description="Subseries within a genus.",
)
SUBSPECIES = utils.vocabs.Term(
    labels=("subspecies",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/7abb3e62-ec02-4b7d-b057-e4380d66dd72"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subspecies"),),
    description="Subspecies",
)
SUBSPECIFICAGGREGATE = utils.vocabs.Term(
    labels=("subspecific aggregate",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/fdbe211f-33d6-4446-a1fb-5eb8de45dd57"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subspecificAggregate"),),
    # Definition retained from the existing term; zoological scope: ICZN Art. 6.2.
    # https://code.iczn.org/chapter-2-the-number-of-words-in-the-scientific-names-of-animals/article-6-interpolated-names/
    description="A loosely defined group of subspecies within a species.",
    scope_note="Under ICZN Article 6.2, a subspecies name placed in parentheses between the species and subspecies names can denote an aggregate of subspecies. This parenthetical name is not counted as a word of the trinomen. Distinguish this grouping within one species from a species aggregate, which groups species.",
)
SUBTRIBE = utils.vocabs.Term(
    labels=("subtribe",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/baefb9ce-5f98-44a7-acc3-5bd1247c8d54"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subtribe"),),
    description="Subtribe",
)
SUBVARIETY = utils.vocabs.Term(
    labels=(
        "subvariety",
        "subvarietas",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/cb2627f0-e121-474b-a354-dd0e392daa84"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/subvariety"),),
    description="Subvariety",
)
SUPERFAMILY = utils.vocabs.Term(
    labels=("superfamily",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/50d96a8d-aa2a-4629-9caa-76637c619851"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/superfamily"),),
    description="Superfamily",
)
SUPRAGENERICNAME = utils.vocabs.Term(
    labels=("supra generic name",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/a8889e2e-8eb3-4ed3-8d32-3974adae6158"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/supragenericname"),),
    description="Used for any other unspecific rank above genera.",
)
TRIBE = utils.vocabs.Term(
    labels=("tribe",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/40d5f3d3-dfbb-4718-9f66-29b5f735142f"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/tribe"),),
    description="Tribe",
)
UNRANKED = utils.vocabs.Term(
    labels=("unranked",),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/6e50f0de-0847-4db3-8bc3-f7e796ed32bf"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/unranked"),),
    description="Unranked",
)
VARIETY = utils.vocabs.Term(
    labels=(
        "variety",
        "varietas",
    ),
    iri=rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/6fa4ff0a-acc8-482b-a574-0ffbbab83ca5"),  # real URI
    exact_matches=(rdflib.URIRef("http://rs.gbif.org/vocabulary/gbif/rank/variety"),),
    description="Variety",
)


# Vocabulary
class TaxonRank(utils.vocabs.FlexibleVocabulary):
    vocab_id = "TAXON_RANK"
    definition = rdflib.Literal("A type of taxonRank.")
    base = "bdr-cv/attribute/taxonRank/"
    history_note = rdflib.Literal(
        "The skos:exactMatch links from TERN concepts to GBIF rank concepts were copied unchanged "
        "from the reviewed BDR taxonomic rank scheme "
        "(https://linked.data.gov.au/dataset/bdr/taxonomic-rank), which retained them from TERN source records. "
        "No additional mappings were inferred by BDR in this update. The GBIF subkingdom concept is reused "
        "directly and has no self-mapping.",
        lang="en",
    )
    proposed_scheme = rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/dd085299-ae86-4371-ae15-61dfa432f924")
    broader = rdflib.URIRef("http://linked.data.gov.au/def/tern-cv/1e4d7110-5f07-45ec-98e7-738236a8d8e0")
    default = None  # No default, ommitted if not provided
    terms = (
        CLASS,
        CULTIVAR,
        CULTIVARGROUP,
        FAMILY,
        FORM,
        GENUS,
        INFORMAL,
        INFRAGENERICNAME,
        INFRAORDER,
        INFRASPECIFICNAME,
        INFRASUBSPECIFICNAME,
        KINGDOM,
        ORDER,
        PHYLUM,
        SECTION,
        SERIES,
        SPECIES,
        SPECIESAGGREGATE,
        SUBFAMILY,
        SUBFORM,
        SUBGENUS,
        SUBKINGDOM,
        SUBORDER,
        SUBSECTION,
        SUBSERIES,
        SUBSPECIES,
        SUBSPECIFICAGGREGATE,
        SUBTRIBE,
        SUBVARIETY,
        SUPERFAMILY,
        SUPRAGENERICNAME,
        TRIBE,
        UNRANKED,
        VARIETY,
    )


# Register
utils.vocabs.register(TaxonRank)
