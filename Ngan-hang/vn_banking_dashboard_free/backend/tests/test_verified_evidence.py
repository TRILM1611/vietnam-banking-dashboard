import unittest
from types import SimpleNamespace
from fastapi import HTTPException

from main import validate_verified_evidence


class VerifiedEvidenceTests(unittest.TestCase):
    def test_unverified_record_does_not_require_evidence(self):
        validate_verified_evidence(SimpleNamespace(verification_status="unverified"))

    def test_verified_record_without_source_is_rejected(self):
        record = SimpleNamespace(
            verification_status="verified", value=1.0, unit="tỷ đồng",
            source_name=None, source_url=None, published_at=None,
            note=None, consolidation="not_disclosed",
        )
        with self.assertRaises(HTTPException) as ctx:
            validate_verified_evidence(record)
        self.assertEqual(ctx.exception.status_code, 422)

    def test_verified_record_with_complete_evidence_is_accepted(self):
        record = SimpleNamespace(
            verification_status="verified", value=1.0, unit="tỷ đồng",
            source_name="BCTC hợp nhất", source_url="https://example.com/report.pdf",
            published_at="2026-10-30", note="Đối chiếu thuyết minh số 12",
            consolidation="consolidated",
        )
        validate_verified_evidence(record)

    def test_verified_record_rejects_non_http_source(self):
        record = SimpleNamespace(
            verification_status="verified", value=1.0, unit="tỷ đồng",
            source_name="BCTC", source_url="file:///tmp/report.pdf",
            published_at="2026-10-30", note="Đối chiếu", consolidation="separate",
        )
        with self.assertRaises(HTTPException):
            validate_verified_evidence(record)


if __name__ == "__main__":
    unittest.main()
