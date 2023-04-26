import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='duman'
)

current = config.cursor()
# добавляем значения в таблицу
id = 1
name = 'Duman'
number = '87053059706'

sql = '''
    INSERT INTO phones VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()
