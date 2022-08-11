#importação do banco
import sqlite3 as lite

#criando conexão
conn = lite.connect('nerdflix.sqlite') 

####################################################criando tabelas######################################################

#CATEGORIA
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE categoria(id INTEGER, tipo INT, PRIMARY KEY('id' AUTOINCREMENT) )")
#TÍTULO
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE titulo(id INTEGER, nome TEXT, tipo INTEGER, preco DOUBLE, status INT, PRIMARY KEY('id' AUTOINCREMENT), FOREIGN KEY('tipo') REFERENCES 'categoria' ('id') ON DELETE CASCADE)")
#COMPRAS
with conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE compras(id INTEGER, comprador TEXT, data DATE, valor DOUBLE, PRIMARY KEY('id' AUTOINCREMENT), FOREIGN KEY ('id') REFERENCES 'titulo' ('id') ON DELETE CASCADE)''')

