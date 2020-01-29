from searcher.serializers import ResultSchema
from .base import TestBase


class TestsApi(TestBase):
    def test_get_success(self):
        json_resp = self.get("main.main", q="Test query")
        assert ResultSchema(many=True).load(json_resp)
