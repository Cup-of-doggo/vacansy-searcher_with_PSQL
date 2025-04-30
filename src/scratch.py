import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def fill_vac_table(info_for_database):
    """Заполняет таблицу вакансий в pgAdmin переданными данными:
    vacansy_url, vacansy_name, description, salary, employee_id, employee_name
    """

    conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password=os.getenv('PSQL_PASSWORD')
    )

    cur = conn.cursor()

    s = 0

    cur.execute('DROP TABLE IF EXISTS vacansys_from_HH')
    cur.execute('CREATE TABLE vacansys_from_HH'
                '('
                'employee_id int,'
                'vacansy_url varchar(100),'
                'vacansy_name varchar(100),'
                'salary int,'
                'description text'
                ');')
    while True:
        if s < len(info_for_database) - 1:
            cur.execute('INSERT INTO vacansys_from_HH '
                        '(vacansy_url, vacansy_name, description, salary, employee_id) '
                        'VALUES (%s, %s, %s, %s, %s);'
                        , (info_for_database[s], info_for_database[s+1], info_for_database[s+2],
                           info_for_database[s+3], info_for_database[s+4]))

            s += 8
        if s == len(info_for_database):
            break
    cur.execute('SELECT * FROM vacansys_from_HH')
    conn.commit()


    cur.close()
    conn.close()


def fill_emp_table(info_for_database):
    """Заполняет таблицу работодателей в pgAdmin переданными данными:
    vacansy_url, vacansy_name, description, salary, employee_id, employee_name
    """

    conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password=os.getenv('PSQL_PASSWORD')
    )

    cur = conn.cursor()

    s = 0

    cur.execute('DROP TABLE IF EXISTS employ_from_HH')
    cur.execute('CREATE TABLE employ_from_HH'
                '('
                'employee_id int,'
                'employee_name varchar(100),'
                'employee_site varchar(100),'
                'employee_description text'
                ');')
    while True:
        if s < len(info_for_database):
            cur.execute('INSERT INTO employ_from_HH '
                        '(employee_id, employee_name,  employee_site, employee_description) '
                        'VALUES (%s, %s, %s, %s);'
                        , (info_for_database[s+4], info_for_database[s+5], info_for_database[s+6],
                           info_for_database[s+7]))

            s += 8
        if s == len(info_for_database):
            break
    cur.execute('SELECT * FROM employ_from_HH')
    conn.commit()


    cur.close()
    conn.close()


def database_creator():
    """Создает базу данных в postgres"""
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password=os.getenv('PSQL_PASSWORD'),
        host="localhost",
        port="5432"
    )

    conn.autocommit = True

    cur = conn.cursor()

    # Создание новой базы данных
    cur.execute('DROP DATABASE IF EXISTS employers')
    cur.execute('CREATE DATABASE employers;')
    conn.commit()

    cur.close()
    conn.close()
