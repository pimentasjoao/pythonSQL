import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent    #comando para pegar o diretorio atual do arquivo
DB_NAME = 'db.sqlite3'   #nome do arquivo de bd a ser criado
DB_FILE = ROOT_DIR / DB_NAME   #diretorio completo do arquivo a ser criado utilizando /

conection=sqlite3.connect(DB_FILE)   #cria a conexão passando o diretorio
cursor = conection.cursor()   #abre o cursor
TABLE_NAME='customers'
sql=f'SELECT * FROM {TABLE_NAME}'   #Quando necessita fazer varios inserts uma de uma vez
cursor.execute(sql)
# for row in cursor.fetchall():
#     _id, name, weight=row
#     print(_id,name,weight)
# fetchall utilizando quando necessita varios registros de uma vez

# row=cursor.fetchone()
# print(row)
#fetchone quando precisa buscar somente 1 registro

# for row in cursor.fetchmany(2):
#     print(row)
#fetchmany é usado quando vc quer somente determinada quantidade de resultados

cursor.close()    #fecha o cursos
conection.close()   #fecha a conexao