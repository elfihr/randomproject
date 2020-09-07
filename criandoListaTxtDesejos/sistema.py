from criandoListaTxtDesejos.interface.produto import *
from criandoListaTxtDesejos.interface.efeito import *

arq = 'Lista_de_desejo.txt'

if not existeArqu(arq):
    criarArquivo(arq)

while True:
    linha2()
    choice = lista(['Ler Lista de Desejos',"Adicionar item a Lista de desejos",'Fechar programa'])
    if choice == 1:
        titulo('---Ler Lista de Aqruivos---')
        lerArqui(arq)
    elif choice == 2:
        titulo('---Adicionar item a Lista---')
        produto = str(input('Digite o produto: '))
        preco = testInt("Digite o preço: ")
        desconto = testInt("Qual o percentual do desconto[%]: ")
        precDesconto = preco-(preco*(desconto/100))
        escrever(arq, produto,preco,desconto,precDesconto)
    elif choice == 3:
        titulo('---Fechando Programa---')
        break
    else:
        print('Digite uma opção valida')
    sleep(1)


print('FIM DO PROGRAMA')



