numero_secreto = 67
descrobriu = False

for n in range(10):
    if not descrobriu:
        chute = int(input('Descubra um número de 0 a 100!\nSeu chute: '))
        if chute < numero_secreto:
            print('Chute muito baixo!')
        elif chute > numero_secreto:
            print('Chute muito alto!')
        else:
            print('Descobriu!')
            descrobriu = True



if descrobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_secreto}')