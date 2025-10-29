import f_4Linha as f

def jogo():
    menu = {
        "1": "Novo Jogo",
        "2": "Carregar Jogo",
        "3": "Configurações",
        "4": "Sair"
    }

    for numero,texto in menu.items():
        print(f"{numero}. {texto}")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Iniciando um novo jogo...")
        
        while True:
        
            f.mostrar_tabuleiro()
            f.verificar_jogada("X")
            f.mostrar_tabuleiro()
            
            auxiliar = f.verificar_tabuleiro("X")
            if auxiliar == 100:
                break

            f.verificar_jogada("O")
            f.mostrar_tabuleiro()

            auxiliar = f.verificar_tabuleiro("O")
            if auxiliar == 100:
                break
            
    elif opcao == "2":
        print("Em Desenvolvimento...")
    elif opcao == "3":
        print("Em Desenvolvimento...")
    elif opcao == "4":
        print("Saindo do jogo...")
        exit()