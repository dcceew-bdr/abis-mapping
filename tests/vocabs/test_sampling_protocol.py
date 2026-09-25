"""Tests the sampling protocol vocabulary."""

# Third-Party
import pytest
import rdflib

# Local
from abis_mapping import utils
from tests import helpers


@pytest.mark.parametrize(
    ("wildnet_code", "canonical_iri"),
    (
        ("ANA", "https://linked.data.gov.au/def/nrm/e405c9c0-2c1f-5dee-8d63-1edfc6ee5b36"),
        ("BAT", "https://linked.data.gov.au/def/nrm/b7a02786-f651-5199-877b-96d5dc4c66c6"),
        ("CAM", "https://linked.data.gov.au/def/nrm/d9ded7e1-e012-53c0-a612-3f5585281cef"),
        ("CAT", "https://linked.data.gov.au/def/nrm/8f6764de-0f3e-5f6f-b86e-e5e9f6053e24"),
        ("ELT", "https://linked.data.gov.au/def/nrm/d1bdaf17-c484-59c6-84a0-8344a5ce5b5c"),
        ("FUT", "https://linked.data.gov.au/def/nrm/970058a7-946d-5a5d-bb5b-c5b801a4def4"),
        ("HTS", "https://linked.data.gov.au/def/nrm/7ed366d3-9c85-5974-863d-127d1ff103ce"),
        ("MIT", "https://linked.data.gov.au/def/nrm/8ca1c330-b64a-5f97-aab4-9023fddaf009"),
        ("PIT", "https://linked.data.gov.au/def/nrm/aa78fa0e-3bd0-5c87-8ac7-0779f0699a11"),
        ("PLY", "https://linked.data.gov.au/def/nrm/c85935df-7a5d-4321-9915-efb7116e9020"),
        ("SPT", "https://linked.data.gov.au/def/nrm/db0cb2f2-e9f8-5679-a566-afce45b28da0"),
        ("UNK", "https://linked.data.gov.au/def/nrm/f6b0f6d8-16d8-5dd7-b1b7-66b0c020b96f"),
    ),
)
def test_wildnet_code_uses_canonical_iri(wildnet_code: str, canonical_iri: str) -> None:
    """Tests that known WildNet codes do not create pending concepts."""
    graph = rdflib.Graph()
    vocab_class = utils.vocabs.get_flexible_vocab("SAMPLING_PROTOCOL")
    vocab = vocab_class(
        graph=graph,
        source=helpers.TEST_DATASET_IRI,
        submitted_on_date=helpers.TEST_SUBMITTED_ON_DATE,
    )

    assert vocab.get(wildnet_code) == rdflib.URIRef(canonical_iri)
    assert len(graph) == 0
