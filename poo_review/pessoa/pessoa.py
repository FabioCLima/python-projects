class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int, email: str, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
        self._senha = senha



    def __repr__(self) -> str:
        return f"<< Nome:{self.nome} {self.sobrenome}-idade {self.idade} anos>>"

    def mostrar_dados(self) -> str:
        return f"Nome: {self.nome} {self.sobrenome} \n idade:{self.idade} anos"

    def mostrar_email(self) -> str:
        return f"email: {self.email}"

    def mostrar_senha(self) -> str:
        return f"senha: {self._senha}"
