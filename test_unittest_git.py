import unittest

from git import MergeRequest, MergeRequestStatus


class TestMergeRequestStatus(unittest.TestCase):

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvote("maintainer")
        self.assertEqual(merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_created_is_pending(self):
        self.assertEqual(MergeRequest().status, MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(
            merge_request.status, MergeRequestStatus.PENDING
        )

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")

        self.assertEqual(
            merge_request.status, MergeRequestStatus.APPROVED
        )

    def test_failure(self):
        self.fail()

    def test_exception(self):
        raise Exception
