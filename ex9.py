def VerificarNumero(x: float):
    return 'Par' if x % 2 == 0 else 'Impar'

num = int(input('>>> '))
retorno = VerificarNumero(num)
print(retorno)
print(VerificarNumero (15))
print(VerificarNumero (150))
print(VerificarNumero (1505))