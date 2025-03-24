import psycopg2

from src.HH_info import info_from_hh, employer_ids

info_for_database = info_from_hh(employer_ids)

def fill_pgadmin(info_for_database):

    conn = psycopg2.connect(
        host='localhost',
        database='employers',
        user='postgres',
        password='6221596Gord'
    )

    cur = conn.cursor()

    s = 0

    cur.execute('DROP TABLE IF EXISTS vacansys_from_HH')
    cur.execute('CREATE TABLE vacansys_from_HH'
                '('
                'employee_id int,'
                'employee_name varchar(100),'
                'vacansy_url varchar(100),'
                'vacansy_name varchar(100),'
                'salary int,'
                'description text'
                ');')
    while True:
        if s < len(info_for_database):
            cur.execute('INSERT INTO vacansys_from_HH '
                        '(vacansy_url, vacansy_name, description, salary, employee_id, employee_name) VALUES (%s, %s, %s, %s, %s, %s);'
                        , (info_for_database[s], info_for_database[s+1], info_for_database[s+2], info_for_database[s+3], info_for_database[s+4], info_for_database[s+5]))

            s += 6
        if s == len(info_for_database):
            break
    cur.execute('SELECT * FROM employers_from_HH')
    conn.commit()


    cur.close()
    conn.close()
