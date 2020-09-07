from time import sleep

def existeArqu(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro')
    else:
        print(f'Criando {nome}...')
        sleep(1)
    finally:
        print(f'{nome} criado com sucesso')

def escrever(arq,produto ='desconhecido',preco=0,desconto = 0,precDescont = 0):
    try:
        a = open(arq,"at")
    except:
        print('Houve um erro ')
    else:
        try:
            a.write(f'PRODUTO: {produto} - PREÇO R${preco} - DESCONTO {desconto}% - PREÇO A VISTA R${precDescont}\n')
        except:
            print('Error')
        else:
            print('Adicionando produto...')
            sleep(1)
            a.close()

def lerArqui(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Arquivo não encontrado ou não existe')
    else:
        print(a.read())
        a.close()
        sleep(1)





