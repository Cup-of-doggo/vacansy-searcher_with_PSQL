from abc import ABC, abstractmethod


class BaseClass(ABC):
    def __init__(self):
        pass



class Parser(ABC):

    def __init__(self, employer_id: int):
        self.__employer_url = f"https://api.hh.ru/employers/{employer_id}"
        self.__vacancy_url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        self.vacancies = []


    @abstractmethod
    def get_employer_data(self):
        pass