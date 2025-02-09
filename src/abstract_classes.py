from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """Абстрактный класс для работы с API по поиску вакансий"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Получение вакансий по поисковому запросу"""
        pass


class AbstractEditJson(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def add_vacancy(self, stock_list) -> None:
        """Метод добавляет вакансию в существующий файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, words_del) -> None:
        """Метод удаляет выбранную вакансию"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод получает список вакансий из файла"""
        pass

    @abstractmethod
    def save_to_file(self, vacancies) -> None:
        """Метод сохраняющий список вакансий в JSON-файл"""
        pass