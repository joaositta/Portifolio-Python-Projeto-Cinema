from SubMenuSalas import*
from SubMenuFilmes import*
from SubMenuSessoes import*
from datetime import*


DicionarioSala = {}
DicionarioFilmes = {}
DicionarioSessoes = {}
#------------------------------------------------------------------------------------------------------------#

opcaoMenu = 0

while (opcaoMenu != 5):

    print("\nBem-Vindo ao Cinema Cine Sitta's ")

    print('Menu de Opções:')
    print('1 - Submenu de Salas')
    print('2 - Submenu de Filmes')
    print('3 - Submenu de Sessões')
    print('4 - Relatório')
    print('5 - Sair')

    opcaoMenu = int(input("Digite a opção Desejada: "))
    #----------------------------------------------------------------------------------------------------------------#

    if(opcaoMenu == 1):
        salas(DicionarioSala)

    elif(opcaoMenu == 2):
        filmes(DicionarioFilmes)

    elif(opcaoMenu == 3):
        sessoes(DicionarioSessoes, DicionarioSala, DicionarioFilmes)

    elif(opcaoMenu == 4):
        x = input("Digite uma Data Inicial (dd/MM/yyyy): ")
        dataInicial= datetime.strptime(x,'%d/%m/%Y')
        y = input("Digite uma Data Final (dd/MM/yyyy): ")
        dataFinal= datetime.strptime(y,'%d/%m/%Y')

        relatorio(DicionarioSessoes, DicionarioSala, DicionarioFilmes,dataInicial,dataFinal)

        

    elif(opcaoMenu == 5):
        break

    else:
        print(" \n Opção Inválida, Tente Novamente! \n ")
        continue
