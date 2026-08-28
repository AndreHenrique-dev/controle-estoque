from time import sleep

print("="*30)
print("controle estoque".center(30).upper())
print("="*30)
print("""1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
5 - Sair""")

product = list()

while True:
    mainMenu_option = (input("Digite sua opção: "))
    if mainMenu_option in "12345":
        break
    else:
        print("Erro! Digite uma opção valida.")

if mainMenu_option == '1': #Cadastrar novo produto
    print()
    print("="*40)
    print("CADASTRO PRODUTOS".center(40))
    print("="*40)
    while True:
        while True:
            idProduct = (input("\nID do produto: ")).upper()
            for i in product:
                if idProduct == i[0]:
                    print("Esse ID ja foi cadastrado! Tente novamente.")
                    break
            else:
                break
        name = (input("Nome do produto: ").upper())
        price = (float(input("Preço do produto: R$")))
        quant = (int(input("Estoque do produto: ")))

        product.append([idProduct, name, price, quant])

        print("\nPRODUTO CADASTRADO COM SUCESSO!\n")
        print(f"ID: {idProduct}"),sleep(0.5)
        print(f"NOME: {name}"),sleep(0.5)
        print(f"PREÇO: R${price}"),sleep(0.5)
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
   

if mainMenu_option == '3':
    print()
    print('='*40)
    print(f"{"ATUALIZAR PRODUTOS":^40}")
    print('='*40)


    while True:
        search = input("\nDigite o ID do produto: ").upper()
        for p in product:
            if search == p[0]:
                print(f"\nEncontrei {p[0]}!\n")
                while True:
                    idProduct = input("Digite o novo ID: ").upper()
                    for i in product:
                        if idProduct == i[0] and idProduct != p[0]:
                            print("Esse ID ja foi cadastrado! Tente novamente.\n")
                            break
                    else:
                        p[0] = idProduct
                        break
                p[1] = input("Digite o novo nome: ").upper()
                p[2] = float(input("Digite o novo preço: R$"))
                p[3] = int(input("Digite o novo estoque: "))
                print("\nPRODUTO ATUALIZADO!\n")
                print(f"ID: {p[0]}"),sleep(0.5)
                print(f"NOME: {p[1]}"),sleep(0.5)
                print(f"PREÇO: R${p[2]}"),sleep(0.5)
                print(f"ESTOQUE: {p[3]}")

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