import variaveis_e_listas as dados
import termtables as tt
import re
import calcula_estoque as calculos


def lista():
    topo = ["MODELO", "NUMERAÇÃO", "QUANTIDADE", "COR", "VALOR UNIDADE", "VALOR ESTOQUE"] 
    listas = []  # lista criada pra gerar a tabela conforme doc da lib 
    calculos.calculaEstoqueModelo()
    for i in range(len(dados.lstModelo)):
        listas.append([dados.lstModelo[i], dados.lstNumeracao[i], dados.lstQtd[i], 
        dados.lstCor[i], dados.lstValorUnit[i], dados.lstValorEstoque[i]]) 

    tabelaRelatorio = tt.to_string(
        listas,
        header=topo,
        style=tt.styles.ascii_thin_double
    )
    print("\n" + tabelaRelatorio)