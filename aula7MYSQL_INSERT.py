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
# cursor.execute(
#     'INSERT INTO customers '
#     '(nome,idade) VALUES ("LUIZ",25) '
# PlaceHolders em MySQL sao substituidos por %s

# sql='INSERT INTO customers (nome,idade) VALUES (%s,%s) '
# cursor.execute(sql,("ANA",25))
#Utilizando tuplas

# sql='INSERT INTO customers (nome,idade) VALUES (%(nome)s,%(idade)s) '
# data = {
#     "nome":"Joao",
#     "idade":31
# }
# cursor.execute(sql,data)
#Utilizando diccionarios em vez de tuplas ou listas

sql='INSERT INTO customers (nome,idade) VALUES (%(nome)s,%(idade)s) '
tupla=({'nome':'Fernando','idade':38},{'nome':'Chirlando','idade':50})
cursor.executemany(sql,tupla)

connection.commit()

cursor.close()
connection.close()