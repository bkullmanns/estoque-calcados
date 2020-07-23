import variaveis_e_listas as dados

def calculaEstoqueModelo():
    global lstValorEstoque #global resolvendo problema de escopo
    dados.lstValorEstoque = []

    for i, valor in enumerate(dados.lstValorUnit):
        quant = int(dados.lstQtd[i])
        valEstoque = quant * float(valor)
        dados.lstValorEstoque.append(valEstoque)

def calculaEstoqueTotal():
    global total
    for i in range(len(dados.lstModelo)):
        dados.total = float(dados.total) + float(dados.lstValorEstoque[i])
        dados.total = "{0:.2f}".format(dados.total) 