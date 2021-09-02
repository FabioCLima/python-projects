import datetime


class Funcionario:
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salário': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

    @staticmethod
    def dia_util(dia):
        # segunda = 0
        # domingo = 0
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


fabio = Funcionario('Fabio Lima', 9500)
print(fabio.nome)
print(fabio.dados())
fabio.aplicar_aumento()
print(fabio.dados())
Funcionario.definir_novo_aumento(1.15)
fabio.aplicar_aumento()
print("novo aumento do Fabio")
print(fabio.dados())

fabiana = Funcionario('Fabiana Oliveira', 4000)
print(fabiana.dados())
fabiana.aplicar_aumento()
print(fabiana.dados())

my_date = datetime.date(2021, 8, 21)
print(Funcionario.dia_util(my_date))
