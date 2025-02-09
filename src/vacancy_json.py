import json

import os

from idlelib.iomenu import encoding

from src.abstract_classes import AbstactEditJson

from config import PATH_TO_JSON

from src.vacancy import Vacancy



class EditJson(AbstactEditJson):

    def __init__(self, file_name = "vacancies.json"):
        self.__file_name = file_name
        self.path_to_file = os.path.join(PATH_TO_JSON, self.__file_name)

        os.makedirs(os.path.dirname(self.path_to_file), exist_ok=True)
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, "w", encoding="utf-8") as file:
                json.dump([], file)

    def _reading_data (self):
        with open(self.path_to_file, "r", encoding="utf-8") as file:
            json.load(file)

    def _saving_data (self, data):
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_to_file(self, vacancies):
        data = self._reading_data()
        for vacancy in vacancies:
            data.append(
                {
                    "name": vacancy.name,
                    "url": vacancy.url,
                    "area": vacancy.area,
                    "salary": vacancy.salary,
                    "description": vacancy.description
                }
            )
        self._saving_data(data)


    def get_vacancies(self):
        data = self._reading_data()
        return [Vacancy(**item) for item in data]


    def add_vacancies(self, vacancy: Vacancy):
        data = self._reading_data()
        data.append(
            {
                "name": vacancy.name,
                "url": vacancy.url,
                "area": vacancy.area,
                "salary": vacancy.salary,
                "description": vacancy.description
            }
        )
        self._saving_data(data)


    def delete_vacancies(self, vacancy_name):
        data = self._reading_data()
        data = [item for item in data if item["name"] != vacancy_name]
        self._saving_data(data)


    def deleting_vacancies (self):
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

