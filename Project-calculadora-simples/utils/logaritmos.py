"""Operações Logaritmicas"""

import math


def log_N():
    n = input('Digite o valor de N, para o cálculo do log_N:\n')
    try:
        N = float(n)
        resultado = math.log(N)
        return resultado
    except ValueError:
        return("Operação não permitida")


def log10_N():
    n = input('Digite o valor de N, para o cálculo do log10_N:\n')
    try:
        N = float(n)
        resultado = math.log10(N)
        return resultado
    except ValueError:
        return("Operação não permitida")


def log2_N():
    n = input('Digite o valor de N, para o cálculo do log2_N:\n')
    try:
        N = float(n)
        resultado = math.log2(N)
        return resultado
    except ValueError:
        return("Operação não permitida")
