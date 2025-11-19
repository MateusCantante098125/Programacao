linha1 = [" ", " ", " "," "," "," "," "]
linha2 = [" ", " ", " "," "," "," "," "]
linha3 = [" ", " ", " "," "," "," "," "]
linha4 = [" ", " ", " "," "," "," "," "]
linha5 = [" ", " ", " "," "," "," "," "]
linha6 = [" ", " ", " "," "," "," "," "]
linha7 = [" ", " ", " "," "," "," "," "]
tabuleiro = [linha1, linha2, linha3, linha4, linha5, linha6, linha7]

def mostrar_tabuleiro():
    print()
    for i in range(7):
        for j in range(7):
            print(tabuleiro[i][j], end=" | ")
        print()
        print("-" * 28)
    print()

def verificar_jogada(arg):
    while True:
        try:
            jogador_primario_linha = int(input(f"Jogador {arg} escolha a linha (0 a 6): "))
            jogador_primario_coluna = int(input(f"Jogador {arg} escolha a coluna (0 a 6): "))
            if not (0 <= jogador_primario_linha <= 6 or 0 <= jogador_primario_coluna <= 6):
                raise ValueError("Fora do intervalo")
            break
        except ValueError:
            print("Entrada inválida. Introduza números inteiros entre 0 e 6.")
        
        if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " " :
            for jogador_primario_linha in range(6, -1, -1):  
                if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " ":
                    tabuleiro[jogador_primario_linha][jogador_primario_coluna] = arg
                    break
            break
        else:
            print("Posição já ocupada, escolha outra.")

def verificar_tabuleiro(arg):
    vitoria = False
    # Linhas
    for i in range(7):
        for j in range(4):
            if (tabuleiro[i][j] == arg and
                tabuleiro[i][j+1] == arg and
                tabuleiro[i][j+2] == arg and
                tabuleiro[i][j+3] == arg):
                vitoria = True
    
    # Colunas
    for i in range(4):
        for j in range(7):
            if (tabuleiro[i][j] == arg and
                tabuleiro[i+1][j] == arg and
                tabuleiro[i+2][j] == arg and
                tabuleiro[i+3][j] == arg):
                vitoria = True

    # Diagonais (1)
    for i in range(4):
        for j in range(4):
            if (tabuleiro[i][j] == arg and
                tabuleiro[i+1][j+1] == arg and
                tabuleiro[i+2][j+2] == arg and
                tabuleiro[i+3][j+3] == arg):
                vitoria = True

    # Diagonais (2)
    for i in range(4):
        for j in range(3, 7):
            if (tabuleiro[i][j] == arg and
                tabuleiro[i+1][j-1] == arg and
                tabuleiro[i+2][j-2] == arg and
                tabuleiro[i+3][j-3] == arg):
                vitoria = True

    # Vitória
    if vitoria:
        print()
        for i in range(7):
            for j in range(7):
                print(tabuleiro[i][j], end=" | ")
            print()
            print("-" * 28)
        print("\nJogador 1 venceu!\n")
        return 100

    # Empate
    cheio = True
    for i in range(7):
        for j in range(7):
            if tabuleiro[i][j] == " ":
                cheio = False

    if cheio:
        print("\nEmpate! O tabuleiro está cheio.\n")
        return 100
    
def jogo():
    menu = {
        "1": "Novo Jogo",
        "2": "Carregar Jogo",
        "3": "Configurações",
        "4": "Sair"
    }

    for numero,texto in menu.items():
        print(f"{numero}. {texto}")

    while True:
        try:
            opcao = input("Escolha uma opção: ").strip()
            if opcao not in menu:
                raise ValueError("Opção inválida")
            break
        except ValueError:
            print(f"Entrada inválida. Escolha uma das opções: {', '.join(menu.keys())}")

    if opcao == "1":
        print("Iniciando um novo jogo...")
        
        while True:
        
            mostrar_tabuleiro()
            verificar_jogada("X")
            mostrar_tabuleiro()
            
            auxiliar = verificar_tabuleiro("X")
            if auxiliar == 100:
                break

            verificar_jogada("O")
            mostrar_tabuleiro()

            auxiliar = verificar_tabuleiro("O")
            if auxiliar == 100:
                break
            
    elif opcao == "2":
        print("Em Desenvolvimento...")
    elif opcao == "3":
        print("Em Desenvolvimento...")
    elif opcao == "4":
        print("Saindo do jogo...")
        exit()