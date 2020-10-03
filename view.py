from projetoprimario import model


def main():

    sair = ""

    model.cadastro()
    model.validacao_login()

    while 'S' not in sair:

        sair = str(input("Deseja sair do sistema ? apenas[sim/não]:")).strip().upper()[0]

        if sair == "S":

            model.print_apresentacoes("saindo do sistema... Obrigado pelo uso!")
        else:
            model.print_apresentacoes("voltando para o loguin!")
            model.validacao_login()


main()
