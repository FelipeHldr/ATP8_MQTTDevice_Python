import random


def temperatura2():
    return random.randrange(25, 35)


def aquecedor2(estado2: str):
    if estado2 == 'on':
        print('Aquecedor da estufa 2 LIGADO')
    else:
        print('Aquecedor da estufa 2 DESLIGADO')
