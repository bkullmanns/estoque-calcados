from tabelas import tabelaCores, tabelaNovasCores
from variaveis_e_listas import novaCor, lstCor, coresFixas
import variaveis_e_listas as dados

def addCor():
    tabelaCores()
    cor = input("Digite uma nova cor (ou 0 para voltar ao menu): ").capitalize()
    if cor == "0": 
        menu()
    elif cor in dados.coresFixas:
        print("Cor já existente. Adicione uma cor diferente ou 0 para voltar ao menu. ")
        tabelaCores()
        addCor()
    elif cor.isdigit() == True:
        print("Valor incorreto. Digite a nova cor desejada. ")
        addCor()
    if len(cor) > 0 and cor.isdigit() == False:
        dados.novaCor.append(cor)
        dados.coresFixas.append(cor)
        print("Nova(s) cor(es) cadastradas: \n")
        tabelaNovasCores()
    sai = input("Continuar cadastrando? (s/n) ")
    if sai == "s":
        addCor()
    else: 
        tabelaCores()
        