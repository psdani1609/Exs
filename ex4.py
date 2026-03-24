try:
    
    opc = int(input('>>>'))
    match opc:
       case 1:
        print('Cadastrar')
       case 2:
        print('Alterar')
       case 3:
        print('Excluir')
       case 4:
        print('Sair')
       case _:
        print('Valor Errado')
except:
    print("Digita direito ai")
        