import variaveis_e_listas as dados
import addestoque as add
import calcula_estoque as calculos
import pega_e_valida as pegou
import tabelas
import main as principal

def venda():
    modelo = dados.modelosFixos[pegou.pegaModelo()-1]
    numeracao = pegou.pegaNumeracao()
    quantidade = pegou.pegaQuantidade()
    cor = dados.lstCor[pegou.pegaCor()-1]

    achei = False
    for i, m in enumerate(dados.lstModelo):
        if modelo == dados.lstModelo[i] and int(numeracao) == int(dados.lstNumeracao[i]) and cor == dados.lstCor[i]:
            achei = True
            if int(dados.lstQtd[i]) >= quantidade:
                achei = True
                tabelas.tabelaVenda(modelo, numeracao, cor, quantidade)
                confirmacao = input("\n Confirma? s/n: ")
                if confirmacao == "s":
                    dados.lstQtd[i] = int(dados.lstQtd[i]) - quantidade
                    input("Venda confirmada. ")
                    menu()
            else:
                input("Venda cancelada. ")

    calculos.calculaEstoqueModelo()
    calculos.calculaEstoqueTotal()

    if not achei:
        op = input("Produto não encontrado. Digite um produto cadastrado ou 0 para retornar ao menu. ")
        if op == "0":
            principal.menu()
        else:
            venda()