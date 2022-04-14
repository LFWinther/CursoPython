'''
For in em python
Interando str com for
função range (start = 0, stop, step = 1)
'''

# texto = 'python'

contador = 0

'''while contador < len(texto):
    print(texto[contador])
    contador += 1'''

'''for letra in texto:
    print(letra)'''

# for n in range(10):  # range(numero inicial, numero final, e a quantidade de vezes que vali pular)
#     print(n)

# for n in range(20, 10, -2):  #para decrescente se coloco o sinal de "-" no step.
#     print(n)

# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'python'
nova_str = ""

for letra in texto:
    if letra == 't':
        nova_str = nova_str + letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
    else:
        nova_str += letra
print(nova_str)
