import math


def soma(a,b):
    print(a+b)
def subtrai(c,d):
    print(c-d)
def multiplicar(e,f):
    print(e*f)
def dividir(g,h):
    print(g/h)

soma(2,6)
subtrai(10,6)
multiplicar(3,9)
dividir(90,9)

print('--------------------------------')

def nomes(nome):
    print(f'Bem vindo: {nome}')

nomes("Sávio Arthur")

print('--------------------------------')
#Default e Non-Default
#Default = Define o valor no parametro (Idade)
#Non-Default = Não define o valor no parametro (Nome)

#ARGUMENTOS DEFAULT DEVE VIR SEMPRE NO FINAL

def nome_idade(nome,idade=21):
    print(f'Olá, meu nome é {nome} e tenho {idade} anos de idade')

nome_idade('Sávio')

print('--------------------------------')

def cliente(nome):
    return f'Olá {nome}'

Savio = cliente('Sávio Arthur')
print(Savio)

def calculadora(a,b):
    return a+b

p = calculadora(10,15)
o = calculadora(20,30)

resultado4 = p+o
print(resultado4)

print('--------------------------------')
# Vários argumentos (xargs)  = Coloca * antes do parametro

def somatorio(*numeros):
    total =0
    for valores in numeros:
        total += valores

    return total

def subtratorio(*numeros):
    total = 0
    for n in numeros:
        total -= n
    return total

def multiplicatorio(*numeros):
    total = 0
    for n in numeros:
        total  *= n
    return total

x = somatorio(1,2,3,4,5,6,7,8,9)
m= multiplicatorio(1,2,3,4,5,6,7,8,9)
s = subtratorio(1,2,3,4,5,6,7,8,9)

print(x)
print(m)
print(s)
print('--------------------------------')
#varios argumentos e varios parametros

def agencia(**carros):
    return carros

print(agencia(marca = 'Gol', cor = 'Preto', motor = 1.3))
print(agencia(marca = 'Gol', cor = 'Preto', motor = 1.3, placa = "1343"))
print(agencia(marca = 'Gol', cor = 'Preto'))

print('--------------------------------')
#Modulos -> Importando modulo de matematica

print(math.factorial(99))
print(math.floor(1.89))
print(math.ceil(2.89))


