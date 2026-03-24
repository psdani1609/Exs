soma = 0
while True:
    n = int(input('>>> '))
    if n == 0:
        break
    soma += n
    print(f'Soma parcial {soma}')
    
print(f'A soma é {soma}')