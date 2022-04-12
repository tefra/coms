import os
from typing import Any


def pytest_configure(*args: Any, **kwargs: Any):
    os.environ["ENVIRONMENT"] = "test"
