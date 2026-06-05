import logging
import pytest

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("test_cars")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test_search.log", encoding="utf-8")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", None),
    ("year", 1),
    (None, 5),
])
class TestCarSearch:
    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Запит GET /cars з параметрами: sort_by={sort_by}, limit={limit}")

        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"Статус відповіді: {response.status_code}")
        assert response.status_code == 200

        cars = response.json()
        logger.info(f"Отримано автомобілів: {len(cars)}")

        if limit:
            assert len(cars) <= limit
            logger.info(f"Перевірка ліміту пройшла: {len(cars)} <= {limit}")

        if sort_by and len(cars) > 1:
            values = [car[sort_by] for car in cars]
            assert values == sorted(values)
            logger.info(f"Перевірка сортування за '{sort_by}' пройшла")