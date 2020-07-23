import pega_e_valida as pegou
import variaveis_e_listas as dados

def addEstoque(modelo, numeracao, quantidade, cor):
    adicionou = False
    for i, m in enumerate(dados.lstModelo):
        if m    == dados.lstModelo[i]    and \
            numeracao == int(dados.lstNumeracao[i]) and \
            dados.coresFixas[int(cor)-1]      == dados.lstCor[i]:
            quantidadeAntiga = dados.lstQtd[i]
            dados.lstQtd[i] = int(dados.lstQtd[i]) + quantidade
            print("Modelo: ", m)
            print("Numeração: ", numeracao)
            print("Cor: ", dados.coresFixas[int(cor-1)])
            print("Quantidade antiga de pares: ", quantidadeAntiga)
            print("Nova quantidade ", dados.lstQtd[i])
            confirmacao = input("Confirma? s/n: ")
            if confirmacao == "s":
                input("Estoque atualizado. ")
                adicionou = True
    return adicionou