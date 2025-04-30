import psycopg2


def test_table_vac_creator():
    """Создает таблицу для проверки работоспособности основного класса"""
    conn = psycopg2.connect(
            host='localhost',
            database='employers',
            user='postgres',
            password='6221596Gord'
        )

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS test_vac_table')
    cur.execute('CREATE TABLE test_vac_table'
                '('
                'employee_id int,'
                'vacansy_url varchar(100),'
                'vacansy_name varchar(100),'
                'salary int,'
                'description text'
                ');')
    cur.execute('INSERT INTO test_vac_table '
                            '(vacansy_url, vacansy_name, description, salary, employee_id) '
                            'VALUES (%s, %s, %s, %s, %s);'
                            , ('https://hh.ru/some_vacancy/777777777','Python developer',
                               'умение тыкать по клавиатуре', 500000, 77777))
    cur.execute('SELECT * FROM test_vac_table')
    conn.commit()

    cur.close()
    conn.close()


def test_table_emp_creator():
    """Создает таблицу для проверки работоспособности основного класса"""
    conn = psycopg2.connect(
            host='localhost',
            database='employers',
            user='postgres',
            password='6221596Gord'
        )

    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS test_emp_table')
    cur.execute('CREATE TABLE test_emp_table'
                '('
                'employee_id int,'
                'employee_name varchar(100)'
                ');')
    cur.execute('INSERT INTO test_emp_table '
                            '(employee_id,employee_name) '
                            'VALUES (%s, %s);'
                            , (77777, 'Крутая IT-Компания'))
    cur.execute('SELECT * FROM test_emp_table')
    conn.commit()

    cur.close()
    conn.close()
