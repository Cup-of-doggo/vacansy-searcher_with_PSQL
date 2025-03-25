from src.HH_info import info_from_hh


test_employers_id = [1,2,3]

def test_info_from_hh():
    assert info_from_hh(test_employers_id) == []