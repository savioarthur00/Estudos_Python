import math

#Desafio 05
frutas = ['maça','morango','manga','uva','abacaxi']

frutas.remove('manga')
frutas.__delitem__(-1)
print(frutas)

#Desafio 06
frutas.insert(0,'manga')
frutas.insert(-1,'abacaxi')

for f in frutas:
    print(f'Eu gosto de {f}')

#desafio 07
for x in range(0,10):
    print(x)

#desafio 08

legumes = ['Cenoura','beterraba','batata']

for f in frutas:
    for l in legumes:
        print(f'Fruta: {f} e legume: {l}')

#desafio 09

contador =0
while contador <=10:
    print(contador)
    contador += 1

#desafio 10

c= 1
while c <= 10:
    if c ==5:
        break

    print(c)
    c +=1
print('--')
c= 1
while c <= 10:
    if c ==5:
        c+=1
        continue

    print(c)
    c +=1

# desafio 11

a=['banana','laranja']
cont = 1
while cont <=3:
    a.append('maça')
    cont+=1
print(a)

# desafio 12

numeros =[1,2,3,4,5,6,7,8,9,10]

for n in numeros:
    if n %2==0 :
        print(f' o número {n} é par')
    else: print(f' o número {n} é impar')


# Desafio 13

pais_capital = {
    'Brasil':'Brasilia',
    'EUA':'Whasingthon',
    'Alemanha':'Munique',
    'França':'Paris'
}

escolha = input('Digite o nome de um país: ')

if escolha in pais_capital:
        print(f'A capital do {escolha} é {pais_capital[escolha]}')
else: print('Não temos informações sobre esse país')


# set

set_1 = {1,2,3,4,5}
set_2 = {3,4,6,7,8}

print(set_1 & set_2)

#def

def expoente(base,expo=2):
  return base.__pow__(expo)

b =int(input('Digite a base: '))
e =int(input('Digite o expoente: '))

print(expoente(b,e))

#fatorial
a = math.factorial(6)

# funções

def funcao1 (x):
    return x*2

def funcao2(x):
    a= x*x
    return funcao1(a)

print(funcao1(2))
print(funcao2(2))

# LAMBDA

nnumeros = [1,2,3,4,5,6]

Cubo = lambda num:  num**3
mult = lambda o,y: o*y
par = lambda v: 'par' if v%2==0 else 'impar'
result = []
quadrado = lambda x: x**2




print(Cubo(3))
print((mult(3,5)))
print(par(86))

for n in nnumeros:
    x=quadrado(n)
    result.append(x)

print(result)