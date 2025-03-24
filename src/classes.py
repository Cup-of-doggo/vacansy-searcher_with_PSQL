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

    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
