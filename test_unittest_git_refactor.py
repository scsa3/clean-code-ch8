"""Clean Code in Python - Chapter 8: Unit Testing and refactoring

> Tests for refactoring_2.py
"""
from unittest import TestCase

from git import MergeRequest, MergeRequestStatus


class TestMergeRequestStatus(TestCase):
    def setUp(self):
        self.merge_request = MergeRequest()

    def assert_rejected(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestStatus.REJECTED
        )

    def assert_pending(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestStatus.PENDING
        )

    def assert_approved(self):
        self.assertEqual(
            self.merge_request.status, MergeRequestStatus.APPROVED
        )

    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assert_rejected()

    def test_just_created_is_pending(self):
        self.assert_pending()

    def test_pending_awaiting_review(self):
        self.merge_request.upvote("core-dev")
        self.assert_pending()

    def test_approved(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.assert_approved()

    def test_no_double_approve(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev1")
        self.assert_pending()

    def test_upvote_changes_to_downvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")
        self.merge_request.downvote("dev1")

        self.assert_rejected()

    def test_downvote_to_upvote(self):
        self.merge_request.upvote("dev1")
        self.merge_request.downvote("dev2")
        self.merge_request.upvote("dev2")

        self.assert_approved()
