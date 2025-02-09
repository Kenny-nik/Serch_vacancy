def get_top(vacancies, n):
    return sorted(vacancies, key=lambda x: x.salary)[-n:]


def filter_vacancies(vacancies, keywords):
    if not keywords:
        return vacancies
    keywords_set = set(keywords)
    return [vacancy for vacancy in vacancies if any(keyword in vacancy.description for keyword in keywords_set)]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)