from abc import ABC, abstractmethod

class AbstractApi(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

class AbstactEditJson(ABC):


    @abstractmethod
    def add_vacancies(self, stock_list):
        pass

    @abstractmethod
    def delete_vacancies(self, words_del):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_to_file(self, vacancies):
        pass
