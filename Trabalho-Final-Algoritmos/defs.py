import sqlite3 as lite
import time
import os
import datetime

conn = lite.connect('nerdflix.sqlite') 

#limpa o terminal ao final de cada execução
def clearTerminal():
    os.system('cls') or None
#reinicia o menu ao final de cada execução
def restartMenu():
    restart = int(input('''Deseja realizar um novo processo?\n[1] - Sim\n[2] - Não\n'''))
    while restart not in range(1, 3):
        restart = int(input('''Deseja realizar um novo processo?\n[1] - Sim\n[2] - Não\n'''))
    if restart == 2:
        print('Encerrando...')
        time.sleep(2)
        exit()
    clearTerminal()
    menu()  

#Apresenta o menu de opções
def menu():
    while True:
        try:
            print(f'O que você gostaria de fazer?')
            esc = int(input('''[1] - Cadastrar novo produto
[2] - Buscar produto
[3] - Editar produto
[4] - Relatório de produtos
[5] - Registro de compras
[6] - Relatório de vendas
[7] - Sair\n'''))

            if not(1 <= esc <= 7):
                raise ValueError      

            if esc == 1:
                clearTerminal()
                cadastro()
            elif esc == 2:
                clearTerminal()
                response = busca()
                print(response)
            elif esc == 3:
                clearTerminal()
                response = editar()
                print(response)
            elif esc == 4:
                clearTerminal()
                response = relatorio()
            elif esc == 5:
                clearTerminal()
                regComp()
            elif esc == 6:
                clearTerminal()
                printCompras()          
            elif esc == 7:
                clearTerminal()
                verif  = int(input('''Tem certeza que deseja sair?
        [1] - Sim
        [2] - Não\n
        '''))
                if verif ==1:
                    clearTerminal()
                    print('Encerrando...')
                    time.sleep(2)
                    exit()
        except ValueError:
            clearTerminal()
            print('Valor inválido')
#Realiza o cadastro dos titulos
def cadastro():
    caracProd = []
    nome = input('Digite o nome do produto: \n')        
    nome = nome.upper()
    
    tipo = int(input('Digite a categoria do produto\n[1] - Filmes\n[2] - Séries\n[3] - Documentários\n'))
    while tipo not in range(1, 4):
        clearTerminal()
        tipo = int(input('Digite a categoria do produto\n[1] - Filmes\n[2] - Séries\n[3] - Documentários\n'))

    preco = float(input('Digite o preço do produto:\n'))
    while preco < 0:
        preco = float(input('Digite o preço do produto:\n'))
        
    status = int(input('O produto está disponível para venda?\n[1] - Sim\n[2] - Não\n'))
    while status != 1 and status != 2:
        status = int(input('O produto está disponível para venda?\n[1] - Sim\n[2] - Não\n'))


    caracProd.extend((nome, tipo, preco, status))
    clearTerminal()
    print(f'''NOME: {caracProd[0]} | CATEGORIA: {buscarCateg(tipo)} | STATUS: {"disponível" if caracProd[3] == 1 else "indisponível"} | PREÇO: R${caracProd[2]} |''')
    res = int(input('''Tem certeza que deseja inserir esses dados ao banco?
[1] - Sim
[2] - Não\n'''))
    while res != 1 and res != 2:
        res = int(input('''Tem certeza que deseja inserir esses dados ao banco?
[1] - Sim
[2] - Não\n'''))
    clearTerminal()
    if res == 1:
        
        try:
            with conn:
                cur = conn.cursor()
                query = ('''INSERT INTO titulo (nome, tipo, preco, status) VALUES(?,?,?,?)''')
                cur.execute(query, caracProd)
                cur.execute('PRAGMA table_info(categoria)')
                payload = (f'''NOME: {caracProd[0]} | CATEGORIA: {buscarCateg(tipo)} | STATUS: {"disponível" if caracProd[3] == 1 else "indisponível"} | PREÇO: R${caracProd[2]} |''')
                idTitulo =  cur.execute('''SELECT MAX(id) FROM titulo''')
                print('Titulo cadastrado com sucesso!')
                print(f'{payload}  CÓDIGO: {idTitulo.fetchone()[0]}')
        except:
            print('Dados não cadastrados')
        restartMenu()

    else:
        menu()

#Faz com que a resposta à categoria seja apresentada como string e não como 1,2 ou 3
def buscarCateg(tipo):
    with conn:
        cur = conn.cursor()
        cur.execute('PRAGMA table_info(categoria)')
        response = cur.execute('''SELECT tipo FROM categoria WHERE id = {}'''.format(tipo))
        return response.fetchone()[0]

#Realiza a busca de acordo com o ID digitado pelo usuário
def busca():
    buscaId = int(input('Insira o código do objeto a ser buscado:\n'))

    try:
        with conn:
            cur = conn.cursor()
            cur.execute('PRAGMA table_info(titulo)')
            query = cur.execute('SELECT * FROM titulo WHERE id = {}'.format(buscaId))
            result = query.fetchone()
            
            if result == None:
                clearTerminal()
                print('Não foi possível encontrar prdutos com o código: {}'.format(buscaId))
                time.sleep(1.5)
                busca()

            if len(result) == 0:
                print('Não foi possível encontrar prdutos com o código: {}'.format(buscaId))
                time.sleep(1.5)
                menu()
            
            clearTerminal()
            return print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
            
    except:
        print('Não foi possível encontrar prdutos com o código: {}'.format(buscaId))
    clearTerminal()

#Edita os dados dos titulos cadastrados
def editar():

    buscaId = int(input('Insira o código do produto a ser editado:\n'))
    clearTerminal()
    
    with conn:
        cur = conn.cursor()
        result = cur.execute('SELECT * FROM titulo WHERE id ={}'.format(buscaId))
        result = cur.fetchone()
        if result == None:
            print('Não foi possível encontrar prdutos com o código: {}'.format(buscaId))
            time.sleep(1.5)
            editar()
        
        print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
        print()



    escEdit = int(input('''O que você gostaria de editar?\n
[1] - Nome do produto
[2] - Categoria do produto
[3] - Preço do produto
[4] - Status do produto\n'''))
    
    if escEdit == 1:
        newName = input('Insira o novo nome do produto\n')
        newName = newName.upper()

        with conn:
            cur = conn.cursor()
            cur.execute('PRAGMA table_info(titulo)')
            query = ("UPDATE titulo SET nome = '{}' WHERE id = {}".format(newName, buscaId))
            cur.execute(query)
            
            result = cur.execute('SELECT * FROM titulo')
            clearTerminal()
            result = cur.fetchone()
            
            clearTerminal()
            print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
            print()
             
            


    elif escEdit == 2:
        newTipo = int(input('''Escolha a nova categoria do produto\n
[1] - Filmes\n
[2] - Séries\n
[3] - Documentários\n'''))

        with conn:
            cur = conn.cursor()
            cur.execute('PRAGMA table_info(titulo)')
            query = ("UPDATE titulo SET tipo = {} WHERE id = {}".format(newTipo, buscaId))
            cur.execute(query)

            print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
            print()
            clearTerminal()  
            
    elif escEdit == 3:
        newPreco = float(input('Digite o  novo preço do produto:\n'))

        with conn:
            cur = conn.cursor()
            cur.execute('PRAGMA table_info(titulo)')
            query = ("UPDATE titulo SET tipo = {} WHERE id = {}".format(newPreco, buscaId))
            cur.execute(query)

            print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
            print()
            clearTerminal()  

    elif escEdit == 4:
        newStatus = int(input('Novo status do produto'))

        with conn:
            cur = conn.cursor()
            cur.execute('PRAGMA table_info(titulo)')
            query = ("UPDATE titulo SET tipo = {} WHERE id = {}".format(newStatus, buscaId))
            cur.execute(query)

            print(f'''NOME: {result[1]} | CATEGORIA: {buscarCateg(result[2])} | STATUS: {"disponível" if result[4] == 1 else "indisponível"} | PREÇO: R${result[3]} | CÓDIGO: {result[0]} |''')
            print()
            clearTerminal()  

#Imprime os dados do titulo de acordo com o filtro selecionado
def relatorio():

    while True:
        print('''Aqui você pode visualizar todos os produtos cadastrados de acordo com os seguintes filtros:\n
[1] - Visualizar todos os produtos
[2] - Apenas filmes
[3] - Apenas series
[4] - Apenas documentarios
[5] - Apenas disponiveis para venda
[6] - Apenas indisponiveis
[7] - Voltar\n''')
    
        escFiltro = int(input('O que deseja visualizar?\n'))
        clearTerminal()

        if escFiltro == 1:
            
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo ORDER BY nome')
                    response = cur.fetchall()
                    
                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except:
                print('Não foi possível buscar titulos no filtro atual')
                time.sleep(2)
            restartMenu()
        

        elif escFiltro == 2:
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo WHERE tipo = 1 ORDER BY nome')
                    response = cur.fetchall()
                    
                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except:
                print('Não foi possível buscar titulos no filtro atual')
            restartMenu()

        elif escFiltro == 3:
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo WHERE tipo = 2 ORDER BY nome')
                    response = cur.fetchall()
                    
                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except:
                print('Não foi possível buscar titulos no filtro atual')
            restartMenu()
        
        elif escFiltro == 4:
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo WHERE tipo = 3 ORDER BY nome')
                    response = cur.fetchall()

                    if len(response) == 0:
                        raise ValueError('Não foi possível buscar titulos no filtro atual')

                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except ValueError as message:
                print(message)
            restartMenu()
                
        
        elif escFiltro == 5:
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo WHERE status = 1 ORDER BY nome')
                    response = cur.fetchall()

                    if len(response) == 0:
                        raise ValueError('Não foi possível buscar titulos no filtro atual')

                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except ValueError as message:
                print(message)
            restartMenu()
                

        elif escFiltro ==  6:
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute('PRAGMA table_info(titulo)')
                    response = cur.execute('SELECT * FROM titulo WHERE status = 2 ORDER BY nome')
                    response = cur.fetchall()

                    if len(response) == 0:
                        raise ValueError('Não foi possível buscar titulos no filtro atual')

                    clearTerminal()
                    for i in response:
                        print(f'''NOME: {i[1]} | CATEGORIA: {buscarCateg(i[2])} | STATUS: {"disponível" if i[4] == 1 else "indisponível"} | PREÇO: R${i[3]} | CÓDIGO: {i[0]} |''')
                        print()
            except ValueError as message:
                print(message)
            restartMenu()
                

        elif escFiltro == 7:
            menu()

#Realiza uma nova compra no nome de um cliente 
def regComp():
    data = format(datetime.date.today(), '%d/%m/%Y')
    cliente = input('Nome do comprador:\n')
    cliente = cliente.upper()
    carrinho = []
    precoFinal = []
    while True:  
        item = int(input('\nInsira o código do item desejado pelo comprador\nPara cancelar: código 0\nPara finalizar as compras: código -1\n'))

        if item > 0:
            with conn:
                cur = conn.cursor()
                cur.execute('PRAGMA table_info(titulo)')
                response = cur.execute('''SELECT id, nome, tipo, preco, status FROM titulo WHERE id = {}'''.format(item))
                response = response.fetchall()
                
                if len(response) == 0:
                    clearTerminal()
                    print(f'Não foram encontrados títulos com o código: {item}\n')
                    break
                
                for l in response:
                    if l[4] == 2:
                        clearTerminal()
                        print(f'''CÓDIGO: {l[0]} | NOME: {l[1]} | TIPO: {buscarCateg(l[2])} | PREÇO: {l[3]}''')
                        print('Você não pode vender este produto pois ele se encontra indisponível')
                        regComp()
                        
                else:
                    for i in response:
                        print(f'''CÓDIGO: {i[0]} | NOME: {i[1]} | TIPO: {buscarCateg(i[2])} | PREÇO: {i[3]}''')

                verif = int(input('''Deseja adicionar esse titulo ao carrinho?
[1] - sim
[2] - não\n'''))
                
                if verif == 2:
                    continue
                elif verif == 1:
                    for i in response:
                        carrinho.append(i)
                        counter = 1
                        clearTerminal()
                        print('ITENS DO CARRINHO:')
                        for item in carrinho:
                            print(f'{counter} - {item[1]}')
                            counter +=1
                                                
                        for row in response:
                            precoFinal.append(row[3])

        elif item == -1:
            if len(precoFinal) == 0:
                clearTerminal()
                print(f'Não existem itens no carrinho de compras\n')                        
                break
            else:
                clearTerminal()
                result = sum(precoFinal)  
                
                while True:
                    finaliza = int(input(f'''Valor da compra: R${result:.2f}\nDeseja continuar?\n[1] - Sim\n[2] - Não\n'''))
                    if finaliza != 1 and finaliza != 2:
                        continue

                    if finaliza == 2:
                        clearTerminal()
                        print('Compra cancelada\nVocê será redirecionado ao menu principal')
                        time.sleep(1.5)
                        menu()

                    if finaliza == 1: 
                        print('''Compra finalizada com sucesso!''')
                        with conn:
                            cur = conn.cursor()
                            cur.execute('PRAGMA table_info(compras)')
                            

                            insert = [cliente, data, result]
                            response = ('''INSERT INTO compras (comprador, data, valor) VALUES (?, ?, ?)''')
                            cur.execute(response, insert)
                            
                            query = cur.execute('''SELECT * FROM compras''')
                            query = query.fetchall()
                            
                            clearTerminal()
                            print('DADOS DA COMPRA')
                            for i in carrinho:
                                print(f'PRODUTO: {i[1]} | PREÇO: R${i[3]:.2f}')
                            print(f'TOTAL: R${result:.2f}')
                            break
                   
        else:
            clearTerminal()
            menu()

def printCompras():
    with conn:
        cur = conn.cursor()
        cur.execute('PRAGMA table_info(compras)')
        response = cur.execute('''SELECT * FROM compras''')
        result = response.fetchall()
        
        clearTerminal()
        print('''RELATÓRIO DE VENDAS''')
        if result == []:
            print('Não foram realizadas vendas ainda')
            restartMenu()

        for i in result:
            print(f'|COMPRADOR: {i[1]} | TOTAL DA VENDA: R$ {i[3]:.2f} | DATA DA VENDA: {i[2]}')
        restartMenu()