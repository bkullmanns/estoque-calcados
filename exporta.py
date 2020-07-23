import variaveis_e_listas as dados

def exportaDados():
    with open('estoque.txt', 'w') as arq:
        for i, modelo in enumerate(dados.lstModelo):
            arq.write(modelo + ', ' + str(dados.lstNumeracao[i]) + ', ' + str(dados.lstCor[i]) + ', ' \
            + str(dados.lstQtd[i]) + ', ' + str(dados.lstValorUnit[i]) + '\n')
        print("Dados exportados com sucesso!")