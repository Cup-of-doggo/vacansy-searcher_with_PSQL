from src.scratch import fill_vac_table, fill_emp_table

test_info = []
def test_fill_pgadmin():
    assert fill_vac_table(test_info) == None
    assert fill_emp_table(test_info) == None