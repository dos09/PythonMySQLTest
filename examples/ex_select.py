import pymysql.cursors
# http://pymysql.readthedocs.io/en/latest/modules/cursors.html
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='zhulien_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    print('print data using fetchone')
    with connection.cursor() as cursor:
        sql = "select id, clan, name, kills from orcs where kills = %s"
        affected_rows = cursor.execute(sql, (13))
        print('fetched', affected_rows, 'rows')
        while affected_rows > 0:
            affected_rows -= 1
            print(cursor.fetchone())
        # the cursor is exhausted, the below returns None
        print(cursor.fetchone())
        
    print('print data using fetchall')
    with connection.cursor() as cursor:
        sql = "select id, clan, name, kills from orcs where kills = %s"
        affected_rows = cursor.execute(sql, (13))
        print('fetched', affected_rows, 'rows')
        for doc in cursor.fetchall():
            print(doc)    
finally:
    connection.close()
