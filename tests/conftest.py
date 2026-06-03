from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    # Arrange: snapshot mutable app state used by route handlers.
    original_activities = deepcopy(app_module.activities)

    # Act: create a client and yield it to the test.
    with TestClient(app_module.app) as test_client:
        yield test_client

    # Assert-equivalent cleanup: restore global state for test isolation.
    app_module.activities.clear()
    app_module.activities.update(original_activities)
