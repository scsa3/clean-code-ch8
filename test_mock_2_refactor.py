import unittest
from unittest.mock import Mock

from mock_2_refactor import BuildStatus


class TestMock2(unittest.TestCase):
    def test_notify(self):
        build_status = BuildStatus(Mock())
        build_status.build_date = Mock(return_value="2018-01-01T00:00:01")
        build_status.notify(1234, "OK")

        expected_payload = {
            "id": 1234,
            "status": "OK",
            "built_at": build_status.build_date(),
        }

        build_status.transport.post.assert_called_with(
            build_status.endpoint, json=expected_payload
        )
