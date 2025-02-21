#Ponto da carne



contador =0
while contador <=10:
    temperatura = int(input('Qual a temperatura atual da carne? '))
    if temperatura < 48:
        print('Deixe cozinhar um pouco mais')
    elif temperatura in range(48,53): print('A carde está selada -  rare')
    elif temperatura in range (54,59): print('A carde está ao ponto para mal - Medium rare')
    elif temperatura in range(60,64): print('A carde está ao ponto - well')
    elif temperatura in range (65,70): print('A carde ao ponto para bem- Medium well')
    elif temperatura in range (71,75): print('A carde está bem passada - well done')
    else: print('A carne queimou!')
    contador += 1
