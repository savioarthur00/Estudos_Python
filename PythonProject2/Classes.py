from datetime import datetime

class  Funcionario:

    def __init__(self,nome,sobrenome,data_nascimento):
        self.nome=nome
        self.sobrenome=sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_atual(self):
        ano_atual = datetime.now().year
        return int(ano_atual-self.data_nascimento)


usario1 = Funcionario('Sávio','Arthur',2009)
usario2 = Funcionario('Ana','Gabriella',2006)


print(Funcionario.nome_completo(usario2))
print(Funcionario.idade_atual(usario1))



