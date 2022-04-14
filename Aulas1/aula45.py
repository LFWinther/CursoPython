'''
Operador ternário em Python
'''
# logged_user = True
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# print(msg)

'''-----'''
idade = input('Idade: ')
if not idade.isnumeric():
    print('Você prcisa digitar um número')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode entrar' if e_maior else 'Não pode entrar'
    print(msg)