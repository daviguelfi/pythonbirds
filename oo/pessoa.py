class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        # atributo  parametro
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        # python3.6 return f'Ola {id(self)}'
        return 'Ola {id(self)}'


if __name__ == '__main__':
    davi = Pessoa(nome='Davi')
    luciano = Pessoa(davi, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print('Filho ' + filho.nome)
    luciano.sobrenome = 'Guelfi'
    del luciano.filhos
    print(luciano.__dict__)
    print(davi.__dict__)
