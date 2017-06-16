import pymysql.cursors
# http://pymysql.readthedocs.io/en/latest/modules/cursors.html
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='zhulien_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    # single inserts
    with connection.cursor() as cursor:
        sql = "insert into orcs(clan, name, kills) values(%s, %s, %s)"
        cursor.execute(sql, ('Pythons', 'Pyfoon', 9))
        cursor.execute('insert into orcs(clan, name, kills) '
                       'values("Pythons", "Pythonizer", 10)')
    # insert many using sequence of sequences (tuples)
    with connection.cursor() as cursor:
        sql = "insert into orcs(clan, name, kills) values(%s, %s, %s)"
        data = (
            ('Pythons', 'Kuku', 10), 
            ('Pythons', 'Pipi', 11)
        )
        affected_rows = cursor.executemany(sql, data)
        print('executemany inserted', affected_rows, 'rows')
    # insert many using sequence of dictionaries
    with connection.cursor() as cursor:
        sql = "insert into orcs(clan, name, kills) values(%(a)s, %(b)s, %(c)s)"
        data = (
            {'a':'Pythons', 'b':'Ongo', 'c':1},
            {'a':'Pythons', 'b':'Bongo', 'c':2}
        )
        affected_rows = cursor.executemany(sql, data)
        print('executemany inserted', affected_rows, 'rows')
    connection.commit()
finally:
    connection.close()
    
# select id, clan, name, kills from orcs;
# delete from orcs where lower(clan) like '%python%';    