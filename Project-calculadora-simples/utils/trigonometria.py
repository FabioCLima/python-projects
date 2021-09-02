"""operações trigonométricas"""

import math


def seno(n):
    try:
        angulo = float(n)
        resultado = math.sin(angulo)
        return resultado
    except ValueError:
        return("Entre com um número válido para o cálculo do seno.")


def cosseno():
    try:
        angulo = float(n)
        resultado = math.cos(angulo)
        return resultado
    except ValueError:
        return("Entre com um número válido para o cálculo do cosseno.")


def tangente(n):
    try:
        angulo = float(n)
        resultado = math.tan(angulo)
        return resultado
    except ValueError:
        return("Entre com um número válido para o cálculo do tangente.")