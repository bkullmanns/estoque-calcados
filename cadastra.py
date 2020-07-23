import variaveis_e_listas as dados

import addestoque as add
import pega_e_valida as pegou

# função

def cadastra():
    modelo = pegou.pegaModelo()
    cor = pegou.pegaCor()
    numeracao = pegou.pegaNumeracao()
    quantidade = pegou.pegaQuantidade()
    adicionado = add.addEstoque(modelo, numeracao, quantidade, cor)

    if adicionado == False:
        valor = pegou.pegaValor()
        dados.lstModelo.append(dados.modelosFixos[int(modelo)-1])
        dados.lstNumeracao.append(numeracao) 
        dados.lstCor.append(dados.coresFixas[int(cor)-1]) 
        dados.lstQtd.append(quantidade)
        dados.lstValorUnit.append(valor)
        print("Cadastro realizado com sucesso!")
