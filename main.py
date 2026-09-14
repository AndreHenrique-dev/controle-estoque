from time import sleep
def title(txt = '',line = '='):
    """
        -> Escreve um titulo centralizado entre duas linhas.
    Parâmetros:
        txt (string, opicional): Define o conteudo do titulo. Definido por padrão como: ''
        line (string, opicional): Define o conteudo(simbolo) da linha. Definido por padrão como '='.
    """
    print(line*(len(txt)+6))
    print(txt.center(len(txt)+6).upper())
    print(line*(len(txt)+6))

def mainMenu():
    """
        -> Mostra um menu com 5 opções.
    """
    print()
    global mainMenu_option
    title("MENU PRINCIPAL:")
    print("1 - Cadastrar produto\n2 - Listar produtos\n3 - Atualizar produto\n4 - Excluir produto\n5 - Sair")
    while True:
        mainMenu_option = (input("Digite sua opção: "))
        if mainMenu_option in "12345":
            break
        else:
            print("\nErro! Digite uma opção valida.\n")
    print()

def createProduct():
    print()
    title("CADASTRO DE PRODUTOS")
    while True:
        while True:
            idProduct = (input("\nID do produto: ")).upper()
            for product in products:
                if idProduct == product["id"]:
                    print("Esse ID ja foi cadastrado! Tente novamente.")
                    break
            else:
                break
        name = (input("Nome do produto: ").upper())
        price = (float(input("Preço do produto: R$")))
        quant = (int(input("Estoque do produto: ")))

        products.append({"id": idProduct,
                        "name" : name,
                        "price": price,
                        "quant" : quant})

        print("\nPRODUTO CADASTRADO COM SUCESSO!\n")
        print(f"ID: {idProduct}"),sleep(0.3)
        print(f"NOME: {name}"),sleep(0.3)
        print(f"PREÇO: R${price}"),sleep(0.3)
        print(f"ESTOQUE: {quant}")

        while True:
            newProduct_option = input("\nDeseja continuar? [S/N] ").upper()
            if newProduct_option in ("S","N"):
                break
            else:
                print("Opção invalida! Digite uma opção valida.")
        if newProduct_option == 'N':
            break
    print()

def readProduct():
    print()
    if products:
        title("LISTAGEM DE PRODUTOS")
        print(f"{"ID":<10}{"NOME":<12}{"PREÇO":<11}{"ESTOQUE":>5}")
        print('-'*40)
        for product in products:
            sleep(0.5)
            print(f"{product['id']:<10}{product['name']:<12}R${product['price']:<5}{product['quant']:>8}")
    else:
        print("Nenhum produto cadastrado.")
        sleep(1)

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

#Programa principal:

products = [] #Lista com os produtos(dicionarios)

title("sistema controle-estoque",'~')

while True:
    mainMenu() #Chama o menu principal.

    if mainMenu_option == '1': #Se 
        createProduct()
    elif mainMenu_option == '2':
        readProduct()
    elif mainMenu_option == '3':
        uptadeProduct()
    elif mainMenu_option == '4':
        deleteProduct()
    else:
        title("ATÉ LOGO!")
        break


