import csv
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    password='duman',
    user='postgres'
)
current = config.cursor()
arr = []
# вставляем данные в телефонную книгу загружая их из csv-файла
with open('example.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phones VALUES (%s, %s, %s) RETURNING *; 
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()


current.close()
config.commit()
config.close()
