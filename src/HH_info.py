from src.classes import HH

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


def info_from_hh(employer_ids):
    all_vacancies = [] #список всей информации с hh
    information = []  # employee_id, employee_name, [vacansy_url, vacansy_name, description, salary]
    for employer_id in employer_ids:
        all_vacancies.append(HH(employer_id).get_employer_data()) #выводим информацию с HH
    n = 0
    while True:
        information.append(all_vacancies[n][0]['id'])
        information.append(all_vacancies[n][0]['name'])
        vac_info = []
        for vac in all_vacancies[n][1]['items']:
            vac_info.append(vac['alternate_url'])
            vac_info.append(vac['name'])
            vac_info.append(vac['snippet']['responsibility'])
            if vac['salary'] is None:
                vac_info.append('Зарплата не указана')
            elif vac['salary']['to'] is not None:
                vac_info.append(vac['salary']['to'])
            elif vac['salary']['from'] is not None:
                vac_info.append(vac['salary']['from'])
            elif vac['salary']['from'] is not None and vac['salary']['to'] is not None:
                vac_info.append(vac['salary']['from'])
        information.append(vac_info)
        n += 1
        if n == len(employer_ids):
            break
    return information
