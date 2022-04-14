#indicadores
#0123456..................33

frase = "o rato roeu a roupa do rei de roma"  #iterável
tamanho_frase = len(frase)
contador = 0
nova_str = ''
input_do_usuario = input('Qual letra deseja por em maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_str += input_do_usuario.upper()
    else:
        nova_str += letra
    contador += 1
print(nova_str)
