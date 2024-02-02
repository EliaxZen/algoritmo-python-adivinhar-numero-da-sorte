numero_secreto = 10
descrobriu = False

if not descrobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descrobriu = True

if not descrobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descrobriu = True

if not descrobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
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