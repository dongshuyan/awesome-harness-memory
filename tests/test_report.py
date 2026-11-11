import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "report" / "index.html"
MANIFEST = ROOT / "report" / "MANIFEST.json"


class ReportContract(unittest.TestCase):
    def test_published_report_matches_manifest_and_counts(self):
        report = REPORT.read_text(encoding="utf-8")
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

        self.assertEqual(
            hashlib.sha256(REPORT.read_bytes()).hexdigest(),
            manifest["source_sha256"],
        )
        self.assertNotIn("review", manifest)
        self.assertNotIn("/Volumes/", report)
        self.assertNotIn("file://", report)
        self.assertIn("lens-map-svg", report)
        self.assertIn("coverage-matrix", report)

        facts = self._json_constant(report, "atlasFacts")
        comparisons = self._json_constant(report, "atlasComparisons")
        research = facts["research"]
        engineering = facts["engineering"]
        expected = {
            f'{engineering_item["id"]}/{research_item["id"]}'
            for engineering_item in engineering
            for research_item in research
        }

        self.assertEqual(len(research), manifest["counts"]["research_perspectives"])
        self.assertEqual(len(engineering), manifest["counts"]["engineering_entries"])
        self.assertEqual(len(comparisons), manifest["counts"]["pairs"])
        self.assertEqual(set(comparisons), expected)
        self.assertEqual(len({item["id"] for item in research}), len(research))
        self.assertEqual(len({item["id"] for item in engineering}), len(engineering))

        coverage = {}
        for item in engineering:
            coverage[item["coverage"]] = coverage.get(item["coverage"], 0) + 1
        self.assertEqual(coverage.get("深度对照"), manifest["counts"]["engineering_evidence_status"]["deep_comparison"])
        self.assertEqual(coverage.get("目录级对照"), manifest["counts"]["engineering_evidence_status"]["catalogue_level"])
        self.assertEqual(coverage.get("目录级对照（身份暂定）", 0), manifest["counts"]["engineering_evidence_status"]["catalogue_level_identity_tentative"])
        self.assertEqual(coverage.get("待补证"), manifest["counts"]["engineering_evidence_status"]["pending_evidence"])

    @staticmethod
    def _json_constant(source, name):
        marker = f"const {name}="
        start = source.index(marker) + len(marker)
        value, _ = json.JSONDecoder().raw_decode(source[start:])
        return value

    def test_readmes_expose_the_public_report_without_private_paths(self):
        expected = "https://dongshuyan.github.io/awesome-harness-memory/report/index.html"
        for name in ("README.md", "README.zh-CN.md"):
            content = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn(expected, content)
            self.assertNotIn("/Volumes/", content)
            self.assertNotIn("file://", content)


if __name__ == "__main__":
    unittest.main()
