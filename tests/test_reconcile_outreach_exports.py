"""Tests for privacy-preserving outreach-export reconciliation."""
from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from tools.reconcile_outreach_exports import reconcile


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(headers)
        writer.writerows(rows)


class ReconcileOutreachExportsTests(unittest.TestCase):
    def test_matches_sent_and_reply_without_exposing_private_fields(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            queue = root / "queue.csv"
            sent = root / "sent.csv"
            replies = root / "replies.csv"
            write_csv(queue, ["prospect_id", "email"], [
                ["P-001", "buyer@example.org"],
                ["P-002", "other@example.org"],
            ])
            write_csv(sent, ["To", "Date", "Message-ID", "Thread-ID", "Subject", "Body"], [
                ["buyer@example.org", "2026-10-25T09:00:00Z", "<m1>", "thread-1", "Private subject", "Private body"],
                ["buyer@example.org", "2026-10-25T09:00:00Z", "<m1>", "thread-1", "Private subject", "Private body"],
                ["unknown@example.org", "2026-10-25T09:01:00Z", "<m2>", "thread-2", "Other", "Secret"],
                ["buyer@example.org", "", "<draft>", "thread-draft", "Draft", "Not sent"],
            ])
            write_csv(replies, ["From", "Date", "In-Reply-To", "Thread-ID", "Subject", "Body"], [
                ["buyer@example.org", "2026-10-25T10:00:00Z", "<m1>", "thread-1", "Re: Private", "Private reply"],
                ["unknown@example.org", "2026-10-25T10:01:00Z", "<missing>", "thread-x", "Unknown", "Secret reply"],
            ])

            report = reconcile(queue, sent, replies)

            self.assertEqual(report["matched_evidence"]["unique_sent_messages"], 1)
            self.assertEqual(report["matched_evidence"]["unique_received_replies"], 1)
            self.assertEqual(report["unmatched_or_invalid"]["unmatched_sent_rows"], 1)
            self.assertEqual(report["unmatched_or_invalid"]["sent_rows_missing_timestamp"], 1)
            self.assertEqual(report["unmatched_or_invalid"]["unmatched_reply_rows"], 1)
            self.assertEqual(report["prospects"][0]["prospect_id"], "P-001")
            self.assertEqual(report["prospects"][0]["evidence_status"], "REPLY_EVIDENCE")
            serialized = str(report)
            for private_value in ("buyer@example.org", "Private subject", "Private body", "Secret reply"):
                self.assertNotIn(private_value, serialized)
            self.assertIn("qualified enquiry", report["claims_not_established"])
            self.assertIn("payment received", report["claims_not_established"])

    def test_ambiguous_queue_email_is_not_guessed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            queue, sent, replies = root / "queue.csv", root / "sent.csv", root / "replies.csv"
            write_csv(queue, ["prospect_id", "email"], [
                ["P-001", "shared@example.org"],
                ["P-002", "shared@example.org"],
            ])
            write_csv(sent, ["To", "Date", "Message-ID"], [
                ["shared@example.org", "2026-10-25", "<m1>"],
            ])
            write_csv(replies, ["From", "Date", "Message-ID"], [])
            report = reconcile(queue, sent, replies)
            self.assertEqual(report["matched_evidence"]["unique_sent_messages"], 0)
            self.assertEqual(report["unmatched_or_invalid"]["unmatched_sent_rows"], 1)


if __name__ == "__main__":
    unittest.main()
