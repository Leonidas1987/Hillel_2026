
import logging
from pathlib import Path

import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"
CARS_URL = f"{BASE_URL}/cars"
LOG_FILE = Path(__file__).resolve().parent / "test_search.log"


# создание логирование в консоль и файл
logger = logging.getLogger("cars_api_tests")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        LOG_FILE, mode="w", encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


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


@pytest.mark.usefixtures("api_session")
class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 3),
            ("brand", 4),
            ("engine_volume", 6),
            (None, 2),
            ("price", None),
            ("year", 10),
        ],
    )
    def test_search_cars(self, sort_by, limit):
        params = {}

        if sort_by is not None:
            params["sort_by"] = sort_by

        if limit is not None:
            params["limit"] = limit

        logger.info(
            "Searching cars: sort_by=%s, limit=%s",
            sort_by,
            limit,
        )

        response = self.session.get(
            CARS_URL,
            params=params,
            timeout=10,
        )

        logger.info(
            "GET %s returned status %s",
            response.url,
            response.status_code,
        )

        assert response.status_code == 200

        cars = response.json()

        assert isinstance(cars, list)

        expected_count = limit if limit is not None else 25
        assert len(cars) == expected_count

        sort_key = sort_by or "brand"
        actual_values = [car[sort_key] for car in cars]

        assert actual_values == sorted(actual_values)

        logger.info(
            "Test passed: returned %s cars, sorted by %s",
            len(cars),
            sort_key,
        )
