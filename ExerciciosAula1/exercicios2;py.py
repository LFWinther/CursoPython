'''num_1 = input('Digite um número inteiro: ')

if num_1.isdigit():
    num_1 = int(num_1)
    if num_1 % 2 == 1:
        print('Ímpar')
    else:
        print('Par')

else:
    print('Isso não é um número inteiro.')'''



'''_____________________________________________________________'''
hora = input('Que horas são? ')
nome = input('Nome: ')
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('O horário deve estar entre 0 e 23')

    else:
        if hora >= 0 and hora <= 11:
            print(f'Bom dia {nome}.')
        elif hora >= 12 and hora <= 17:
            print(f'Boa tarde {nome}.')
        else:
            print(f'Boa noite {nome}.')
else:
    print('O horário deve estar entre 0 e 23')
'''_________________________________________________________________'''

'''usuario = input('Digite o seu primeiro nome: ')
qtd_carac = len(usuario)

if qtd_carac <= 4:
    print('Seu nomé é curto.')
elif qtd_carac <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')'''