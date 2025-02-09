import json
import os
from typing import Any, Dict, List

from config import PATH_TO_JSON
from src.abstract_classes import AbstractEditJson
from src.vacancy import Vacancy


class EditJson(AbstractEditJson):
    """Класс для работы с JSON-файлами"""

    def __init__(self, file_name="vacancies.json") -> None:
        self.__file_name = file_name
        self.path_to_file = os.path.join(PATH_TO_JSON, self.__file_name)

        os.makedirs(os.path.dirname(self.path_to_file), exist_ok=True)
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, "w", encoding="utf-8") as file:
                json.dump([], file)

    def _reading_data(self) -> List[Dict[str, Any]]:
        """Чтение данных из JSON-файла"""
        with open(self.path_to_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def _saving_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохранение данных в JSON-файл"""
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_to_file(self, vacancies: List[Vacancy]) -> None:
        """Метод сохраняющий список вакансий в JSON-файл"""
        data = self._reading_data()
        for vacancy in vacancies:
            data.append(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "area": vacancy.area,
                    "salary": vacancy.salary,
                    "description": vacancy.description,
                }
            )
        self._saving_data(data)

    def get_vacancies(self) -> List[Vacancy]:
        """Метод получает список вакансий из файла"""
        data = self._reading_data()
        return [Vacancy(**item) for item in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод добавляет вакансии в существующий файл"""
        data = self._reading_data()
        data.append(
            {
                "name": vacancy.name,
                "url": vacancy.url,
                "area": vacancy.area,
                "salary": vacancy.salary,
                "description": vacancy.description,
            }
        )
        self._saving_data(data)

    def delete_vacancy(self, vacancy_name: str) -> None:
        """Метод удаляет выбранную вакансию"""
        data = self._reading_data()
        data = [item for item in data if item["name"] != vacancy_name]
        self._saving_data(data)

    def deleting_vacancies(self) -> None:
        """Метод очищает JSON-файл"""
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)