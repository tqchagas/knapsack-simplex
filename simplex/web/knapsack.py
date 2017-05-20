from pulp import (
    LpInteger, LpMaximize, LpProblem, LpStatus, LpVariable
)


def knapsack(w, wi, vi):
    itens = list(sorted(vi.keys()))

    # modelo
    modelo = LpProblem("Knapsack", LpMaximize)

    # variaveis
    x = LpVariable.dicts('x', itens, lowBound=0, upBound=1, cat=LpInteger)

    # objetivo
    modelo += sum(vi[i] * x[i] for i in itens)

    # constantes
    modelo += sum(wi[i] * x[i] for i in itens) <= w

    # otimizacao
    modelo.solve()

    # status
    status = LpStatus[modelo.status]

    respostas = []
    for i in itens:
        respostas.append("{0} = {1}".format(
            x[i].name.split('_')[1], int(x[i].varValue)))
    return status, respostas
