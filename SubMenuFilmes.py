def verificaFilme (dc, codigoFilme):

    if(codigoFilme in dc):
        return True
    else:
        return False

def AdicionarFilme (dc):
    print('+--------+---------+---------+')
    print('Bem-Vindo ao Adicionar Filme!\n')

    codigoFilme = int(input("Digite o Código do Filme: "))
    existe = verificaFilme(dc, codigoFilme)

    if( existe == True):
        print('+--------+---------+---------+')
        print("Esse filme ja Existe!")
        print('+--------+---------+---------+')

    else:
        print('+--------+---------+---------+')
        print('Criando seu Filme!')
        
        nome = input('Digite o nome do Filme: ')
        ano = input('Digite o ano de lançamento (dd/MM/yyyy): ')
        genero = input('Digite o gênero do filme: ')
        atores = []

        opcao = 0

        while ( opcao != 2):
            print('+--------+---------+---------+--------+---------+---------+')
            print("Digite 1 (Adicionar um Ator) ou 2 (Parar de adicionar atores) ")
            opcao = int(input('Digite aqui: '))

            if(opcao == 1):
                nomes = input('Digite o nome do ator: ')

                atores.append(nomes)
                print('Adicionado com Sucesso!\n')

            else:
                print('Você Saiu!\n')

        dc[codigoFilme] = (nome , ano, genero, atores)
        print('+--------+---------+---------+')
        print('Filme adicionado com Sucesso !\n')
        print('+--------+---------+---------+')



def AlterarFilme (dc,codigoFilme):


    existe = verificaFilme(dc, codigoFilme)

    if(existe == True):

        resultado = input('Tem certeza que deseja alterar (SIM) ou (NAO)').upper()

        if(resultado == "SIM"):

            print('+--------+---------+---------+')
            nome = input('Digite o nome do Filme: ')
            ano = input('Digite o ano de lançamento (dd/MM/yyyy): ')
            genero = input('Digite o gênero do filme: ')
            atores = []

            opcao = 0

            while (opcao != 2):
                print("Digite 1 (Adicionar um Ator) ou 2 (Parar de adicionar atores) ")
                opcao = int(input('Digite aqui: '))

                if (opcao == 1):
                    nomes = input('Digite o nome do ator: ')

                    atores.append(nomes)
                    print('Adicionado com Sucesso!\n')

                else:
                    print('Você Saiu!\n')


            dc[codigoFilme] = (nome, ano, genero, atores)
            print('+--------+---------+---------+')
            print('Alterado com Sucesso!')
            print('+--------+---------+---------+')

        else:
            print('+--------+---------+---------+')
            print('Filme não Alterado!\n')
            print('+--------+---------+---------+')

    else:
        print('+--------+---------+---------+')
        print('Esse filme não existe!\n')
        print('+--------+---------+---------+')



def RemoverFilme(dc,codigoFilme):

    existe = verificaFilme(dc, codigoFilme)

    if (existe == True):

        resultado = input('Tem certeza que deseja alterar (SIM) ou (NAO)').upper()

        if (resultado == "SIM"):

            del dc[codigoFilme]
            print('+--------+---------+---------+')
            print('Filme removido com Sucesso!')
            print('+--------+---------+---------+')

        else:
            print('+--------+---------+---------+')
            print('Filme não Removido! \n')
            print('+--------+---------+---------+')

    else:
        print('+--------+---------+---------+')
        print('Esse filme não existe! \n')
        print('+--------+---------+---------+')


def MostrarTodosFilmes(dc):

    for chave in dc:
        tupla = dc[chave]
        atoress = ', '.join(tupla[3])

        print('+--------+---------+---------+')
        print(f"\nCódigo do Filme: {chave}")
        print(f"Nome do Filme: {tupla[0]}")
        print(f"Ano do Filme: {tupla[1]}")
        print(f"Gênero do Filme: {tupla[2]}")
        print(f"Atores do Filme: {atoress}\n")
        print('+--------+---------+---------+\n')

def MostrarFilme(dc,codigoFilme):

    existe = verificaFilme(dc,codigoFilme)

    if( existe == True):

        tupla = dc[codigoFilme]
        atoress = ','.join(tupla[3])

        print('+--------+---------+---------+')
        print(f"\nCódigo do Filme: {codigoFilme}")
        print(f"Nome do Filme: {tupla[0]}")
        print(f"Ano do Filme: {tupla[1]}")
        print(f"Gênero do Filme: {tupla[2]}")
        print(f"Atores do Filme: {atoress}\n")
        print('+--------+---------+---------+')
        

def GravaFilme(dc):

    arquivo = open ("Filme.txt", "w")

    for codigoFilme in dc:
        tupla = dc[codigoFilme]
        atoress = ', '.join(tupla[3])

        linha = f"\n {codigoFilme}; {tupla[0]}; {tupla[1]}; {tupla[2]}; {atoress} \n"
        print(linha)

        arquivo.write(linha)





#------------------------------PROGRAMA PRINCIPAL --------------------------------------#

def filmes (dicionario):

    opcao = 0

    while (opcao != 6):

        print('\n1- Adicionar Filme')
        print('2 - Alterar Filme')
        print('3 - Remover Filme')
        print('4 - Mostrar todos os Filmes')
        print('5 - Mostrar um Filme')
        print('6 - Sair do Menu')

        opcao = int(input('Digite a opção desejada: '))

        if(opcao == 1):
            AdicionarFilme(dicionario)

        elif(opcao == 2):
            codigoFilme = int(input('Digite o código do filme: \n'))
            AlterarFilme(dicionario,codigoFilme)


        elif(opcao == 3):
            codigoFilme = int(input('Digite o código do filme: \n'))
            RemoverFilme(dicionario,codigoFilme)


        elif (opcao == 4):
            MostrarTodosFilmes(dicionario)


        elif (opcao == 5):
            codigoFilme = int(input('Digite o código do filme: \n'))
            MostrarFilme(dicionario,codigoFilme)


        elif (opcao == 6):
            GravaFilme(dicionario)
            break

        else:
            print('Opção Inválida, Tente Novamente!\n')
