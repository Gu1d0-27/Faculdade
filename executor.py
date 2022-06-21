from ast import While
from crud import MyCrud

banco = MyCrud()
banco.criarTabela()


#Opções de execução
while True: 
    print('''
    Escolha uma opção: 
    1 - inserir dados 
    2 - ler dados 
    3 - alterar dados 
    4 - deletar dados 
    5 - sair
    ''' )

    valor =input('->') 
          
    if valor == '1':
        nome = input ('Informe o seu nome? ')
        cpf = input ('Informe o seu CPF? ')
        
        banco.inserir(nome, cpf)

    elif valor == '2':
        resultados = banco.ler() 
        for resultado in resultados: 
            print (resultado[0], resultado[1], resultado[2])

    elif valor == '3':
        identificacao = int(input ('Informe o id que deseja alterar? ')) 
        nome = input ('Informe o seu nome? ') 
        cpf = input ('Informe o nome CPF? ') 
        banco.alterar(identificacao, nome, cpf)

    elif valor == '4':
        identificacao = int(input ('Informe o id que deseja deletar? '))
        banco.excluir(identificacao)

    else:
        break


banco.fechardB()
