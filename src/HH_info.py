from src.classes import HH


def info_from_hh(employer_ids):
    """Достает информацию из HH по списку ID работодателей,
    преобразует в список для передачи в postgres таблицу
    """

    all_vacancies = [] #список всей информации с hh
    information = []  #vacansy_url, vacansy_name, description, salary, employee_id, employee_name
    for employer_id in employer_ids:
        all_vacancies.append(HH(employer_id).get_employer_data()) #выводим информацию с HH
    n = 0
    while True:
        for vac in all_vacancies[n][1]['items']:
            information.append(vac['alternate_url'])
            information.append(vac['name'])
            information.append(vac['snippet']['responsibility'])
            if vac['salary'] is None:
                information.append(0)
            elif vac['salary']['to'] is not None:
                information.append(int(vac['salary']['to']))
            elif vac['salary']['from'] is not None:
                information.append(int(vac['salary']['from']))
            elif vac['salary']['from'] is not None and vac['salary']['to'] is not None:
                information.append(int(vac['salary']['from']))
            information.append(all_vacancies[n][0]['id'])
            information.append(all_vacancies[n][0]['name'])
            information.append(all_vacancies[n][0]['site_url'])
            information.append(all_vacancies[n][0]['description'])

        n += 1
        if n == len(employer_ids):
            break
    return information

