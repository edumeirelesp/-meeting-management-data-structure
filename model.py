cadastro_sys = dict()

registro_cadastros_sys = list()

reuniao = dict()

todas_as_reunioes = list()

participante = dict()

participantes = list()

sala = dict()

sala["ocupada"] = "Não"

atas = dict()


def linha(tam=42):
    '''
    :param tam: ele recebe um valor pre determinado para o tamanho da linha, podendo ser alterado
    :return: retorna a linha de separação
    '''
    print("\33[32m-\33[m" * tam)


def retorno_de_erros(txt):
    linha(len(txt))
    print(f"\33[31m{txt.upper().strip()}\33[m")
    linha(len(txt))


def retorno_de_menus(txt):
    print(f"\33[32m{txt.upper().strip(): ^42}\33[m")


def print_apresentacoes(escreva):
    print(f" \33[35m{escreva.upper().strip():~^40}\33[m")
    print()


def visualizar_participantes():
    for i, j in enumerate(participantes):
        print(f'No indice [{i}], está cadastrado: {j}')
        linha()

        for k, v in j.items():
            print(f'{k}: \33[36m{v}\33[m')
        linha()


def visualizar_reunioes():
    """
    no lugar da lista todas_as_reunioes...
    se tiver banco de dados ou txt tem que...
     ver a quantia de lá e não da lista.
    :return: o retorno sera a visualização organizada da lista
    """
    if len(todas_as_reunioes) > 1:
        print(len(todas_as_reunioes))
        print_apresentacoes("todas as reuniões publicadas")

    else:
        print_apresentacoes("reunião publicada")

    for i in todas_as_reunioes:
        for k, v in i.items():
            print(f"{k}: \33[36m{v}\33[m")
        linha()


def visualizar_ata():
    print_apresentacoes("ata da reunião")
    retorno_de_menus("horarios, data e participantes")
    visualizar_reunioes()


def add_atas():
    qntia_de_atas = int(input("Quantas atas terá a reunião: "))
    for i in range(qntia_de_atas):
        atas[f"ata{i + 1}"] = str(input(f"Escreva a {i + 1}ª ata da reunião: ")).upper()

    reuniao["atas"] = atas


def alterar_presenca():
    presenca = str(input("Confirme sua presença na reunião [digite SIM ou NÂO]: ")).upper().strip()[0]
    if presenca == "N":
        indice = int(input("Digite qual participante quer alterar a presença (com o indice): "))
        participantes[indice]["presenca"] = "NAO"

    else:
        print_apresentacoes("permancencia na reunião confirmada!")


def cadastro():
    print_apresentacoes("Cadastro do sistema")

    cadastro_sys["login"] = str(input("Digite seu login: ")).upper().strip()
    cadastro_sys["senha"] = str(input("Digite sua senha: "))
    cadastro_sys["cpf"] = int(input("Digite o seu cpf: "))

    print_apresentacoes("escolha o acesso ao sistema")

    print("""    1 - Usuario comum
    2 - Gestor de recursos
    3 - Coordenador""")

    linha()

    while True:
        try:

            escolha = int(input("Qual a função do usuario no sistema: "))
            if escolha == 1:

                cadastro_sys["função:"] = "USUARIO COMUM"
                break
            elif escolha == 2:

                cadastro_sys["função:"] = "GESTOR DE RECURSOS"
                break
            elif escolha == 3:

                cadastro_sys["função:"] = "COORDENADOR"
                break
            else:

                retorno_de_erros("Escolha errada... digite novamente apenas 1, 2 ou 3.")
        except:
            retorno_de_erros("Escolha uma das opções existentes... 1, 2 ou 3!!")

    registro_cadastros_sys.append(cadastro_sys.copy())


def validacao_login():
    print_apresentacoes("Login do sistema")

    logando = False

    while not logando:

        loguin = str(input("Login: ")).upper().strip()
        senha = str(input("Senha: "))

        if loguin == cadastro_sys["login"]:

            if senha == cadastro_sys["senha"]:
                opcoes_todos()
                logando = True

            else:
                retorno_de_erros("Senha inexistente!!")
        else:
            retorno_de_erros("loguin inexistente!!")


def opcoes_todos():
    retorno_de_menus("""        Escolha a opção do sistema:

                                    1 - CRIAR REUNIAO
                                    2 - CONFIRMA OU NEGAR PRESENÇA 
                                    3 - VISUALIZAR AS REUNIÕES PUBLICADAS
                                    4 - VISUALIZAR AS REUNIÕES QUE JA FORAM CONFIRMADA SUA PRESESNÇA
                                    5 - VISUALIZAR ATAS DE REUNIÃO
                                    6 - EDITAR TODAS AS ATAS
                                    7 - REALOCAR REUNIÕES DE SALA
                                    8 - ADICIONAR PARTICIPANTE NA LISTA DE REUNIÃO
                                    9 - CONFIRMA LOCAL DE REUNIÃO
                                    10 - CADASTRAR NOVOS ESPAÇOS DE REUNIÃO
                                    """)

    opcao = int(input("Qual serviço do sistema deseja usa: "))
    if 1 <= opcao <= 10:
        if opcao == 1:
            criar_reuniao()

        elif opcao == 2:
            if not participantes:
                retorno_de_erros("não há participantes, você precisa criar uma reunião!")

            else:
                visualizar_participantes()
                alterar_presenca()

        elif opcao == 3:
            if not todas_as_reunioes:
                retorno_de_erros("não há reuniões publicadas!")

            else:
                visualizar_reunioes()

        elif opcao == 4:
            if not participantes:
                retorno_de_erros("não há participantes, você precisa criar uma reunião!")

            else:
                cpf = int(input("Digite seu cpf para verificar se áh reunião confirmada: "))
                for i in participantes:
                    for v in i.values():
                        if cpf == v:
                            visualizar_reunioes()
                        else:
                            retorno_de_erros("você não está na reunião!")
                            break

        elif opcao == 5:
            if not participantes:
                retorno_de_erros("não há dados!!")

            else:
                visualizar_ata()

        else:
            if cadastro_sys["função:"] == "COORDENADOR":
                opcoes_adicionais_coordenador(opcao)

            elif cadastro_sys["função:"] == "GESTOR DE RECURSOS":
                opcoes_adicionais_gestor(opcao)

            else:
                retorno_de_erros("Opção invalida!!")
    else:
        retorno_de_erros("digite apenas números entre 1 a 10!!")


def opcoes_adicionais_coordenador(opcao):
    if opcao == 6:
        visualizar_ata()
        print_apresentacoes("editar atas!")
        add_atas()

    elif opcao == 7:
        print_apresentacoes("realocar reunião!")
        cadastro_de_sala()

    elif opcao == 8:
        print_apresentacoes("adicionar mais participante!")
        add_participantes()

    else:
        retorno_de_erros("digite opções direcionada a coodenador!")


def opcoes_adicionais_gestor(opcao):
    if opcao == 9:
        print_apresentacoes("confirmar local de reunião!")
        visualizar_reunioes()

    elif opcao == 10:
        print_apresentacoes("cadastrar novos espaços de reunião!")
        criar_reuniao()

    else:
        retorno_de_erros("digite opções direcionada a gestor!")


def cadastro_de_sala():
    print_apresentacoes("Cadastrando Sala")

    retorno_de_menus("""Temos 3 Salas para reuniões, escolha a desocupada!!
    1 - Sala 01
    2 - Sala 02
    3 - Sala 03""")

    while True:

        try:

            escolha_sala = int(input("Digite qual sala deseja: "))

            if escolha_sala == 1:

                sala["sala"] = "Sala 01"
                sala["ocupada"] = "Sim"
                break
            elif escolha_sala == 2:

                sala["sala"] = "Sala 02"
                sala["ocupada"] = "Sim"
                break
            elif escolha_sala == 3:

                sala["sala"] = "Sala 03"
                sala["ocupada"] = "Sim"
                break
            else:

                retorno_de_erros("Escolha errada... digite novamente apenas 1, 2 ou 3.")
        except:

            retorno_de_erros("digite apenas números validos!!")


def add_participantes():
    print_apresentacoes("Participante")

    participante["nome"] = (str(input("Digite o nome do participante: ")).strip().upper())

    idade = str(input("Digite a idade do participante: "))
    while True:

        if idade.isnumeric():
            participante["idade"] = idade
            break
        idade = str(input("Digite apenas numeros referente a idade: "))

    participante["profissao"] = str(input("Digite sua profissão: ")).strip().upper()

    participante["presenca"] = str(input("Confirma presença na reunião? [SIM/NÃO]: ")).upper().strip()

    participante["cpf"] = int(input("Digite seu cpf: "))

    participantes.append(participante.copy())


def criar_reuniao():
    todas_as_reunioes.clear()

    print_apresentacoes("CRIANDO REUNIÃO")

    while True:

        try:

            qntos_participantes = int(input("Digite quantos participantes adicionar: "))
            break
        except:

            retorno_de_erros("digite apenas números!!")
    for i in range(qntos_participantes):
        add_participantes()

    cadastro_de_sala()

    reuniao["horario inicio"] = str(input("Digite o horario inicial: "))

    reuniao["horario final"] = str(input("Digite o horario final: "))

    reuniao["data"] = str(input("Data da reunião: "))

    reuniao["local"] = sala

    add_atas()

    reuniao["participantes"] = participantes

    todas_as_reunioes.append(reuniao.copy())
    # depois de criado os dados manda para um local de armazenamento txt ou um banco de dados

