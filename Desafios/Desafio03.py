

funcionarios = {'Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa'}
turno_dia = {'Ana','Marcos','Alice','Melissa'}
turno_noite = {'Pedro','Sophia','Bruno'}
tem_carro = {'Marcos','Alice','Bruno','Melissa'}


carro_noite = (tem_carro & turno_noite)
print(carro_noite)
carro_dia = (tem_carro & turno_dia)
print(carro_dia)
nao_tem_carro = funcionarios - tem_carro
print(nao_tem_carro)

funcionarios2 = ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia2 = ['Ana','Marcos','Alice','Melissa']
turno_noite2 = ['Pedro','Sophia','Bruno']
tem_carro2 = ['Marcos','Alice','Bruno','Melissa']

car_noi = set(tem_carro2).intersection(turno_noite2)
car_dia = set(tem_carro2).intersection(turno_dia2)
no_car = set(funcionarios2).difference(tem_carro2)
print(car_noi)
print(car_dia)
print(no_car)