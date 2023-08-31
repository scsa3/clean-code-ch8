from git import MergeRequestStatus


def evaluate_merge_request(upvotes_count, downvotes_count):
    if downvotes_count > 0:
        return MergeRequestStatus.REJECTED
    if upvotes_count >= 2:
        return MergeRequestStatus.APPROVED
    return MergeRequestStatus.PENDING
