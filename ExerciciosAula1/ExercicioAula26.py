usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'luis'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Connect')
else:
    print('Usuário ou senha inválidos.')