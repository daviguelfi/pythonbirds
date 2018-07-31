class Pessoa:
    def __init__(self, nome = None, idade=35):
        # atributo  parametro
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return 'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'davi'
    print(p.nome)
