''' *enumerate '''

lista = [['Edu', 'João', 'Luis'],  #0
    ['Maria', 'Aline', 'Joana'],  #1
    ['Helena', 'Ed', 'Lu'],]  #2

# enumerada = list(enumerate(lista))
# print(enumerada[1][1][2])

for v1, v2 in enumerate(lista):
    print(v1, v2)