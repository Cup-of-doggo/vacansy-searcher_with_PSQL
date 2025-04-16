import os
from abc import ABC, abstractmethod

import psycopg2
from dotenv import load_dotenv

load_dotenv()

class BaseClass(ABC):
    """Абстрактный класс для подключения к postgres"""
    def __init__(self):
        self.__conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password=os.getenv('PSQL_PASSWORD')
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