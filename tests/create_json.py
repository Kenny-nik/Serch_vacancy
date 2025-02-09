from src.API import VacanciesRequest
from src.vacancy_json import EditJson

hh_api = VacanciesRequest()
hh_vacancies = hh_api.load_vacancies("Python-developer")

def lool():
    vacancies_list = []
    for item in hh_vacancies:
        while len(vacancies_list) <= 2:
            vacancies_list.append(item)

    all_vacancy = EditJson("data_test.json")
    all_vacancy._saving_data(vacancies_list)
    return all_vacancy
lool()