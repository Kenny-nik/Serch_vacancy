from src.vacancy import Vacancy


def test_vacancy_init(test_vacancy):
    assert test_vacancy.name == "Junior Python Engineer"
    assert test_vacancy.url == "https://hh.ru/vacancy/110646488"
    assert test_vacancy.area == "Минск"
    assert test_vacancy.salary == 150000
    assert test_vacancy.description == "1+ year of professional work experience"


def test_vacancy_validate(test_vacancy_2):
    assert test_vacancy_2.name == "Junior Python Engineer"
    assert test_vacancy_2.url == "https://hh.ru/vacancy/110646488"
    assert test_vacancy_2.area == "Регион отсутствует"
    assert test_vacancy_2.salary == 0
    assert test_vacancy_2.description == "Описание отсутствует"


def test_vacancy_str(test_vacancy, test_vacancy_2):
    assert str(test_vacancy) == (
        "Junior Python Engineer: 1+ year of professional work experience, регион: Минск, зарплата: 150000, ссылка: https://hh.ru/vacancy/110646488"
    )
    assert str(test_vacancy_2) == (
        "Junior Python Engineer: Описание отсутствует, регион: Регион отсутствует, зарплата: Нет данных, ссылка: https://hh.ru/vacancy/110646488"
    )


def test_create_json(json_data):
    result = Vacancy.create_json(json_data)
    assert len(result) == 3
    assert result[0].name == "Стажер Python Developer"
    assert result[0].url == "https://hh.ru/vacancy/116876598"
    assert result[0].area == "Ташкент"
    assert result[0].salary == 0
    assert result[0].description == (
        "Experience: Minimum of 1 years of professional experience in <highlighttext>Python</highlighttext> <highlighttext>development</highlighttext>. - Portfolio: Proven track record of successful projects and contributions..."
    )