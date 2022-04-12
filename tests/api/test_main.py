from tests import testing


class IndexTests(testing.ClientTests):
    def test_returns_hello(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"status": "hello"}, response.json())
