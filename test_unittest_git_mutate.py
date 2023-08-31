import unittest

from git import MergeRequestStatus
from git_mutate import evaluate_merge_request


class TestMergeRequestEvaluate(unittest.TestCase):
    def test_approved(self):
        result = evaluate_merge_request(3, 0)
        self.assertEqual(result, MergeRequestStatus.APPROVED)
