import json
import os

import pytest

from src.vacancy import Vacancy

current_directory = os.path.dirname(os.path.abspath(__file__))
PATH_TO_DATA_TEST = os.path.abspath(os.path.join(current_directory, "../data/data_test.json"))


@pytest.fixture
def test_vacancy():
    return Vacancy(
        "Junior Python Engineer",
        "https://hh.ru/vacancy/110646488",
        "Минск",
        150000,
        "1+ year of professional work experience",
    )


@pytest.fixture
def test_vacancy_2():
    return Vacancy("Junior Python Engineer", "https://hh.ru/vacancy/110646488", None, None, None)


@pytest.fixture
def list_vacancies():
    return [
        Vacancy(
            "Junior Python Engineer",
            "https://hh.ru/vacancy/110646488",
            "Минск",
            150000,
            "1+ year of professional work experience",
        ),
        Vacancy(
            "Python-разработчик (Junior - Middle)",
            "https://hh.ru/vacancy/110423905",
            "Вологда",
            70000,
            "Рython3+. Django 2+, опыт работы от 1 года. "
            "Django REST Framework. MySQL. MariaDB. Умение работать с git. "
        ),
        Vacancy(
            "Middle Python разработчик",
            "https://hh.ru/vacancy/110956175",
            "Москва",
            100000,
            "Разработка и поддержка веб-приложений на Python "
            "с использованием Django и FastAPI (опыт от 3 лет). Глубокое знание принципов ООП..."
        ),
    ]


@pytest.fixture
def json_data():
    with open(PATH_TO_DATA_TEST, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data