from src.HH_info import info_from_hh
from src.classes import DBManager
from src.scratch import fill_vac_table, database_creator, fill_emp_table
from dotenv import load_dotenv


employer_ids = [
    4509259,
    3152,
    3344320,
    9418714,
    135317,
    972961,
    1815369,
    9805014,
    1440683,
    1749518,
]


def main():
    """Основная функция для вывода информации в базу данных и консоль"""
    database_creator()
    fill_vac_table(info_from_hh(employer_ids))
    fill_emp_table(info_from_hh(employer_ids))
    print('Здравствуйте, если вы хотите получить список всех работодателей и количество их вакансии напишите "1",'
          '\nесли вы хотите получить полный список вакансий у работодателей нажмите "2",'
          '\nесли вы хотите посмотреть среднюю зарплату у работодателей нажмите "3",'
          '\nесли вы хотите получить список вакансий с зарплатой выше среднего нажмите "4",'
          '\nесли вы хотите найти какую то конкретную вакансию нажмите "5", затем напишите какую.')
    user_input =  input()

    if user_input == '1':
        info = DBManager().get_companies_and_vacancies_count('vacansys_from_HH',
                                                             'employ_from_HH')
        return info

    elif user_input == '2':
        info = DBManager().get_all_vacancies('vacansys_from_HH',
                                                             'employ_from_HH')
        return info

    elif user_input == '3':
        info = DBManager().get_avg_salary('vacansys_from_HH',
                                                             'employ_from_HH')
        return info

    elif user_input == '4':
        info = DBManager().get_vacancies_with_higher_salary('vacansys_from_HH',
                                                             'employ_from_HH')
        return info

    elif user_input == '5':
        print("Введите слово для поиска:")
        keyword_input = input()
        info = DBManager().get_vacancies_with_keyword('vacansys_from_HH',
                                                             'employ_from_HH',keyword_input)
        return info


print(main())

