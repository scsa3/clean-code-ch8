import pytest

from git_open_close import MergeRequest, MergeRequestException


def test_cannot_vote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
    with pytest.raises(
            MergeRequestException, match="can't vote on a closed merge request"
    ):
        merge_request.downvote("dev1")
