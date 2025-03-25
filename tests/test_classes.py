from src.classes import DBManager
from tests.conftest import test_table_creator

test_table_creator()

def test_DBManager():
    assert DBManager().get_companies_and_vacancies_count('test_table')
    assert DBManager().get_all_vacancies('test_table')
    assert DBManager().get_avg_salary('test_table')
    assert DBManager().get_vacancies_with_higher_salary('test_table')
    assert DBManager().get_vacancies_with_keyword('test_table','Python')
