''' Quantidade de caricteres '''

usuario = input('Usuário: ')
qtd_carac = len(usuario)

if qtd_carac < 6:
    print('Precisa de pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado.')