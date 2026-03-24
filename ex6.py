soma = 0
cont = 0
while True:
    n = int(input('>>> '))
    if n == 0:
        break
    soma = soma + n
    cont = cont + 1
    
if cont <= 0:
    print('Não temos média')
else:
    print(f'A média é {soma / cont}')