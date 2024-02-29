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
sql="DELETE FROM customers WHERE id=%s"
cursor.execute(sql,1)

connection.commit()

cursor.close()
connection.close()