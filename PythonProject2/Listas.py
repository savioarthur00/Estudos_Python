from array import array

#Criando uma Lista
cidades = ['Rio de janeiro', 'São Paulo', 'Recife', 'João Pessoa']
print(cidades)

#Manipulando listas
numeros = [1,2,3,4,9,0]

numeros[0] = 30
numeros.append(59)
numeros.remove(4)
numeros.insert(1,369)
numeros.pop(2)
numeros.sort()
print(numeros)

# concatenação de listas

numeros_2 = [88,89,87,86,85]
multiplicar_lista = numeros_2 * 3

concatenacao = numeros_2 +numeros
numeros_2.extend(numeros)

print(multiplicar_lista)
print(f'Concatenação simples: {concatenacao}')
print(f'Concatenando com extends: {numeros_2}')

#LISTAS DENTRO DE LISTAS
itens =[['item 1','item 2'], ['item 3','item 4']]
print(itens[1][1])

# UNPACKING LISTS

produtos = ['Arroz','Feijão','Laranja','Banana',1,2,3,4,5]

item1,item2, *outros, item8 = produtos

print(item1)
print(item2)
print(item8)
print(outros)

# Looping dentro de LISTS

valores = [50,80,110,189,125]

for x in valores:
    print(f'O valor do produto é de: R$ {x}')

# LISTAS

cores = ['azul','amarelo','verde','preto','vermelho']

cor = input('Digite a cor que você deseja: ')

if cor.lower() in cores:
        print(f'A cor {cor} tem no estoque!')
else: print('A cor não tem em estoque')

# SEPARANDO STRINGS CM LIST

var = list('Fisioterapia')
print(var)

# Zipando LISTAS

cores_novas = ['azul','vermelho','amarelo','verde','preto']
preco = [10,20,30,40,50]

duas_listas = list(zip(cores_novas,preco))
print(duas_listas)

# input em listas com ,

fruta = input('Digite frutas separadas por virgulas: ')

lista = fruta.split(', ')
print(lista)

#TUPLES: USA O () E NÃO PODE SER ALTERADAS!
# ARRAYS: SÃO INDICADOS PARA LISTAS MUITO GRANDES  -lembrar de importar

letras = ['a','b','c','d']
inteiros = [1,2,3,4,5,6,7,8,9]
floates = [1.2,1.3,1.4]

l = array('w',['a','b','c','d'])
i = array('i',[1,2,3,4,5,6,7,8,9])
f = array('f',[1.2,1.3,1.4])

print(l)
print(i)
print(f)

# USANDO SET : {}  SIMILAR A LISTA, NÃO POSSUI INDEX, NÃO PERMITE DUPLICADOS

list1 = [10,20,30,40,50]
list2= [10,20,30,60,70,80]

set1 = set(list1)
set2= set(list2)

set1.add(77)
set1.update([10,90,100])
set1.remove(10)
set1.discard(110) #Se não existir, não dá erro

print(set1 | set2) #Union  #concatena e remove os valores duplicados  - .union
print(set1 - set2) #Difference - .difference
print(set1 & set2) #And - .and
print(set1 ^ set2) #Symmetric Difference  - remove todos que tem repetidos!

set3 = set2.union(set1)

print(set3)

# UTILIZANDO DICIONÁRIOS (KEY,VALUES)

aluno = {'Nome':'Ana', 'idade':20, 'Situação':'Cadastrada'}

print(aluno['Situação'])

#alterando um item do dicionário:

aluno['Nome'] = 'Gabriella'
print(aluno)
aluno.update({'nome': 'Ana Gabriella', 'idade':21, 'Endereço':'Serra Talhada'})  #Update além de atualizar, tbm adiciona caso não possua
print(aluno)
del aluno['idade']
print(aluno.get('nome'))


# for com Dicionários

aluno2 = {
    'Nome':'Ana',
    'idade':20,
    'Situação':'Cadastrada',
    'Materias': ['Matematica','Física']

}


for x in aluno2.values():
    print(f'Imprime os valores: {x}')

for x in aluno2:
    print(f'Imprime as keys: {x}')

for x in aluno2.items():
    print(f'Imprime as chaves e valores: {x}')

for keys,values in aluno2.items():
    print(f'Impime os valores: {keys} e os Valores: {values} sem parenteses')

# função lambda
# Função sem nome, somente 1 única expressão.   Argumento : Expressão
# Muito utilizada dentro de uma função

somar = lambda x,y: x+y
print(somar(5,6))

def calculadora (x,y):
    resultado = lambda x,y: x+y +10
    return resultado(x,y) *10

print(calculadora(2,2))


# MAP

lista_a = [1,2,3,4]

def multi (x):
    return x*2

Lista_resultado=map(multi,lista_a)
print(list(Lista_resultado))

# map com lambda

print(list(map(lambda x: x*2, lista_a)))

# FILTER - filtrar resultados

filtragem  = [10,20,30,40,50,60,70,80]

def menor20 (x):
    return x > 20

print(list(filter(menor20,filtragem)))

print(list(filter(lambda x: x>30, filtragem)))


#LIST COMPREHENSION ( EXPRESSÃO for ITEN in ITENS)
# Lista dentro de um for, mais curta de escrver

frutas_a = ['abacaxi','maracuja','caja','pera','graviola','imbu']
frutas_com_a=[]
frutas_sem_a = []
# sem a compreensão
for f in frutas_a:
    if 'a' in f:
        frutas_com_a.append(f)
    else: frutas_sem_a.append(f)

print(frutas_com_a)
print(frutas_sem_a)

# com compreensão
frutas_novas = [fruta for fruta in frutas_a if 'c' in fruta]
print(frutas_novas)

numerologia = []

for x in range(6):
    numerologia.append(x *10)
print(numerologia)

numerologia_2 = [numero*10  for numero in range(7) ]
print(numerologia_2)




# GERADORES DE EXPRESSÃO
# COLOCANOD APENAS EM ()
# Mais economico em bytes

from sys import getsizeof

#GENERATOR
numerologia_2 = (numero*10  for numero in range(7))
print(getsizeof(numerologia_2))

#LIST
numerologia_2 = [numero*10  for numero in range(7) ]
print(getsizeof(numerologia_2))