import requests

BASE_URL = "http://127.0.0.1:8080"
CARS_URL = f"{BASE_URL}/cars"

class CarsController:
    def __init__(self, session: requests.Session):
        self.session = session

    def search_cars(self, sort_by=None, limit=None):
        params = {}

        if sort_by is not None:
            params["sort_by"] = sort_by

        if limit is not None:
            params["limit"] = limit

        return self.session.get(
            CARS_URL,
            params=params,
            timeout=10,
        )
