import random

# Variáveis globais
tabuleiro_visivel = []
tabuleiro_oculto = []
navios_restantes = 0

def criar_tabuleiros():
    global tabuleiro_visivel, tabuleiro_oculto, navios_restantes
    
    tabuleiro_visivel = []
    tabuleiro_oculto = []
    
    # Cria tabuleiro 7x7
    for i in range(7):
        linha_v = ["~"] * 7 
        linha_o = [" "] * 7
        tabuleiro_visivel.append(linha_v)
        tabuleiro_oculto.append(linha_o)
    
    navios_colocados = 0
    while navios_colocados < 5:
        linha = random.randint(0, 6)
        coluna = random.randint(0, 6)
        
        if tabuleiro_oculto[linha][coluna] == " ":
            tabuleiro_oculto[linha][coluna] = "N"
            navios_colocados += 1
            
    navios_restantes = 5

def mostrar_tabuleiro():
    print("\n   0   1   2   3   4   5   6")
    print("  ---------------------------")
    for i in range(7):
        print(f"{i} |", end=" ")
        for j in range(7):
            print(tabuleiro_visivel[i][j], end=" | ")
        print()
        print("  ---------------------------")
    print(f"\nNavios restantes: {navios_restantes}\n")

def realizar_jogada():
    global navios_restantes
    
    while True:
        try:
            linha = int(input("Escolha a linha do tiro (0 a 6): "))
            coluna = int(input("Escolha a coluna do tiro (0 a 6): "))
            
            if not (0 <= linha <= 6 and 0 <= coluna <= 6):
                raise ValueError("Fora do intervalo")
            
            if tabuleiro_visivel[linha][coluna] != "~":
                print("Já disparaste para aqui! Tenta outra posição.")
                continue
                
            break
        except ValueError:
            print("Entrada inválida. Introduza números inteiros entre 0 e 6.")

    if tabuleiro_oculto[linha][coluna] == "N":
        print("\n*** FOGO! Acertaste num navio! ***")
        tabuleiro_visivel[linha][coluna] = "X"
        navios_restantes -= 1
    else:
        print("\n--- Água! Falhaste o alvo. ---")
        tabuleiro_visivel[linha][coluna] = "O"

def jogo():
    menu = {"1": "Novo Jogo", "2": "Instruções", "3": "Sair"}

    print("\n=== BATALHA NAVAL ===")
    for numero, texto in menu.items():
        print(f"{numero}. {texto}")

    while True:
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            if opcao not in menu:
                raise ValueError("Opção inválida")
            break
        except ValueError:
            print(f"Entrada inválida. Escolha: {', '.join(menu.keys())}")

    if opcao == "1":
        print("A preparar os navios...")
        criar_tabuleiros()
        tentativas = 0
        
        while navios_restantes > 0:
            mostrar_tabuleiro()
            realizar_jogada()
            tentativas += 1
            
        mostrar_tabuleiro()
        print(f"\nPARABÉNS! Afundaste todos os navios em {tentativas} tentativas!")
        
    elif opcao == "2":
        print("\n--- INSTRUÇÕES ---")
        print("1. Existem 5 navios escondidos no tabuleiro 7x7.")
        print("2. Escolhe as coordenadas (linha e coluna) para disparar.")
        print("3. 'X' significa que acertaste, 'O' significa água.")
        print("4. Tenta afundar todos com o menor número de tiros!")
        jogo() 
        
    elif opcao == "3":
        print("A sair do jogo...")
        exit()
