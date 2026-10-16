def is_float(num):
    while True:
        num = num.strip()
        try:
            num = num.replace(',','.')
            num = float(num)
            return num
        except:
            print("Entrada invalida!")
            num = input("Digite novamente: ")

def is_int(num):
    num = num.strip()
    try:
        num = int(num)
        return num
    except:
        print("Entrada invalida!")
        num = input("Digite novamente: ")
        

def max_len(name, limit):
    while True:
        name = name.strip()
        if len(name) > limit:
            print()
            print(f"Entrada invalida! Limite {limit} caracteres.")
            name = input("Digite novamente: ")
        else:
            return name
            