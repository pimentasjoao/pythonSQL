import sqlite3   #biblioteca para uso de SQLLite
from pathlib import Path  #biblioteca para uso de Diretorios em Python


ROOT_DIR = Path(__file__).parent    #comando para pegar o diretorio atual do arquivo
DB_NAME = 'db.sqlite3'   #nome do arquivo de bd a ser criado
DB_FILE = ROOT_DIR / DB_NAME   #diretorio completo do arquivo a ser criado utilizando /

conection=sqlite3.connect(DB_FILE)   #cria a conexão passando o diretorio
cursor = conection.cursor()   #abre o cursor

#SQL
TABLE_NAME='customers'

#cursor.execute(f'INSERT INTO {TABLE_NAME} (id,name,weight) VALUES (NULL,"Luiz Otavio",9.9)')  # Forma hardcoded
# cursor.execute(f'DELETE FROM {TABLE_NAME}')

# sql=f'INSERT INTO {TABLE_NAME} (name,weight) VALUES (?,?)'    #Melhor forma de fazer para evitar SQLInjection
# cursor.execute(sql,("JOANA",10))

sql=f'INSERT INTO {TABLE_NAME} (name,weight) VALUES (?,?)'   #Quando necessita fazer varios inserts uma de uma vez
cursor.executemany(sql,(("Ana",23),("Jose",20)))

conection.commit()

cursor.close()    #fecha o cursos
conection.close()   #fecha a conexao