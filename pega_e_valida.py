import variaveis_e_listas as dados
from tabelas import tabelaCores, tabelaModelos
import addcor
import re

## validando:

def validaModelo(modelo):
    erro = ""
    if modelo.isdigit() == True:
        if int(modelo) < 1 or int(modelo) > 4:
            erro = "Modelo errado. Digite o nº correspondente ao modelo desejado."
    else:
        erro = "Digite um valor numérico."
    return erro

def validaNumeracao(numeracao):
    erro = ""
    try:
        numeracao = int(numeracao)
        if numeracao < 22 or numeracao > 46:
            erro = "Numeração errada. Digite um valor entre 22 e 46."
    except ValueError:
        erro = "Digite um valor numérico."  
    return erro

def validaQuantidade(quantidade):
    erro = ""
    try:
        quantidade = int(quantidade)
        if quantidade <= 0:
            erro = "Quantidade negativa ou igual à 0."
    except ValueError:
        erro = "Digite um valor numérico."      
    return erro

def converteValor(valor): #convertendo nº com vírgula pra float
    virgula = re.search(r',', valor)
    if virgula:
        valor = re.sub(',', '.', valor)
    return valor

def validaValor(valor):
    erro = ""
    try:
        valor = float(valor)
        if valor <= 0:
            erro = "Valor negativo ou igual à 0."
    except ValueError:
        erro = "Digite um valor numérico." 
    return erro

def validaCor(cor):
    erro = ""   
    try:
        cor = int(cor)
        if cor > len(dados.coresFixas)-1:
            erro = "Cor inexistente."
    except ValueError:
        erro = "Digite um valor numérico correspondente à cor desejada: " 
    return erro

##################################################################
########################## Pegando os dados ######################

def pegaModelo():
    tabelaModelos()  
    modelo = input("Digite o nº correspondente ao modelo: ")
    err = validaModelo(modelo)
    while err != "":
        print(err)
        modelo = input("Digite o nº correspondente ao modelo: ")
        err = validaModelo(modelo)
    return int(modelo)

def pegaNumeracao():
    numeracao = input("Digite a numeração (em nºs): ")
    err = validaNumeracao(numeracao)
    while err != "":
        print(err)
        numeracao = input("Digite a numeração (em nºs): ")
        err = validaNumeracao(numeracao)
    return int(numeracao)

def pegaQuantidade():
    quantidade = input("Digite a quantidade (em nºs): ")
    err = validaQuantidade(quantidade)
    while err != "":
        print(err)
        quantidade = input("Digite a quantidade (em nºs): ")
        err = validaQuantidade(quantidade)  
    return int(quantidade)

def pegaValor():
    valor = input("Digite o valor (em nºs): ")
    valor = converteValor(valor)
    err = validaValor(valor)
    while err != "":
        print(err)
        valor = input("Digite o valor (em nºs): ")
        valor = converteValor(valor)
        err = validaValor(valor) 
    return float(valor)

def pegaCor():
    tabelaCores()
    cor = input("Digite o nº correspondente à cor desejada ou 0 para adicionar nova cor: ")
    if cor == "0":
        addcor.addCor()
    err = validaCor(cor)
    while err != "":
        print(err)
        cor = input(" ")
        err = validaCor(cor) 
    return int(cor)
