import os
from src.HH_info import info_from_hh
from src.classes import DBManager
from src.scratch import fill_pgadmin
from dotenv import load_dotenv
import psycopg2


load_dotenv()


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
    conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password=os.getenv('PSQL_PASSWORD'),
           host="localhost",
            port="5432"
        )

    conn.autocommit = True

    cur = conn.cursor()

    #Создание новой базы данных
    cur.execute('DROP DATABASE IF EXISTS employers')
    cur.execute('CREATE DATABASE employers;')
    conn.commit()

    cur.close()
    conn.close()

    fill_pgadmin(info_from_hh(employer_ids))
    vac = DBManager().get_all_vacancies('vacansys_from_HH')
    return vac

print(main())