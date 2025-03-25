from abc import ABC, abstractmethod

import psycopg2


class BaseClass(ABC):
    def __init__(self):
        self.__conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password='6221596Gord'
    )
        self._cur = self.__conn.cursor()


class Parser(ABC):

    def __init__(self, employer_id: int):
        self.__employer_url = f"https://api.hh.ru/employers/{employer_id}"
        self.__vacancy_url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        self.vacancies = []


    @abstractmethod
    def get_employer_data(self):
        pass