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
        jogador_primario_linha = int(input(f"Jogador {arg} escolha a linha (0 a 6): "))
        jogador_primario_coluna = int(input(f"Jogador {arg} escolha a coluna (0 a 6): "))
        
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