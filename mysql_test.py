import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='zhulien_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = ''
        cursor.execute(sql)
        for doc in cursor.fetchall():
            print(doc)
finally:
    connection.close()
