import psycopg2

from src.HH_info import info_from_hh, employer_ids

info_for_database = info_from_hh(employer_ids)

conn = psycopg2.connect(
    host='localhost',
    database='employers',
    user='postgres',
    password='6221596Gord'
)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS employers_from_HH')
cur.execute('CREATE TABLE employers_from_HH'
            '('
            'employee_id int PRIMARY KEY,'
            'employee_name varchar(1000),'
            'vacansy_url varchar(1000),'
            'vacansy_name varchar(1000),'
            'salary varchar(1000),'
            'description text'
            ');')
cur.execute('SELECT * FROM employers_from_HH')
conn.commit()
n = 0
s = 2

while True:
    x = 0
    if n < len(info_for_database):
        cur.execute('INSERT INTO employers_from_HH '
                    '(employee_id, employee_name, vacansy_url, vacansy_name, description, salary) VALUES (%s, %s, %s, %s, %s, %s);'
                    ,(info_for_database[n], info_for_database[n+1], info_for_database[s][x], info_for_database[s][x+1], info_for_database[s][x+2],info_for_database[s][x+3]))
        n += 3
        s += 3
        x += 4
    if n == len(info_for_database):
        break

conn.commit()

#rows = cur.fetchall()

cur.close()
conn.close()

#CREATE TABLE post
#(
#    post_id int PRIMARY KEY,
#    title varchar(100) NOT NULL,
#    content text
#);
#
#INSERT INTO post VALUES (1, 'Happy New Year', '');
#INSERT INTO post VALUES
#(2, 'My plans for 2023', ''),
#(3, 'Lesson learned from 2022', ''),
#(4, 'NewPost!', '');
#SELECT * FROM post;





def filling_out_the_table():
    pass
