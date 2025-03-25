import psycopg2
import requests

from src.ABS_classes import BaseClass, Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, employer_id: int):
        self.__employer_url = f"https://api.hh.ru/employers/{employer_id}"
        self.__vacancy_url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        self.vacancies = []
        super().__init__(employer_id)


    def get_employer_data(self):
        """
        Получает данные о работодателе и его вакансиях по идентификатору работодателя.
        """
            # Получение информации о работодателе
        employer_response = requests.get(self.__employer_url, timeout=10)
        employer_data = employer_response.json()

            # Получение вакансий работодателя
        vacancy_response = requests.get(self.__vacancy_url, timeout=10)
        vacancy_data = vacancy_response.json()

        return employer_data, vacancy_data



class DBManager(BaseClass):
    """
    Основной класс для работы с postgresSQL
    """

    def __init__(self):
        self.__conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password='6221596Gord'
    )
        self._cur = self.__conn.cursor()
        super().__init__()

    def get_companies_and_vacancies_count(self, postgres_table):
        self._cur.execute(""
                          "SELECT DISTINCT employee_name, COUNT(vacansy_name) "
                          f"FROM {postgres_table} "
                          "GROUP BY employee_name")
        return self._cur.fetchall()


    def get_all_vacancies(self, postgres_table):
        self._cur.execute(""
                          "SELECT employee_name, vacansy_name, salary, vacansy_url "
                          f"FROM {postgres_table}")
        return self._cur.fetchall()


    def get_avg_salary(self, postgres_table):
        self._cur.execute(""
                          "SELECT AVG(salary) "
                          f"FROM {postgres_table} "
                          "WHERE salary > 0 ")
        return self._cur.fetchall()


    def get_vacancies_with_higher_salary(self, postgres_table):
        self._cur.execute(""
                          "SELECT vacansy_name, salary "
                          f"FROM {postgres_table} "
                          f"WHERE salary  >= (SELECT AVG(salary) from {postgres_table} WHERE salary > 0) "
                          "")
        return self._cur.fetchall()


    def get_vacancies_with_keyword(self,postgres_table, keyword):
        self._cur.execute(""
                          "SELECT vacansy_name, salary "
                          f"FROM {postgres_table} "
                          f"WHERE vacansy_name LIKE '%{keyword}%'")
        return self._cur.fetchall()
