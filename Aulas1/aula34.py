'''
While (enquanto)
utilizamos para realizar ações enquanto uma condiçaõ for verdadeira.
* Requisitos: Entender condiçõe se operações
'''
'''while True: #loop infinito
    nome = input('Nome: ')
    print(f'Olá {nome}')           '''

x = 0
y = 0
'''while x <= 10:
    print(x)
    x = x+ 1
print('FIM')'''

'''while x < 10:
    if x == 3:  #se x é igual a 3 não vai ser lido o restante do cod
        x = x + 1
        continue  # sempre que usado tudo após a ele não será lido
    print(x)
    x = x + 1
print('FIM')'''

'''while x < 10:
    if x == 3:
        x = x + 1
        break  # finaliza o cod
    print(x)
    x = x + 1'''

'''__________________________________________________________________'''
'''while x < 10:
    y = 0
    while y < 5:
        print(f'X vale{x} e Y vale {y}')
        y += 1
    x += 1  # x = x + 1
print('FIM')'''

'''---------------------------------------------------------------------------'''

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('deseja sair? [s]im oi [n]ão')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

      # +  -  /  *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido.')
    if sair == 's':
        break
