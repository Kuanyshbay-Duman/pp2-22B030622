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
        CREATE TABLE ss(
            username VARCHAR(100) PRIMARY KEY,
            level VARCHAR(12),
            score VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()
