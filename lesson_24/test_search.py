import logging
from pathlib import Path
import pytest

from auth import api_session
from controller import CarsController


LOG_FILE = Path(__file__).resolve().parent / "test_search.log"

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
        LOG_FILE,
        mode="w",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


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
        controller = CarsController(self.session)

        logger.info(
            "Searching cars: sort_by=%s, limit=%s",
            sort_by,
            limit,
        )

        response = controller.search_cars(
            sort_by=sort_by,
            limit=limit,
        )

        logger.info(
            "GET /cars returned status %s",
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
