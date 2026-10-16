from app.services import *
from app.ui import title

#Programa principal:

title("sistema controle-estoque",'~')

while True:
    mainMenu_option = mainMenu()

    try:
        if mainMenu_option == '1':
            createProduct()
        elif mainMenu_option == '2':
            readProduct()
        elif mainMenu_option == '3':
            uptadeProduct()
        elif mainMenu_option == '4':
            deleteProduct()
        else:
            if connection is not None and connection.is_connected(): #Fechando conexão ao fim do programa.
                connection.close()
            title("ATÉ LOGO!")
            break
    except Error as erro:
        if mainMenu_option != '2':
            connection.rollback()
        print(f"Falha na requisição!\nErro > {erro}")