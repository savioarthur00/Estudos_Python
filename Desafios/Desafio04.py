#Calculadora de IMC

def imc2(altura,peso):
    a = (altura/100)**2
    return peso/a

altura = float(input('Digite sua altura em Cm: '))
peso = float(input('Digite seu peso: '))

imc = float(imc2(altura,peso))

if imc < 18.5:
    print('Magreza')
elif 18.5 < imc < 24.9:
    print('Normal')
elif 25.0 < imc < 29.9:
    print('Sobrepeso')
elif 30 < imc < 39.9:
    print('Obesidade')
else :
    print('Obesidade grave')