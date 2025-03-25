from src.HH_info import info_from_hh
from src.classes import DBManager
from src.scratch import fill_pgadmin

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


if __name__ == '__main__':

    fill_pgadmin(info_from_hh(employer_ids))
    print(DBManager().get_all_vacancies('vacansys_from_HH'))
