from abc import ABC, abstractmethod

class GetVacanciesAbstractClass(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

class JSON_ABS(ABC):
    @abstractmethod
    def save_vacancies(self):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass
