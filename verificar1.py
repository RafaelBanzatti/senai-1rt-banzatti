while True:
    numero = int(input('Insira um valor: '))
    if numero <0:
        print ('numero negativo')
        break

    if numero %2 == 0:
        print ('o numero {} eh par'.format(numero))
    else:
        print ('o numero {} eh impar'.format(numero))
