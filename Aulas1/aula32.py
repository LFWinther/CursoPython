# Formatando valores com modificadores

'''
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuantes (float)
:.(número)f -  Qunatidade de casa decimais (float)
:(Caractere) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

< - Esquerda
> - Direita
^ - Cima
'''

num_1 = 1
print(f'{num_1:0>10}') # aplica 9 zeros até completar as 10 casa solitidatas
num_2 = 1024
print(f'{num_2:0^10}')
num_3 = 1150
print(f'{num_3:.2f}')

