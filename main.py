from src.utils import filter_vacancies, get_top, print_vacancies
from src.vacancy import Vacancy
from src.API import VacanciesRequest
from src.vacancy_json import EditJson


def user_interaction() -> None:

    print("Вас приветствует программа поиска вакансий с сайта hh.ru")
    search_query = input("Введите поисковый запрос: ")
    # search_query = ["Альфа-Банк"]
    filter_words = input("Введите ключевые слова для фильтрации вакансий разделяя пробелом: ").split()
    # filter_words = ["Менеджер"]
    top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    # top_n = 3
    print("Идет поиск вакансий...")

    hh_api = VacanciesRequest()
    hh_vacancies = hh_api.load_vacancies(search_query)

    vacancies_list = Vacancy.create_json(hh_vacancies)
    file = "vacancies.json"
    all_vacancy = EditJson(file)
    # all_vacancy.deleting_vacancies()
    all_vacancy.save_to_file(vacancies_list)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    if top_n:
        top_vacancies = get_top(filtered_vacancies, top_n)
    else:
        print("Выведено топ 3 вакансии")
        top_n = 3
        top_vacancies = get_top(filtered_vacancies, top_n)

    user_response = input("Сохранить вакансии в файл? (yes/no): ").lower()
    if user_response == "yes":
        filename = input("Введите название файла: ")
        if filename:
            file = f"{filename}.json"
            result = EditJson(file)
            result.deleting_vacancies()
            result.save_to_file(top_vacancies)
            print(f"Вакансии успешно сохранены в файл -> {file}")
        else:
            result = EditJson()
            result.deleting_vacancies()
            result.save_to_file(top_vacancies)
            print("Вакансии сохранены в файл по умолчанию -> vacancies.json")
    else:
        print("Вакансии не сохранены")

    if top_vacancies:
        print(f"Найдено {len(top_vacancies)} вакансий")
        print_vacancies(top_vacancies)
    else:
        print("Ничего не найдено по Вашим критериям")


if __name__ == "__main__":
    user_interaction()