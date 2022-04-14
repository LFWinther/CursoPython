# isnumeric isdigit isdecimal

num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')



try: #tenta
    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
except:
    print('ERROR')
