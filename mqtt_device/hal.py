import random


def temperatura():
    return random.randrange(25, 35)


def aquecedor(estado: str):
    if estado == 'on':
        print('Aquecedor da estufa 1 LIGADO')
    else:
        print('Aquecedor da estufa 1 DESLIGADO')
