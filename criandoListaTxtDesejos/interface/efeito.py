
def linhas():
    print('-'*30)

def linha2():
    print('-='*15)

def titulo(msg):
    print("-"*15)
    print(f'{msg:>15}')
    print('-'*15)

def testInt(item):
    while True:
        try:
            n = int(input(item))
        except Exception as erro:
            print(f'{erro.__class__}')
        except:
            return 0
        else:
            return n

def lista(list):
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c+=1
    linhas()
    opc = testInt('Escolha a sua opção: ')
    linhas()
    return opc

