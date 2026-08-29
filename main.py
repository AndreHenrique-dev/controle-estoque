from time import sleep

print("="*30)
print("controle estoque".center(30).upper())
print("="*30)
print("""1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
5 - Sair""")

products = list()

while True:
    mainMenu_option = (input("Digite sua opção: "))
    if mainMenu_option in "12345":
        break
    else:
        print("Erro! Digite uma opção valida.")
    print()

if mainMenu_option == '1': #Cadastrar novo produto
    print()
    print("="*40)
    print("CADASTRO PRODUTOS".center(40))
    print("="*40)
    while True:
        while True:
            idProduct = (input("\nID do produto: ")).upper()
            for product in products:
                if idProduct == product[0]:
                    print("Esse ID ja foi cadastrado! Tente novamente.")
                    break
            else:
                break
        name = (input("Nome do produto: ").upper())
        price = (float(input("Preço do produto: R$")))
        quant = (int(input("Estoque do produto: ")))

        products.append([idProduct, name, price, quant])

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

    print("="*30)
    print("controle estoque".center(30).upper())
    print("="*30)
    print("""
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Atualizar produto
    4 - Excluir produto
    5 - Sair""")
    while True:
        mainMenu_option = (input("Digite sua opção: "))
        if mainMenu_option in "12345":
            break
        else:
            print("Erro! Digite uma opção valida.")
    print()

if mainMenu_option == '2':
    if products:
        print("="*40)
        print(f"{"LISTAGEM DE PRODUTOS":^40}")
        print("="*40)
        print(f"{"ID":<10}{"NOME":<12}{"PREÇO":<11}{"ESTOQUE":>5}")
        print('-'*40)
        for product in products:
            sleep(0.5)
            print(f"{product[0]:<10}{product[1]:<12}R${product[2]:<5}{product[3]:>8}")
    else:
        print("Nenhum produto cadastrado.")

if mainMenu_option == '3':
    print('='*40)
    print(f"{"ATUALIZAR PRODUTOS":^40}")
    print('='*40)


    while True:
        search = input("\nDigite o ID do produto: ").upper()
        for product in products:
            if search == product[0]:
                print(f"\nEncontrei {product[0]}!\n")
                while True:
                    idProduct = input("Digite o novo ID: ").upper()
                    for i in products:
                        if idProduct == i[0] and idProduct != product[0]:
                            print("Esse ID ja foi cadastrado! Tente novamente.\n")
                            break
                    else:
                        product[0] = idProduct
                        break
                product[1] = input("Digite o novo nome: ").upper()
                product[2] = float(input("Digite o novo preço: R$"))
                product[3] = int(input("Digite o novo estoque: "))
                print("\nPRODUTO ATUALIZADO!\n")
                print(f"ID: {product[0]}"),sleep(0.5)
                print(f"NOME: {product[1]}"),sleep(0.5)
                print(f"PREÇO: R${product[2]}"),sleep(0.5)
                print(f"ESTOQUE: {product[3]}")

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