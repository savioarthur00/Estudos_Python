#Latas de tintas necessárias

def latas (rend,altura,largura):
    area = altura * largura
    print(f'Você irá precisar de: {area/rend} latas de tinta')

rendimento = int(input('Qual o rendimento da tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

latas(rendimento,altura,largura)
