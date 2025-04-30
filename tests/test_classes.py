import psycopg2

from src.classes import DBManager
from tests.conftest import test_table_vac_creator, test_table_emp_creator

test_table_vac_creator()
test_table_emp_creator()

def test_DBManager():
    assert DBManager().get_companies_and_vacancies_count('test_vac_table', 'test_emp_table')
    assert DBManager().get_all_vacancies('test_vac_table', 'test_emp_table')
    assert DBManager().get_avg_salary('test_vac_table', 'test_emp_table')
    assert DBManager().get_vacancies_with_higher_salary('test_vac_table', 'test_emp_table')
    assert DBManager().get_vacancies_with_keyword('test_vac_table',
                                                  'test_emp_table', 'Python')


def test_table_deleter():
    """Удаляет таблицы для проверки работоспособности основного класса"""

    conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password='6221596Gord'
    )

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS test_vac_table')
    cur.execute('DROP TABLE IF EXISTS test_emp_table')
    conn.commit()

    cur.close()
    conn.close()
