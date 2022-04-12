import unittest

from fastapi.testclient import TestClient

from coms.server import app


class ClientTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = TestClient(app)
