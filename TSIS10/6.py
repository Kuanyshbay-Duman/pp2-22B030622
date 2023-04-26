import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    password='duman',
    user='postgres'
)

current = config.cursor()

# запрос id, name, number по отсортированному имени
sql1 = '''
    SELECT id, name, number FROM phones ORDER BY name ASC
'''
# запрос номера телефона определенного человека
sql2 = '''
    SELECT number FROM phones WHERE name = 'Nuray'
'''
current.execute(sql2)

final = current.fetchall()
print(final)
current.close()
config.commit()
config.close()
