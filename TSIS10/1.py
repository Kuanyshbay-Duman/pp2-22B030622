import psycopg2
# создаем таблицу телефонной книги
config = psycopg2.connect(
    host='localhost',
    database='postgres',
    password='duman',
    user='postgres'
)

current = config.cursor()
sql = '''
        CREATE TABLE phones(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()
