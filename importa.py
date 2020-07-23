def importaDados():
    with open('estoque.txt', 'r') as arq:
        for tenis in arq:
            print(tenis.strip('\n'))