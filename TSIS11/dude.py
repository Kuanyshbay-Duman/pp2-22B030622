import psycopg2
import re


conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='duman'
)
cur = conn.cursor()


cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_bk(a VARCHAR)
      RETURNS SETOF phonebook 
   AS
   $$
      SELECT * FROM phonebook WHERE name = a OR number = a;
   $$
   language sql;
   '''
)


cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_to_phonebook(i INTEGER, nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM phonebook WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE phonebook
               SET  number = phon
               WHERE name = nm;
         ELSE
            INSERT INTO phonebook(id, name,  number) VALUES (i, nm, phon);
            END IF;
      END;
      $$;''')


cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
  invalid_users TEXT[][];
BEGIN 
   FOREACH i SLICE 1 IN ARRAY users
   LOOP
    IF LENGTH(i[3]) != 11 THEN
        invalid_users := array_cat(invalid_users, ARRAY[i]);
    ELSE
        INSERT INTO phonebook (id, name, number) VALUES (CAST(i[1] AS INTEGER ), i[2], i[3]);
    END IF;
END LOOP;
 
    IF array_length(invalid_users, 1) > 0 THEN
        RAISE NOTICE 'The following users have invalid phone numbers: %', invalid_users;
    END IF;
END
$$;
''')


cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF phonebook
AS $$
   SELECT * FROM phonebook
 ORDER BY id
 LIMIT a OFFSET b;
$$
language sql;""")


cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_phonebook(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM phonebook WHERE name = nm);
 IF cnt IS NOT NULL THEN
        DELETE FROM phonebook
  WHERE name=nm;
    END IF;
END;
$$;""")


a = input('search\ninsert\ninsertloop\ndelete\npaginating\n')
if a == 'search':
    cur.execute("SELECT search_from_bk('87054566677')")
    result = cur.fetchall()
    print(result)
if a == 'insert':
    cur.execute("CALL insert_to_phonebook('1', 'Duman','87774545505')")
if a == 'insertloop':
    cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['12', 'Ron', '87076052769'],
    ARRAY['13', 'Anjel', '87079815546'],
    ARRAY['14', 'Ch', '87074793780']
]);''')
if a == 'paginating':
    cur.execute(
        '''SELECT * FROM paginating(4, 2);'''
    )
    print(cur.fetchall())
if a == 'delete':
    cur.execute("CALL delete_from_phonebook('Leo Messi')")

conn.commit()
cur.close()
conn.close()
