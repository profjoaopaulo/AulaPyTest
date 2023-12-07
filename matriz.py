

#Leitura da Matriz:
#linhas

mat = []

for i in range(3):
    m = [] #matriz vazia
    l = int(input("Linhas?"))
    c = int(input("Colunas?"))
    for i in range(l):
        linha = []
        #colunas
        for j in range(c):
            linha.append(input("M%i%i: " % (i, j)))
        m.append(linha) #adicionando a linha

    #Impressão da matriz:
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()

    mat.append(m)


print(mat)