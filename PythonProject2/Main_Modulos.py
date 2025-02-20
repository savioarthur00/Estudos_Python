import Modulos  #Puxa todas as funções do modulo
# from Modulos import somar, subtracao  -- Puxa somente as funções especifícas
from Modulos.Modulo import somar,subtracao,find_index

list1 = ['a','b','c','d','e']
var_c=find_index(list1,'d')
print(var_c)
