import sys


def entrada():
    filcol = sys.stdin.readline().split(" ")
    numf = int(filcol[0])
    numc = int(filcol[1])
    n = int(sys.stdin.readline())

    tablero = []

    for i in range(numf):
        tablero.append([0] * numc)

    for i in range(n):
        en = sys.stdin.readline().split(" ")
        tablero[int(en[0])][int(en[1])] = int(en[2])

    return numf, numc, tablero


def solver(numf, numc, tablero):

    c = numc - 1

    valores = []
    for i in range(numf):
        valores.append([0] * numc)

    while c >= 0:
        f = numf - 1
        while f >= 0:
            if c == numc - 1:
                der = 0
            else:
                der = valores[f][c + 1]
            if f == numf - 1:
                aba = 0
            else:
                aba = valores[f + 1][c]

            valores[f][c] = tablero[f][c] + max(der, aba)
            f -= 1
        c -= 1

    return valores[0][0]





# PROGRAMA PRINCIPAL ----------------------------------------------------------------
sys.setrecursionlimit(5000)

numf, numc, tablero = entrada()

print(solver(numf, numc, tablero))
