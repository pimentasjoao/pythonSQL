import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent    #comando para pegar o diretorio atual do arquivo
DB_NAME = 'db.sqlite3'   #nome do arquivo de bd a ser criado
DB_FILE = ROOT_DIR / DB_NAME   #diretorio completo do arquivo a ser criado utilizando /

conection=sqlite3.connect(DB_FILE)   #cria a conexão passando o diretorio
cursor = conection.cursor()   #abre o cursor
TABLE_NAME='customers'
sql=f'DELETE FROM {TABLE_NAME} WHERE NAME = "Jose"'   
cursor.execute(sql)
conection.commit()

cursor.close()    #fecha o cursos
conection.close()   #fecha a conexao