from git import MergeRequest, MergeRequestStatus


def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestStatus.REJECTED


def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_approved():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")

    assert merge_request.status == MergeRequestStatus.APPROVED


def test_failure():
    assert False


def test_exception():
    raise Exception
