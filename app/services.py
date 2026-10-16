from time import sleep
from app.database import *
from app.ui import *
from app.validators import *

connection = connector()

products = [] #Lista com os produtos(dicionarios)

def mainMenu(): #Menu principal.
    """
        -> Mostra um menu com 5 opções.
    """
    print()
    title("MENU PRINCIPAL:")
    print("1 - Cadastrar produto\n2 - Listar produtos\n3 - Atualizar produto\n4 - Excluir produto\n5 - Sair")
    while True:
        mainMenu_option = (input("Digite sua opção: "))
        if mainMenu_option in ('1','2','3','4','5'):
            return mainMenu_option
        else:
            print("\nErro! Digite uma opção valida.\n")


def createProduct(): #Inserir novos produtos.
    cursor = connection.cursor() #Criar cursor.
    print()
    title("CADASTRO DE PRODUTOS")

    code = max_len(name = input("CÓDIGO(5 digitos): "), limit = 5)
    name = input("NOME: ")
    price = is_float(input("PREÇO: "))
    quant = input("ESTOQUE: ")
    param = (code,name,price,quant)
    sql = ("INSERT INTO estoque (codigo,nome,preco,quantidade) values (%s,%s,%s,%s)")

    cursor.execute(sql,param)
    connection.commit()

    cursor.close()

    print("\nProduto cadastrado com sucesso!")

def readProduct(): #Listar produtos.
    print()
    title("LISTANDO PRODUTOS")
    cursor = connection.cursor(dictionary = True) #Criar cursor.

    sql = ('SELECT * FROM estoque') #Variavel com comando SQL.

    cursor.execute(sql) #Executando o comando no banco de dados.

    estoque  = cursor.fetchall() #Recolhendo todos os dados do cursor.

    print(f"{'CÓDIGO':<7} {'NOME':<20} {'PREÇO':>8} {'ESTOQUE':>14}")
    print('-' * 53)

    for products in estoque:
        print(f"{products['codigo']:<7} {products['nome']:<20} {'R$':>5} {products['preco']:>6.2f} {products['quantidade']:>10}")
        sleep(0.4)

    cursor.close()
    

def uptadeProduct():
    print()
    title("atualizando produtos")
    if products:
        updateProduct_option = ''

        while True:
            search = input("\nDigite o ID do produto: ").upper()
            for product in products:
                if search == product['id']:
                    print(f"\nEncontrei {product['id']}!\n")
                    while True:
                        idProduct = input("Digite o novo ID: ").upper()
                        for i in products:
                            if idProduct == i['id'] and idProduct != product['id']:
                                print("Esse ID ja foi cadastrado! Tente novamente.\n")
                                break
                        else:
                            product['id'] = idProduct
                            break
                    product['name'] = input("Digite o novo nome: ").upper()
                    product['price'] = float(input("Digite o novo preço: R$"))
                    product['quant'] = int(input("Digite o novo estoque: "))
                    print("\nPRODUTO ATUALIZADO!\n")
                    print(f"ID: {product['id']}"),sleep(0.3)
                    print(f"NOME: {product['name']}"),sleep(0.3)
                    print(f"PREÇO: R${product['price']}"),sleep(0.3)
                    print(f"ESTOQUE: {product['quant']}")

                    while True:
                        updateProduct_option = input("\nDeseja continuar? [S/N] ").upper()
                        if updateProduct_option in ("S","N"):
                            break
                        else:
                            print("Opção invalida! Digite uma opção valida.")
                    break
            else:
                print("\nNão encontrei! Digite novamente\n")
            if updateProduct_option == 'N':
                break
    else:
        print("Nenhum produto cadastrado!")
        sleep(1)

def deleteProduct():
    deleteProducts_option = ''
    if products:
        while True:
            delete_IdProduct = input("Digite o ID do produto: ").upper()
            print()
            for i,product in enumerate(products):
                if delete_IdProduct == product['id']:
                    print("Produto encontrado! Excluindo...")
                    del products[i]
                    sleep(0.5)
                    print("Produto excluido!\n")
                    print(f"Lista atualizada:")
                    if products:
                        print(f"{"ID":<10}{"NOME":<12}{"PREÇO":<11}{"ESTOQUE":>5}")
                        print('-'*40)
                        for product in products:
                            sleep(0.5)
                            print(f"{product['id']:<10}{product['name']:<12}R${product['price']:<5}{product['quant']:>8}")

                        while True:
                            deleteProducts_option = input("\nDeseja continuar? [S/N] ").upper()
                            if deleteProducts_option in ('S', 'N'):
                                break
                            else:
                                print("Entrada invalida! Digite novamente.")
                        break
                    else:
                        print("Lista vazia!")
                        break
            else:
                print("Não encontrei! Tente novamente\n")

            if deleteProducts_option == 'N' or not products:
                break
    else:
        print("Nenhum produto cadastrado!")
        sleep(1)
