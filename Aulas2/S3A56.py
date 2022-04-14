'''
Funções (def) em Python - args **kwargs -
'''
def func(a1,a2, a3, a4, a5, nome=None):
    print(a1,a2,a3,a4,a5, nome)
    return nome
var = func(1,2,3,4, 5, nome='Luis')
print(var)