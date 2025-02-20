
def somar(x,y):
    print(f'A soma dos dois valores é: {x+y} ' )

def subtracao(x,y):
    print(f'A subtração dos dois valores é: {x-y} ' )

def find_index(to_find,item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1

