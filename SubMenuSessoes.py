from SubMenuSalas import*
from SubMenuFilmes import*
from Auxiliar import*
from datetime import*

#---------------------------------------------------------------------#
def verificaSessao(dc,chave):

    if ( chave in dc):
        return True

    else:
        return False

#---------------------------------------------------------------------#

def AdicionarSessao (dc,dcSala,dcFilme):
    print('Bem-Vindo a Sessões!\n')

    codigoFilme = int(input('Digite o código do Filme ja criado: '))
    existe1 = verificaFilme(dcFilme, codigoFilme)

    codigoSala = int(input('Digite o código da Sala ja criada: '))
    existe2 = verificaSala(dcSala, codigoSala)


    if ( existe1 == True and existe2 == True):

        print('Criando Sessão!\n')

        codigoSessao = input("Digite o código da Sessão: ")
        codigoSal = codigoSala
        codigoFil = codigoFilme
        Data = input('Digite a data da Sessão ( dd/MM/yyyy): ')
        Horario = input('Digite o horario da Sessão ( HH:mm ): ')

        chave = (codigoSessao , codigoFil, codigoSal, Data, Horario )

        existe = verificaSessao(dc, chave)

        if(existe == True):
            print('+--------+--------+--------+--------+--------+')
            print('Essa Sala/Filme ainda não existe!')
            print('Necessário primeiro criar uma Sala e depois um Filme para criar uma Sessão! \n')
            print('+--------+--------+--------+--------+--------+')


        else:
            precoIngresso = float(input("Digite o preço do Ingresso: "))
            dc[chave]= precoIngresso

            print('+--------+--------+--------+--------+--------+')
            print('Sessão adicionada com Sucesso !\n')
            print('+--------+--------+--------+--------+--------+')



def AlterarSessao(dc,dcSala, dcFilme):

    print('Bem-Vindo a Alterar Sessão!\n')

    codigoFilme = int(input('Digite o código do Filme ja criado: '))
    existe1 = verificaFilme(dcFilme, codigoFilme)

    codigoSala = int(input('Digite o código da Sala ja criada: '))
    existe2 = verificaSala(dcSala, codigoSala)

    if (existe1 == True and existe2 == True):

        print('Alterando Sessão!\n')

        print('+--------+--------+--------+--------+--------+')
        codigoSessao = input("Digite o código da Sessão: ")
        codigoSal = codigoSala
        codigoFil = codigoFilme
        Data = input('Digite a data da Sessão ( dd/MM/yyyy): ')
        Horario = input('Digite o horario da Sessão ( HH:mm ): ')

        chave = (codigoSessao, codigoFil, codigoSal, Data, Horario)

        existe = verificaSessao(dc, chave)


        if (existe == True):
            print('+--------+--------+--------+--------+--------+')

            escolha = input('Deseja mesmo Alterar essa Sessão ? (SIM) ou (NÃO): ').upper()
            print('+--------+--------+--------+--------+--------+')
            
            if (escolha == 'SIM'):
                precoIngresso = float(input("Digite o preço do Ingresso: "))
                dc[chave] = precoIngresso
                print('+--------+--------+--------+--------+--------+')
                print('Sessão Altera com Sucesso! \n')
                print('+--------+--------+--------+--------+--------+')


            else:
                print('+--------+--------+--------+--------+--------+')
                print('Sessão não Alterada!\n')
                print('+--------+--------+--------+--------+--------+')

        else:
            print('+--------+--------+--------+--------+--------+')
            print('Essa Sala/Filme ainda não existe!')
            print('Necessário primeiro criar uma Sala e depois um Filme para criar uma Sessão! \n')
            print('+--------+--------+--------+--------+--------+')

def RemoverSessao(dc,dcFilme,dcSala):

    print('Bem-Vindo a Remover Sessão!\n')

    codigoFilme = int(input('Digite o código do Filme ja criado: '))
    existe1 = verificaFilme(dcFilme, codigoFilme)

    codigoSala = int(input('Digite o código da Sala ja criada: '))
    existe2 = verificaSala(dcSala, codigoSala)

    if (existe1 == True and existe2 == True):
        codigoSessao = input("Digite o código da Sessão: ")
        codigoSal = codigoSala
        codigoFil = codigoFilme
        Data = input('Digite a data da Sessão ( dd/MM/yyyy): ')
        Horario = input('Digite o horario da Sessão ( HH:mm ): ')

        chave = (codigoSessao, codigoFil, codigoSal, Data, Horario)

        existe = verificaSessao(dc, chave)

        if (existe == True):
            print('+--------+--------+--------+--------+--------+')
            escolha = input('Deseja mesmo remover a Sessão ? (SIM) ou (NÃO): ').upper()
            print('+--------+--------+--------+--------+--------+')
            
            if (escolha == 'SIM'):
                del dc[chave]
                print('+--------+--------+--------+--------+--------+')
                print('Sessão Removida com Sucesso! \n')
                print('+--------+--------+--------+--------+--------+')


            else:
                print('+--------+--------+--------+--------+--------+')
                print('Sessão não Removida!\n')
                print('+--------+--------+--------+--------+--------+')

        else:
            print('+--------+--------+--------+--------+--------+')
            print('Essa Sala/Filme ainda não existe!')
            print('Necessário primeiro criar uma Sala e depois um Filme para criar uma Sessão! \n')
            print('+--------+--------+--------+--------+--------+')
    

def MostrarTodasSessoes(dc,dcSala, dcFilme):
    for chave in dc:
        codigoSessao = chave[0]
        tupla = chave[1]
        tupla2 = chave[2]
        tupla3 = chave[3]
        tupla4 = chave[4]

        junta = (codigoSessao, tupla, tupla2, tupla3, tupla4)
        valor = dc[junta]

        print('\nDados da Sala:')
        MostrarSala(dcSala,tupla2)

        print('Dados do Filme:')
        MostrarFilme(dcFilme,tupla)

        print('\nDados da Sessão:')
        print('+--------+--------+--------+--------+--------+')
        print(f'Código da Sessão: {codigoSessao}')
        print(f'Data da Sessão: {tupla3}')
        print(f'Horario da Sessão: {tupla4}')
        print(f'Valor do ingresso: {dc[junta]}')
        print('+--------+--------+--------+--------+--------+')

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

def MostrarSessao(dc,dcSala, dcFilme,codigoFilme,codigoSala,codigoSessao,Data,Horario):

    chave = (codigoSessao, codigoFilme, codigoSala, Data, Horario)
    existe = verificaSessao(dc, chave)


    if(existe == True):

        print('\nDados da Sala:')
        MostrarSala(dcSala,codigoSala)

        print('Dados do Filme:')
        MostrarFilme(dcFilme,codigoFilme)

        print('Dados da Sessão:')
        print('+--------+--------+--------+--------+--------+')
        print('Dados da Sessão:')
        print(f'Data da Sessão: {Data}')
        print(f'Horario da Sessão: {Horario}')
        print(f'Valor do ingresso: {dc[chave]}')
        print('+--------+--------+--------+--------+--------+')

    else:
        print('Essa Sessão nao Existe !,')
        print('Neccesário cria-la primeiro!')


def GravaSessao(dc):

    arquivo = open('Sessao.txt', 'w')

    for chave in dc:
        codigoSessao = chave[0]
        tupla = chave[1]
        tupla2 = chave[2]
        tupla3 = chave[3]
        tupla4 = chave[4]

        junta = (codigoSessao , tupla, tupla2, tupla3, tupla4)
        valor = dc[junta]

        linha = f'{codigoSessao}; {tupla}; {tupla2}; {tupla3}; {tupla4}; {valor}\n'

        arquivo.write(linha)


#-------------------------------------------RELATÓRIO --------------------------------------------------#

def relatorio (dc,dcSala,dcFilme,x,y):

    for chave in dc:
        tupla = chave[0]
        tupla2 = chave[1]
        tupla3 = chave[2]
        tupla4 = chave[3]
        tupla5 = chave[4]

        dataIn = datetime.strptime(tupla4,'%d/%m/%Y')

        if(dataIn >= x and dataIn <=y ):
            MostrarSessao(dc,dcSala,dcFilme, tupla2, tupla3, tupla, tupla4, tupla5)


#-----------------------------------------PROGRAMA PRINCIPAL -------------------------------------------#
def sessoes (dicionario,dicionarioSala,dicionarioFilmes):

    opcao = 0

    while (opcao != 6):

        print('\n1- Adicionar Sessão')
        print('2 - Alterar Sessão')
        print('3 - Remover Sessão')
        print('4 - Mostrar todas as Sessões')
        print('5 - Mostrar uma Sessão')
        print('6 - Sair do Menu')

        opcao = int(input('Digite a opção desejada: '))

        if(opcao == 1):
            AdicionarSessao(dicionario, dicionarioSala, dicionarioFilmes)


        elif(opcao == 2):
            AlterarSessao(dicionario,dicionarioSala,dicionarioFilmes)


        elif(opcao == 3):
            RemoverSessao(dicionario,dicionarioSala,dicionarioFilmes)


        elif (opcao == 4):
            MostrarTodasSessoes(dicionario,dicionarioSala,dicionarioFilmes)


        elif (opcao == 5):
            codigoFilme = int(input('Digite o código do Filme ja criado: '))
            codigoSala = int(input('Digite o código da Sala ja criada: '))
            codigoSessao = input("Digite o código da Sessão: ")
            Data = input('Digite a data da Sessão ( dd/MM/yyyy): ')
            Horario = input('Digite o horario da Sessão ( HH:mm ): ')
            MostrarSessao(dicionario,dicionarioSala,dicionarioFilmes,codigoFilme,codigoSala,codigoSessao,Data,Horario)


        elif (opcao == 6):
            GravaSessao(dicionario)
            break



        
