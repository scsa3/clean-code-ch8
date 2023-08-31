import unittest

from git_open_close import MergeRequest, MergeRequestException


class TestMergeRequestStatus(unittest.TestCase):
    def test_cannot_upvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaises(
            MergeRequestException, merge_request.upvote, "dev1"
        )

    def test_cannot_downvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            merge_request.downvote,
            "dev1",
        )
