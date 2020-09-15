from projetos.folhaDePag.library.calculadora import *

tothoraExtra = valorLiquidoFolha = dsr = comissao = dependente = horaExtra= insal = dia = nuteis = irrf = fgts = valeTot1 = adiantamento = 0
salario = float(input("SALARIO: "))

#Periculosidade
resp=" "
while resp != "N":
    resp = str(input("PERICULOSIDADE[S/N] ")).strip().upper()[0]
    if resp in "S":
        salario += salario*0.3
    break

#Insalubridade
resp = " "
while resp != "N":
    resp = str(input("Insalubre?[S/N] ")).strip().upper()[0]
    if resp in "S":
        perc = float(input("Qual o percentual de adicional[ate40%]: "))
        insal = (salario*perc)/100
        salario += insal
        perc = 0
    break

#Ferias
resp=" "
while resp != "N":
    resp = str(input("FERIAS?[S/N] ")).strip().upper()[0]
    if resp in "S":
        salario += salario/3
    break

dia = numero("Dias Uteis")
nuteis = numero('Dias não Uteis')

#Vale Transporte
while resp != "N":
    resp = str(input("Tem vale transporte?[S/N] ")).strip().upper()[0]
    if resp in "S":
        valeT = float(input("qual valor do vale transporte: "))
        passD = int(input('Quantas passagens por dia?'))
        vt1 = valeT*passD*dia
        vt2 = salario*0.06
        if vt1 <= vt2:
            valeTot1 = vt1
        else:
            valeTot1 = vt2
    break

#Comissao
resp = " "
while resp != "N":
    resp = str(input("COMISSÃO?[S/N] ")).strip().upper()[0]
    if resp in "S":
        comissao = float(input('COMISSÃO: '))
        perc = 0
    break

salarioHora = salario/220
salarioMinuto = salario/13200

#Hora Extra
resp=" "
while resp != "N":
    resp = str(input("Tem hora extra?[S/N] ")).strip().upper()[0]
    if resp in "S":
        horaExtra = float(input("HORA EXTRA[Apenas Hora] ")) * 60
        horaExtra += float(input("HORA EXTRA[Apenas minuto] "))
        por = float(input('Qual o percentual da hora extra[150% a 200%]'))
        tothoraExtra = salarioMinuto*(por/100)*(horaExtra)
    break

#Adiantamento
resp = " "
while resp != "N":
    resp = str(input("Tem adiantamento?[S/N] ")).strip().upper()[0]
    if resp in "S":
        perc = float(input("Qual o percentual[ate50%]: "))
        adiantamento = (salario*perc)/100
    break

#Dependente
resp = " "
while resp != "N":
    resp = str(input("Tem Dependente?[S/N] ")).strip().upper()[0]
    if resp in "S":
        dep = int(input("quantos: "))
        dependente = dep*189.59
    else:
        dependente = 0
    break

#Descanso Remunerado
if comissao > 0 or tothoraExtra > 0:
    dsr = ((tothoraExtra+comissao)/dia) * nuteis
else:
    dsr = 0

#SalarioBruto
salarioBruto = salario+tothoraExtra+dsr+comissao

#INSS
if salarioBruto <= 1045:
    inss = salario*0.075
elif salarioBruto > 1045.0 and salarioBruto <= 2089.60:
    inss = (salarioBruto-1045)*0.09+78.37
elif salarioBruto > 2089.6 and salarioBruto <= 3134.4:
    inss = (salarioBruto - 2089.6)*0.12+172.38
else:
    inss = (salarioBruto - 3134.4)*0.14+297.75

#IRRF
irrf1 = (salarioBruto - inss - dependente)
if irrf1 <= 1903.98:
    print('Isento')
elif irrf1 >1903.99 and irrf1 <= 2826.65:
    irrf = irrf1 * 0.075 - 142.8
elif irrf1 > 2826.66 and irrf1 <= 3751.05:
    irrf = irrf1 * 0.15 - 354.8
elif irrf1 > 3751.06 and irrf1 < 4664.68:
    irrf = irrf1 * 0.225 - 636.13
elif irrf1 > 4664.68:
    irrf = irrf1 * 0.275 - 869.36

#FGTS
fgts = salarioBruto * 0.08

#Descontos
desconto = adiantamento+inss+valeTot1+irrf
valorLiquidoFolha = salarioBruto-desconto

if salarioBruto <= 1425.56:
    valorLiquidoFolha += 48.62

print(f"REMUNERAÇÃO: R${salarioBruto:.2f}\nCOMISSÃO: R${comissao:.2f}\nHORA EXTRA: {horaExtra}minutos\n"
      f"Adiantamento: R${adiantamento}\nInsalubridade: R${insal}\nDSR(descansoRem): R${dsr:.2f}"
      f"\nGanho Hora extra: R${tothoraExtra:.2f}\nValor da passagem: R${valeTot1}\n\nINSS: R${inss:.2f}"
      f"\nIRRF: R${irrf:.2f}\nVALOR LIQUIDO DA FOLHA: {valorLiquidoFolha:.2f}\nFGTS: R${fgts:.2f}")