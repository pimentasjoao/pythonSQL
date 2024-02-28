import sqlite3   #biblioteca para uso de SQLLite
from pathlib import Path  #biblioteca para uso de Diretorios em Python


ROOT_DIR = Path(__file__).parent    #comando para pegar o diretorio atual do arquivo
DB_NAME = 'db.sqlite3'   #nome do arquivo de bd a ser criado
DB_FILE = ROOT_DIR / DB_NAME   #diretorio completo do arquivo a ser criado utilizando /

conection=sqlite3.connect(DB_FILE)   #cria a conexão passando o diretorio
cursor = conection.cursor()   #abre o cursor

#SQL
TABLE_NAME='customers'

cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
               '('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')'
)

conection.commit()

cursor.close()    #fecha o cursos
conection.close()   #fecha a conexao