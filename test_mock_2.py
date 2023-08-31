import unittest
from unittest import mock

from mock_2 import BuildStatus, STATUS_ENDPOINT


class TestMock2(unittest.TestCase):
    @mock.patch("mock_2.requests")
    def test_notify(self, mock_requests):
        build_date = "2018-01-01T00:00:01"
        with mock.patch("mock_2.BuildStatus.build_date", return_value=build_date):
            BuildStatus.notify(123, "OK")

        expected_payload = {"id": 123, "status": "OK", "built_at": build_date}
        mock_requests.post.assert_called_with(
            STATUS_ENDPOINT, json=expected_payload
        )
