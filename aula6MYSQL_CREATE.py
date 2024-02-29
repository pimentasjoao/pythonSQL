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
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
)
connection.commit()

cursor.close()
connection.close()