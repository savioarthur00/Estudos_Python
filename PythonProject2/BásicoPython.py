import math
# Usa-se a # para fazer um comentário  atalho :(ctrl + / )
''' Aspas triplas são
comentários extensos
'''

print ("Pode ser com aspas simples ou duplas, em caso de texto. Caso for variavel basta colocar o nome da variável")
print("---------------------------------------------")
print(" DEFININDO VARIÁVEIS ")
nome = "Sávio"
sobrenome = "Arthur"
print(nome + " " + sobrenome)
print("---------------------------------------------")
print(" TIPOS DE VARIÁVEIS")
print("INT - FLOAT - STRING - BOOLEAN  - NONE")
idade = 25 #int
peso = 71.2 #float
nome2 = "Sávio" #String
status = False #boolean (Primeira letra maiuscula)
vazio = None # Ausencia de valor (Primeira letra maiuscula)
print(type(nome2))
# print(type(idade))
# print(type(peso))
# print(type(status))
# print(type(vazio))

print(nome2,",tem ", idade , "anos," , "pesa: " , peso , ",ele vai para a academia? " , status)

print("---------------------------------------------")
print(" OPERADORES MATEMATICOS ")

num1= 10
num2 = 8
resultado = num1 + num2
print(resultado)
print("Soma:", num1 + num2)
print("Subtração:", num1 - num2)
print("Multiplicação:", num1 * num2)
print("Potencia: " , num1 ** num2)
print("Divisão:", num1 / num2)
print("Divisão mostrando somente o inteiro: " ,num1 // num2)
print("Divisão mostrando somente o resto: " ,num1 % num2)

print("---------------------------------------------")
print(" OPERADOR DE ATRIBUIÇÃO AUMENTADA")

print("Usando o: += | -=  | *= | /=  ")
prod1 = 10
prod1/=5
print(prod1)

print("---------------------------------------------")
print(" FUNÇÕES ")

numb = 1.59876524
print("Função para arredondar Round: " ,round(numb))  #arredonda valores
print("Função para arredondar Round (Numero,X):" ,round(numb,3))  #arredonda valores com X casas decimais
print("Função para fazer potencia Pow:", pow(2,3)) # função de potencia (2 elevado a 3)
print("Função para maior valor Max: ", max(2,6,15,26,95,87,102))
print("Função para menor valor Min:", min(2,6,15,26,95,87,102))
print("Função para somar valores Sum:", sum([2,6,15,26,95,87,102]))
print("---------------------------------------------")

print(" ORDEM DOS OPERADORES")

print("1º Parenteses: ()")
print("2º Expoentes: **")
print("3º Multiplicação: *")
print("4º Divisão: /")
print("5º Divisão inteira: //")
print("6º Modulo: %")
print("7º Adição: +")
print("8º Subtração: -")

print((10+2)*3 + (5*6)**2)
print("---------------------------------------------")

print("  Usando o modulo MATH")

print(math.ceil(4.3)) # Ceil = teto; Arredonda para cima
print(math.floor(4.3)) # Floor = chão; Arredonda para baixo
print(math.pow(4,3)) # Potencia
print(math.sqrt(16)) #Raiz qubrada

print("---------------------------------------------")

print(" MANIPULANDO STRINGS")

mensagem = 'Este Curso é Muito Bom'

#indexação e fatiamento
print(f'Pegando somente 1 caractere: {mensagem[0]}') #Somente 1 indice
print(f'Pegando somente um trecho da frase: {mensagem[0:4]}') #trecho, não incluíndo o 3

#Metodos em String

print(f'Colocando tudo em maiusculo: {mensagem.upper()}') #tudo em maisculo
print(f'Colocando tudo em minusculo: {mensagem.lower()}') #tudo minusculo
print(f'Removendo espacços no inicio: {mensagem.strip()}') #Remove espaços no inicio
print(f'Trocando palavras:  {mensagem.replace('BOM','Excelente')}') #troca palavras
print(f'Separando palavra por palavra: {mensagem.split()}') #Separa palavra por palavra

# Formatação f-String
name = 'Sávio'
age = 28

print(f'Usando o f-String: O meu nome é {name} e tenho {age} anos de idade')

# Escape Sequece
mensagem2 = 'Quebrando Linhas:  Aprender Python é \n muito simples' #\n serve para quebrar linhas
print(mensagem2)

tabulacao = "Tabulando:  Coluna 1 \t Coluna 2 \t Coluna 3"  #\t serve para tabular, criando colunas
print(tabulacao)

#Usando a barra invertida para localizar arquivos
barraInvertida = 'Usando barra para endereçamentos:  c:\\users\\Savio' #Usa-se 2 barras para identificar que é uma barra invertida
print(barraInvertida)

#Colocando aspas em um texto

aspasNoTexto = 'Colocando aspas no texto:  Aprender \'Python\' é muito divertido '
print(aspasNoTexto)

#Tabulando e pulando linhas em 1 unica linha

tabulando_e_pulando_linhas = 'Nome:\tSávio Arthur\nIdade:\t25\nPaís:\tBrasil'
print(tabulando_e_pulando_linhas)

print("OBS: Aspas triplas servem para textos multilinhas ")


print("---------------------------------------------")

print(' Usando o INPUT')
nome4 = input('Digite o seu nome: ')

print(nome4)

print("---------------------------------------------")

print(' Convertendo String para Int')

numero = int(input('Digite um número: '))
print(type(numero))

print("---------------------------------------------")
print(' MINI PROGRAMA: ACRSCENTANDO 10%')

produto = float(input('Digite o valor do produto: '))
acrescimo_10 = produto* 1.1

print(f'Com um acréscimo de 10% o valor do produto fica: R${acrescimo_10:.2f}')

print("---------------------------------------------")
print(' 2 ENTRADAS EM 1 ÚNICO INPUT')

dados = input('Digite seu nome e sua idade: ').split()
nome5 = dados[0].upper()
idade2 = dados[1]

print(nome5)
print(idade2.upper())

print("---------------------------------------------")
print('Exercicio 01')

# temperatura = float(input('Qual a temperatura atual? '))
temperatura = 15
if(temperatura <10):
    print('Muito frio!')
elif ( 10<temperatura<20):
    print('Está agradavel')
else: print('Está quente')
print("---------------------------------------------")
print('Exercicio 02')
horario = 15
if(horario <12):
    print('Bom dia')
elif ( 12<horario<18):
    print('Boa tarde')
else: print('Boa noite')
print("---------------------------------------------")
print('Exercicio 03')

compra = float(input('Digite o valor da compra: '))

if(compra>200):

    print(f'O valor final com o desconto foi de R${compra*0.8: .2f}')
elif(compra > 100):
    print('Após 10% de desconto o valor final foi de: ', compra * 0.9)
else: print('Após 5% de desconto o valor final foi de: ',compra*0.95)

print("---------------------------------------------")
print('Exercicio 04')

username= 'admin'
password= 12345
login = input('Digite seu login: ')
senha = int(input('Digite sua senha: '))

if(login == username and senha == password):
    print('Logado!')
else: print('Você digitou login ou senha inválidos')

print("---------------------------------------------")
