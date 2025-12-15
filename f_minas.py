import random

tamanho = 5
num_minas = 5
tabuleiro_visivel = []
tabuleiro_interno = []

def criar_tabuleiros():
    global tabuleiro_visivel, tabuleiro_interno
    
    tabuleiro_visivel = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(" ")
        tabuleiro_visivel.append(linha)

    tabuleiro_interno = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        tabuleiro_interno.append(linha)
            
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        
        if tabuleiro_interno[linha][coluna] != 'M':
            tabuleiro_interno[linha][coluna] = 'M'
            minas_colocadas += 1
            
    for l in range(tamanho):
        for c in range(tamanho):
            if tabuleiro_interno[l][c] == 'M':
                continue 
            
            contador = 0
            for i in range(-1, 2):      
                for j in range(-1, 2):  
                    linha_vizinha = l + i
                    coluna_vizinha = c + j
                    
                    if 0 <= linha_vizinha < tamanho and 0 <= coluna_vizinha < tamanho:
                         if tabuleiro_interno[linha_vizinha][coluna_vizinha] == 'M':
                            contador += 1
            tabuleiro_interno[l][c] = str(contador)

def mostrar_tabuleiro():
    print("\n   0   1   2   3   4") 
    print("  " + "-" * 21)
    for i in range(tamanho):
        print(f"{i} |", end=" ")
        for j in range(tamanho):
            valor = tabuleiro_visivel[i][j]
            if valor == " ":
                print("?", end=" | ") 
            else:
                print(valor, end=" | ")
        print()
        print("  " + "-" * 21)
    print()

def verificar_jogada():
    while True:
        try:
            linha = int(input(f"Escolha a linha (0 a {tamanho-1}): "))
            coluna = int(input(f"Escolha a coluna (0 a {tamanho-1}): "))
            
            if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
                raise ValueError("Fora do intervalo")
            
            if tabuleiro_visivel[linha][coluna] != " ":
                print("Essa posição já foi revelada. Escolha outra.")
                continue
                
            break
        except ValueError:
            print(f"Entrada inválida. Introduza números entre 0 e {tamanho-1}.")

    conteudo = tabuleiro_interno[linha][coluna]
    
    if conteudo == 'M':
        print("\nBOOM! Acertaste numa mina!")
        tabuleiro_visivel[linha][coluna] = '*' 
        revelar_tudo()
        mostrar_tabuleiro()
        print("Game Over. Perdeste!\n")
        return False 
    else:
        tabuleiro_visivel[linha][coluna] = conteudo
        return True 

def revelar_tudo():
    for i in range(tamanho):
        for j in range(tamanho):
            tabuleiro_visivel[i][j] = tabuleiro_interno[i][j]

def verificar_vitoria():
    casas_fechadas = 0
    for i in range(tamanho):
        for j in range(tamanho):
             if tabuleiro_visivel[i][j] == " ":
                casas_fechadas += 1
    
    if casas_fechadas == num_minas:
        print("\nPARABÉNS! Encontraste todas as casas seguras!")
        revelar_tudo()
        mostrar_tabuleiro()
        return True
    return False

def jogo():
    menu = {
        "1": "Novo Jogo (Campo de Minas)",
        "2": "Instruções",
        "3": "Sair"
    }

    while True:
        print("\n--- MENU CAMPO DE MINAS ---")
        for numero, texto in menu.items():
            print(f"{numero}. {texto}")

        try:
            opcao = input("Escolha uma opção: ").strip()
        except:
            continue

        if opcao == "1":
            print("Iniciando Campo de Minas...")
            criar_tabuleiros()
            
            jogando = True
            while jogando:
                mostrar_tabuleiro()
                resultado_jogada = verificar_jogada()
                
                if resultado_jogada == False: 
                    jogando = False
                elif verificar_vitoria(): 
                    jogando = False
                    
        elif opcao == "2":
            print("\nINSTRUÇÕES:")
            print("- O tabuleiro é 5x5 e tem 5 minas escondidas.")
            print("- Escolhe linha e coluna para abrir uma casa.")
            print("- Se aparecer um número, indica quantas minas há à volta.")
            print("- Se aparecer 'M' (mina), perdes o jogo.")
            print("- Abre todas as casas sem minas para vencer.")
            
        elif opcao == "3":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")
