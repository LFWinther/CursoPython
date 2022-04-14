''' While / else
contadores
acumuladores
'''

contador = 1
acumulador = 1

'''while contador <= 10:
    print(contador)
    contador += 1'''

'''while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('FIM')'''

#se algo impedir que o código chegue ao "else", ele nãos erá executado.
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('else')
print('isso não está no "else"')