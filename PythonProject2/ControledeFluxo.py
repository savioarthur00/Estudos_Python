#for loops


# RANGE = FAÇA ATÉ
for x in range(5):
    print(x) # Imprimindo de 0 a 4
print('---------------')
for x in range(1,6):
        print(x) #imrpimindo de 1 a 5
print('---------------')
for x in range(1, 10,2):
        print(x) #imprime de 1 a 10, pulando de 2 em 2


print('------------------------------------------------')
# Para Strings

frase = ' Agora imprima essa frase, letra a letra'
for x in frase:
    print(f'A letra {x} pertence a frase {frase}')

print('------------------------------------------------')
# if dentro de for

compra= False
dados= 'Compra aprovada com sucesso'

for tentativas in range(1,5):
    if compra:
        print(dados)
        break
    elif tentativas == 3:
        compra = True
    else:   print(f'{tentativas}º tentativa para aprovar a compra')

print('------------------------------------------------')
#NESTED LOOPS  = loop dentro de loop

for x in range (1,6):
    print('produto ' + str (x))
    for y in range (1,5):
        print(x,y)

print('------------------------------------------------')
# separando strings

palavra = 'FANTASTICO'
for espaco in palavra:
    print(f' {espaco}', end='')
print()
print('------------------------------------------------')
# criando um retangulo

simbolo = '/'

for linha in range(6):

    for coluna in range(6):
        print(simbolo, end='')
    print()

print('------------------------------------------------')
# WHILE LOOP

valor = 100
dia = 1
while valor > 20:
    print(f'No {dia}º dia, o produto será vendido por R${valor},00')
    dia +=1
    valor -=10

print('------------------------------------------------')
# operador ternario

idade=12

resultado2 = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print(resultado2)
