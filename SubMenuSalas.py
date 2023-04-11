from Auxiliar import*


#---------------------------------------------------------------------------------------#
def verificaSala(dicionario, codigoSala):

    if ( codigoSala in dicionario ):
        return True

    else:
        return False

def AdicionarSala(dc):
    print('+--------+--------+--------+')
    print('Bem-Vindo a SALAS:\n')

    codigoSala = int(input('Digite o código da Sala: '))
    existe = verificaSala( dc , codigoSala)

    if(existe == True):
        print('+--------+--------+--------+')
        print('\nEssa Sala ja Existe! \n ')
        print('+--------+--------+--------+')

    else:
        print('+--------+--------+--------+')
        print("\nCriando sua Sala! \n")

        nome= input("Digite o nome da Sala: ")
        capacidade= int(input("Digite a capacidade: "))
        tipoExibicao = input("Digite o tipo de Exibição: ")
        acessibilidade= input("Digite informações sobre Acessibilidade: ")

        dc[codigoSala]= (nome, capacidade, tipoExibicao, acessibilidade)

        print('-------------+------------+---------+')
        print('\nSala Adicionada com Sucesso! \n')
        print('-------------+------------+---------+')



def AlterarSala(dc,codigoSala):

    print('Bem-Vindo a Alterar Sala!\n')

    existe = verificaSala(dc , codigoSala)

    if(existe == True):
        print('Alterando Sala!\n')
        
        nome = input("Digite o nome da Sala: ")
        capacidade = int(input("Digite a capacidade: "))
        tipoExibicao = input("Digite o tipo de Exibição: ")
        acessibilidade = input("Digite informações sobre Acessibilidade: ")

        dc[codigoSala] = (nome, capacidade, tipoExibicao, acessibilidade)

        print('+--------+--------+--------+')
        print('\nSala Alterada com Sucesso!\n')
        print('+--------+--------+--------+')

    else:
        print('+--------+--------+--------+')
        print('Essa Sala não existe, você precisa cria-la primeiro!')
        print('+--------+--------+--------+')


def RemoverSala(dc,codigoSala):

    print('Bem-Vindo a Remover Sala!\n')

    existe = verificaSala(dc, codigoSala)

    if(existe == True):
        print(f'Deseja mesmo Remover a sala {codigoSala} ?')
        resposta = input('Digite Aqui. (SIM) (NÃO): ').upper()

        if(resposta == "SIM"):
            del dc[codigoSala]
            print('+--------+--------+--------+')
            print('Removido com Sucesso!\n')
            print('+--------+--------+--------+')

        else:
            print('+--------+--------+--------+')
            print('Remoção Não Efetuada!\n')
            print('+--------+--------+--------+')
    else:
        print('+--------+--------+--------+')
        print('Não existe essa Sala, Volte ao Menu!\n')
        print('+--------+--------+--------+')



def MostrarTodasSalas(dc):
     for chave in dc:
         tupla = dc[chave]
         print('\n--------------------------------------')
         print(f"Código da Sala: {chave}")
         print(f"Nome da Sala: {tupla[0]}")
         print(f"Capacidade da Sala {tupla[1]}")
         print(f"Tipo de Exibição da Sala {tupla[2]}")
         print(f"Acessibilidade da Sala {tupla[3]}\n")
         print('--------------------------------------\n')
         


def MostrarSala(dc,codigoSala):

    existe = verificaSala(dc, codigoSala)

    if(existe == True):

        tupla = dc[codigoSala]
        print('\n--------------------------------------')
        print(f"\nCódigo da Sala: {codigoSala}")
        print(f"Nome da Sala: {tupla[0]}")
        print(f"Capacidade da Sala: {tupla[1]}")
        print(f"Tipo de Exibição da Sala: {tupla[2]}")
        print(f"Acessibilidade da Sala: {tupla[3]}\n")
        print('--------------------------------------')



    else:
        print('Não existe nenhuma Sala! ')


def GravaSala(dc):
    arquivo = open("Salas.txt", "w")

    for codigoSala in dc:
        tupla = dc[codigoSala]
        linha = f" {codigoSala}; {tupla[0]}; {tupla[1]}; {tupla[2]}; {tupla[3]}\n"

        arquivo.write(linha)






#-----------------------------------Programa Principal Salas ---------------------------#
def salas (dicionario):

    opcao = 0

    while (opcao != 6):

        print('\n1- Adicionar Sala')
        print('2 - Alterar Sala')
        print('3 - Remover Sala')
        print('4 - Mostrar todas as Salas')
        print('5 - Mostrar uam Sala')
        print('6 - Sair do Menu')

        opcao = int(input('Digite a opção desejada: '))

        if(opcao == 1):
            AdicionarSala(dicionario)

        elif(opcao == 2):
            print('\nVocê entrou em Alterar Sala\n')
            codigoSala = int(input(" Digite o código para alterar: "))

            AlterarSala(dicionario,codigoSala)

        elif(opcao == 3):
            print('\nBem-Vindo ao Remover Sala')
            codigoSala = int(input('Digite o código da sala: '))
            RemoverSala(dicionario,codigoSala)

        elif (opcao == 4):
            MostrarTodasSalas(dicionario)

        elif (opcao == 5):
            codigoSala = int(input('Digite o código da sala: '))
            MostrarSala(dicionario,codigoSala)

        elif (opcao == 6):
            GravaSala(dicionario)
            break



