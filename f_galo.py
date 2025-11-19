linha1 = [" ", " ", " "]
linha2 = [" ", " ", " "]
linha3 = [" ", " ", " "]
tabuleiro = [linha1, linha2, linha3]

def mostrar_tabuleiro():
    print()
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end=" | ")
        print()
        print("-" * 9)
    print()

def verificar_jogada(arg):
    while True:
        try:
            jogador_primario_linha = int(input(f"Jogador {arg} escolha a linha (0, 1 ou 2): "))
            jogador_primario_coluna = int(input(f"Jogador {arg} escolha a coluna (0, 1 ou 2): "))
            if jogador_primario_linha not in [0, 1, 2] or jogador_primario_coluna not in [0, 1, 2]:
                raise ValueError("Linha e coluna devem ser 0, 1 ou 2.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")
        
        if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " " :
            tabuleiro[jogador_primario_linha][jogador_primario_coluna] = arg
            break
        else:
            print("Posição já ocupada, escolha outra.")

def verificar_tabuleiro(arg):
    vitoria = False
    # Linhas
    for i in range(3):
        j = 0  
        if (tabuleiro[i][j] == arg and
            tabuleiro[i][j+1] == arg and
            tabuleiro[i][j+2] == arg ):
            vitoria = True
    
    # Colunas
    for j in range(3):
        i=0
        if (tabuleiro[i][j] == arg and
            tabuleiro[i+1][j] == arg and
            tabuleiro[i+2][j] == arg ):
            vitoria = True

    # Diagonais 
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == arg:
        vitoria = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == arg:
        vitoria = True

    # Vitória
    if vitoria:
        print()
        for i in range(3):
            for j in range(3):
                print(tabuleiro[i][j], end=" | ")
            print()
            print("-" * 9)
        print("\nJogador 1 venceu!\n")
        return 100

    # Empate
    cheio = True
    for i in range(3):
        for j in range(3):
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
            opcao = input("Escolha uma opção: ")
            if opcao not in ["1", "2", "3", "4"]:
                raise ValueError("Opção inválida. Escolha 1, 2, 3 ou 4.")
            break
        except ValueError as e:
            print(e)

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