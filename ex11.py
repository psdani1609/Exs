def ValidarFrase(texto):
    return texto != ''

arq = open('dados.txt', 'w', encoding='utf-8')

while True:
    frase = input('Digite a frase: ')
    if frase.lower() == 'sair':
        break
    
    if not ValidarFrase(frase):
        print('Frase errada')
        continue
    
    arq.write(frase + '\n')
    
    arq.close()