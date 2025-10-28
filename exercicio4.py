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
    
    linha1 = [" ", " ", " "]
    linha2 = [" ", " ", " "]
    linha3 = [" ", " ", " "]
    tabuleiro = [linha1, linha2, linha3]
    
    while True:
    
        print()
        for i in range(3):
            for j in range(3):
                print(tabuleiro[i][j], end=" | ")
            print()
            print("-" * 9)
        print()
        
        while True:
            jogador_primario_linha = int(input("Jogador 1, escolha a linha (0, 1 ou 2): "))
            jogador_primario_coluna = int(input("Jogador 1, escolha a coluna (0, 1 ou 2): "))
            
            if tabuleiro[jogador_primario_linha][jogador_primario_coluna] == " " :
                tabuleiro[jogador_primario_linha][jogador_primario_coluna] = "X"
                break
            else:
                print("Posição já ocupada, escolha outra.")
        
        print()
        for i in range(3):
            for j in range(3):
                print(tabuleiro[i][j], end=" | ")
            print()
            print("-" * 9)
        print()
        
        vitoria = False
        # Linhas
        for i in range(3):
            j = 0  
            if (tabuleiro[i][j] == "X" and
                tabuleiro[i][j+1] == "X" and
                tabuleiro[i][j+2] == "X" ):
                vitoria = True
        
        # Colunas
        for j in range(3):
            i=0
            if (tabuleiro[i][j] == "X" and
                tabuleiro[i+1][j] == "X" and
                tabuleiro[i+2][j] == "X" ):
                vitoria = True

        # Diagonais 
        
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X":
            vitoria = True
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X":
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
            break

        # Empate
        cheio = True
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    cheio = False

        if cheio:
            print("\nEmpate! O tabuleiro está cheio.\n")
            break
        
        
        while True:
            
            jogador_secundario_linha = int(input("Jogador 2, escolha a linha (0, 1 ou 2): "))
            jogador_secundario_coluna = int(input("Jogador 2, escolha a coluna (0, 1 ou 2): "))
            
            if tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] == " " :
                tabuleiro[jogador_secundario_linha][jogador_secundario_coluna] = "O"
                break
            else:
                print("Posição já ocupada, escolha outra.")

        print()
        for i in range(3):
            for j in range(3):
                print(tabuleiro[i][j], end=" | ")
            print()
            print("-" * 9)
        print()
        
        vitoria = False
        # Linhas
        for i in range(3):
            j = 0  
            if (tabuleiro[i][j] == "O" and
                tabuleiro[i][j+1] == "O" and
                tabuleiro[i][j+2] == "O" ):
                vitoria = True
        
        # Colunas
        for j in range(3):
            i=0
            if (tabuleiro[i][j] == "O" and
                tabuleiro[i+1][j] == "O" and
                tabuleiro[i+2][j] == "O" ):
                vitoria = True

        # Diagonais 
        
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O":
            vitoria = True
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O":
            vitoria = True

        # Vitória
        if vitoria:
            print()
            for i in range(3):
                for j in range(3):
                    print(tabuleiro[i][j], end=" | ")
                print()
                print("-" * 9)
            print("\nJogador 2 venceu!\n")
            break

        # Empate
        cheio = True
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    cheio = False

        if cheio:
            print("\nEmpate! O tabuleiro está cheio.\n")
            break
        
elif opcao == "2":
    print("Em Desenvolvimento...")
elif opcao == "3":
    print("Em Desenvolvimento...")
elif opcao == "4":
    print("Saindo do jogo...")
    exit()
    