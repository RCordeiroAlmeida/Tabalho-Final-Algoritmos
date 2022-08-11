# Tabalho-Final-Algoritmos
Este é o trabalho final do CCR - Algorítmos e programação da 1° Fase - Ciência da Computação - UFFS

Sistema NerdFlix

Você foi contratado(a) para trabalhar na startup NerdFlix, uma empresa que disponibiliza produtos (filmes, séries e documentários) por meio de stream. A empresa possui um sistema Web onde o cliente se cadastra, adquire produtos e realiza pagamentos.

Você foi incumbido de administrar os dados no backoffice da empresa, isto é, num sistema interno. Como ainda não cursou a disciplina de BD na UFFS, você ainda não sabe como integrar os dados entre os dois sistemas. Desta forma, você decidiu criar outro sistema em Python onde os funcionários da NerdFlix irão digitar novamente todas as compras realizadas pelos pelos clientes no sistema Web.

Nas próximas seções são descritas as informações necessárias para a implementação do sistema.
Objetivo

O objetivo de seu programa é possibilitar que o usuário (funcionário da empresa) cadastre os produtos e também registre as compras feitas pelos clientes.

Neste momento, o sistema não terá um cadastro de clientes completo. Assim, cada compra será vinculada apenas ao login do cliente.

Abaixo, são detalhadas as opções que devem estar presentes no menu principal:

 
1 - Cadastrar produtos

O usuário do sistema poderá criar um novo produto informando os seguintes dados cadastrais:

    Código do produto: código numérico do produto;
    Nome: nome do produto;
    Tipo: 1 para série, 2 para filme, 3 para documentário;
    Preço: valor de venda do produto;
    Disponível para venda: valor booleano que indica se o produto pode (True) ou não (False) ser vendido neste momento.

2 - Consultar produto

Permite buscar os dados de um determinado produto pelo seu código. Caso o produto não exista, exibir a mensagem Produto não cadastrado.
3 - Atualizar produtos

Permite que dados de um determinado produto sejam atualizados. Como o código identifica um produto, este não pode ser alterado.
4 - Relatório de produtos

Ao acessar esta opção, o sistema deve perguntar o que o usuário de seja visualizar: todos os produtos (opção 0), somente filmes (opção 1), séries (opção 2), documentários (opção 3), todos os produtos disponíveis para venda (opção 4) ou todos os produtos indisponíveis (opção 5).

Em seguida, exibir a lista de produtos, filtrados conforme opção descrita acima. Devem ser exibidas as colunas código, nome, tipo e preço. A lista deve vir ordenada pelo nome do produto. O tipo deve ser exibido com sua descrição textual (embora armazenado na forma de número).

    DICA: você pode adicionar um conjunto de 10 produtos predefinidos diretamente no código-fonte, a fim de facilitar os testes da aplicação.

5 - Registrar compra

Para registrar uma compra, primeiramente é necessário informar o login do cliente (string). O sistema também deve gerar automaticamente a data da compra e armazená-la. Em seguida, deve ser informado o código de cada produto (após a digitação, deverá ser apresentado o nome do produto para que o usuário se certifique de que digitou o código correto). Se for informado o código de um produto não disponível para venda, o sistema deve reportar um erro e impedir a inserção do mesmo no registro da compra. Deverá existir uma forma de encerrar o registro da compra (dica: pode ser o código -1 , por exemplo). A forma de pagamento não será controlada. Ao final, o sistema deverá apresentar um tipo de cupom fiscal. Ex.:
Código 	Nome 	Tipo 	Preço
12 	Item 1 	Filme 	9,90
4 	Item 2 	Série 	18,70
78 	Item 3 	Filme 	13,90
		        Total 	42,50
6 - Relatório de compras

Mostrar uma lista com todas as compras, contendo: data (dd/mm/aaaa), login do cliente e valor total.
