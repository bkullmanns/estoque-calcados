import variaveis_e_listas as dados
import calcula_estoque as calculos
import termtables as tt
import re
from colorama import Fore, init
init()

def tabelaModelos():
    titulo = ["","MODELOS"]
    modelos = []

    for i, modelo in enumerate(dados.modelosFixos):
        modelos.append([i+1, modelo])      
   
    menuModelos = tt.to_string(
        modelos,
        header=titulo,
        style=tt.styles.ascii_thin_double
    )
    print(Fore.GREEN + "\n" + menuModelos + "\n")

########################################################################################################
###################### TABELA OPÇOES ###################################################################
########################################################################################################

def tabelaOpcoes():
    titulo = ["", "ATUALIZAR"]   
    op = []
    opcoes = ["Por modelo", "Específico"]

    for i, j in enumerate(opcoes):
        op.append([i+1, j])          

    listaOp = tt.to_string(
        op,
        header=titulo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + listaOp)

########################################################################################################
###################### TABELA CORES ####################################################################
########################################################################################################

def tabelaCores():
    titulo = ["", "CORES"]   
    cores = []

    for i, cor in enumerate(dados.coresFixas):
        cores.append([i+1, cor])  

    listaCores = tt.to_string(
        cores,
        header=titulo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + listaCores + "\n")

########################################################################################################
###################### TABELA NOVAS CORES ##############################################################
########################################################################################################

def tabelaNovasCores():
    titulo = ["", "ATUALIZA"]   
    cores = []

    for i, cor in enumerate(dados.novaCor):
        cores.append([i+1, cor])        

    listaCores = tt.to_string(
        cores,
        header=titulo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + listaCores + "\n")

########################################################################################################
###################### TABELA VENDA ####################################################################
########################################################################################################

def tabelaVenda(modelo, numeracao, cor, quantidade):
    topo = ["MODELO", "NUMERAÇÃO", "COR", "QUANTIDADE"] 
    linha = []   

    calculos.calculaEstoqueModelo()
    linha.append([modelo, numeracao, cor, quantidade]) 

    tabelaVenda = tt.to_string(
        linha,
        header=topo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + tabelaVenda)

########################################################################################################
###################### TABELA MENU #####################################################################
########################################################################################################

def relatorioGeral():
    topo = ["MODELO", "NUMERAÇÃO", "QUANTIDADE", "COR", "VALOR UNIDADE", "VALOR ESTOQUE"] 
    linhas = []  # lista criada pra gerar a tabela conforme doc da lib 
    calculos.calculaEstoqueModelo()
    for i in range(len(dados.lstModelo)):
        linhas.append([dados.lstModelo[i], dados.lstNumeracao[i], dados.lstQtd[i], dados.lstCor[i], 
        dados.lstValorUnit[i], dados.lstValorEstoque[i]]) 

    calculos.calculaEstoqueTotal()
    
    linhas.append(["--", "--", "--", "--", "--", dados.total])

    tabelaGeral = tt.to_string(
        linhas,
        header=topo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + tabelaGeral)

########################################################################################################
###################### TABELA MENU #####################################################################
########################################################################################################
    

def tabelaMenu():
    menu = ["","MENU"]   
    itens = [["0","Sair"], ["1", "Cadastrar Tenis"], ["2", "Relatório Geral"], ["3", "Realizar Venda"], ["4", "Atualizar preços"], 
    ["5", "Cadastrar cores"], ["6", "Exportar os dados"], ["7", "Importar os dados"]]

    menuGeral = tt.to_string(
        itens,
        header=menu,
        style=tt.styles.ascii_thin_double
    )
    print(Fore.RED + "\n" + menuGeral + "\n")