def numero(msg):
    ok=False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok =True
        else:
            try:
                if n != n.isnumeric():
                    ok = True
            except:
                print('erro')
            else:
                print("Dados não inseridos")
        if ok:
            break
    return valor

def linha2():
    print('-'*15)

def linhas():
    print('-'*30)


def titulo(msg):
    print("-"*15)
    print(f'{msg:>15}')
    print('-'*15)

def lista(list):
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c+=1
    linhas()
    opc = numero('Escolha a sua opção: ')
    linhas()
    return opc

def periculosidade(n):
    salario = n
    resp=" "
    while resp != "N":
        resp = str(input("PERICULOSIDADE[S/N] ")).strip().upper()[0]
        if resp in "S":
            salario += salario*0.3
        break
    return salario