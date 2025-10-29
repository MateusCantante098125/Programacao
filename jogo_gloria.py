import f_gloria as f

def jogo():
    menu = {
        "1": "Novo Jogo",
        "2": "Carregar Jogo",
        "3": "Configurações",
        "4": "Sair"
    }

    for numero, texto in menu.items():
        print(f"{numero}. {texto}")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Iniciando um novo jogo da Glória...\n")
        f.iniciar_jogo()

    elif opcao == "2":
        print("Em Desenvolvimento...")

    elif opcao == "3":
        print("Em Desenvolvimento...")

    elif opcao == "4":
        print("Saindo do jogo...")
        exit()
