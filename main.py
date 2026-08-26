print("="*30)
print("controle estoque".center(30).upper())
print("="*30)
print("""1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
5 - Sair""")

name = ''
price = 0
quant = 0
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
        name = (input("\nNome do produto: ").upper())
        price = (float(input("Preço do produto: R$")))
        quant = (int(input("Estoque do produto: ")))
        idProduct = (input("ID do produto: "))

        product.append([name, price, quant,idProduct])
        
        while True:
            newProduct_option = input("\nDeseja continuar? [S/N] ").upper()
            if newProduct_option in ("S","N"):
                break
            else:
                print("Opção invalida! Digite uma opção valida.")
        if newProduct_option == 'N':
            break

    print(product)
