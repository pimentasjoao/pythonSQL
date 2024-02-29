import pymysql
import dotenv

ENV=dotenv.dotenv_values()

connection= pymysql.connect(
    host=ENV['MYSQL_HOST'],
    user=ENV['MYSQL_USER'],
    password=ENV['MYSQL_PASSWORD'],
    database=ENV['MYSQL_DATABASE'],
    charset='utf8mb4'
)
cursor=connection.cursor()
sql="SELECT * FROM customers"
cursor.execute(sql)
for row in cursor.fetchall():
    _id, nome, idade=row
    print(_id, nome, idade)

connection.commit()

cursor.close()
connection.close()