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
sql="UPDATE customers SET NOME=%s WHERE id=%s"
# cursor.execute(sql,("Joana",4))
#Update somente um registro
data=[("Charles",2),("Andre",3)]
cursor.executemany(sql,data)
connection.commit()

cursor.close()
connection.close()