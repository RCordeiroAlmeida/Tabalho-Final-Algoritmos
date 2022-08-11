#importação do banco
import sqlite3 as lite



#criando conexão
conn = lite.connect('nerdflix.sqlite') 

#inserindo dados
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO categoria (tipo) VALUES('filme')")
    cur.execute("INSERT INTO categoria (tipo) VALUES('serie')")
    cur.execute("INSERT INTO categoria (tipo) VALUES('documentario')")
    
caracProd1 = ['BREAKING BAD', 2, 10.99, 1]
with conn:
    cur = conn.cursor()
    query = ('INSERT INTO titulo (nome, tipo, preco, status) VALUES(?,?,?,?)')
    cur.execute(query, caracProd1)

caracProd2 = ['BETTER CALL SAUL', 2, 11.50, 1]
with conn:
    cur = conn.cursor()
    query = ('INSERT INTO titulo (nome, tipo, preco, status) VALUES(?,?,?,?)')
    cur.execute(query, caracProd2)

caracProd3 = ['EL CAMIÑO', 1, 7.75, 2]
with conn:
    cur = conn.cursor()
    query = ('INSERT INTO titulo (nome, tipo, preco, status) VALUES(?,?,?,?)')
    cur.execute(query, caracProd3)

