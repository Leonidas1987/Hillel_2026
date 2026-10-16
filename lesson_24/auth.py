
import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"

logger = logging.getLogger("cars_api_tests")

@pytest.fixture(scope="class")
def api_session(request):
    session = requests.Session()

    try:
        logger.info("Starting API authentication")

        response = session.post(
            AUTH_URL,
            auth=HTTPBasicAuth("test_user", "test_pass"),
            timeout=10,
        )

        logger.info(
            "Authentication response: %s",
            response.status_code,
        )

        assert response.status_code == 200, (
            f"Authentication failed: {response.text}"
        )

        access_token = response.json().get("access_token")
        assert access_token, "Access token was not returned"

        session.headers.update({
            "Authorization": f"Bearer {access_token}"
        })

        request.cls.session = session

        logger.info("Authentication successful")

        yield session

    except Exception:
        logger.exception("API session setup failed")
        raise

    finally:
        session.close()
        logger.info("API session closed")
