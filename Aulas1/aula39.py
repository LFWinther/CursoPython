while True:
    num_1 = input('Digite um número: ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        print()
        continue
    operador = input('Digite um operador (+ - * /):')
    num_2 = input('Digite outro número: ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        print()
        continue


    num_1 = int(num_1)
    num_2 = int(num_2)


    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador    == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido')