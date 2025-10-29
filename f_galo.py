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
        jogador_primario_linha = int(input(f"Jogador {arg} escolha a linha (0, 1 ou 2): "))
        jogador_primario_coluna = int(input(f"Jogador {arg} escolha a coluna (0, 1 ou 2): "))
        
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

    # Empate
    cheio = True
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                cheio = False

    if cheio:
        return print("\nEmpate! O tabuleiro está cheio.\n")
        
   