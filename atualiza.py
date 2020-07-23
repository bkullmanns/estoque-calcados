import variaveis_e_listas as dados
from tabelas import tabelaOpcoes
import pega_e_valida as pegou
import relatorio as mostra

def atualiza():
    tabelaOpcoes()
    op = input("Digite a opção escolhida (em nºs): ")
    if op == "0":
        menu()
    if op == "1":
        modelo = dados.modelosFixos[pegou.pegaModelo()-1]
        novoValor = input("Novo valor: ")
        for i, produto in enumerate(dados.lstModelo):
            if modelo == produto: 
                achei = True
                dados.lstValorUnit[i] = novoValor
                print("Valor atualizado com sucesso! ")
                mostra.lista()
        if not achei:
            print("Modelo não encontrado. ")

    elif op == "2":
        modelo = dados.modelosFixos[pegou.pegaModelo()-1]
        numeracao = pegou.pegaNumeracao()
        cor = dados.lstCor[pegou.pegaCor()-1]
        achei = False
        for i, m in enumerate(dados.lstModelo):
            if modelo == dados.lstModelo[i] and int(numeracao) == int(dados.lstNumeracao[i]) and cor == dados.lstCor[i]:
                achei = True
                print("Produto: ", modelo)
                print("Quantidade: ", dados.lstQtd[i])
                novoValor = input("Novo preco: ")
                dados.lstValorUnit[i] = novoValor
                print("Valor do respectivo modelo atualizado com sucesso!")
                mostra.lista()
        if not achei:
            print("Modelo não encontrado.")
    else: 
        print("Valor incorreto. Digite 1 ou 2 para acessar o menu desejado. Ou 0 para retornar ao menu principal: ")
        atualiza()    