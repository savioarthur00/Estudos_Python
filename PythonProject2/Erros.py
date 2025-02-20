try:
    letras = ['a','b','c']
    print(letras[4])

except IndexError:
    print('Index fora do array.')


try:
    valor = int(input('Digete o valor do produto: '))
    print(valor)

except ValueError:
    print('ERRO: Você deve digitar um número inteiro, letras não são aceitas')


finally: print('FINALLY: Tudo que está dentro do finally vai rodar com ou sem erro')

try:
    valor = int(input('Digete o valor do produto: '))
    print(valor)

except ValueError:
    print('ERRO: Você deve digitar um número inteiro, letras não são aceitas')


else:
    print('Else: Só vem para o else se a condição do try for verdadeira!')