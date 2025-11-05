from random import randint

linha1 = ["00","01","02","03","04","05","06","07","08","09"]
linha2 = ["10","11","12","13","14","15","16","17","18","19"]
linha3 = ["20","21","22","23","24","25","26","27","28","29"]
linha4 = ["30","31","32","33","34","35","36","37","38","39"]
linha5 = ["40","41","42","43","44","45","46","47","48","49"]
tabuleiro = [linha1, linha2, linha3, linha4, linha5]

def mostrar_tabuleiro():
    print()
    for i in range(5):
        for j in range(10):
            print(tabuleiro[i][j], end=" | ")
        print()
        print("-" * 49)
    print()

def lancar_dado():
    return randint(1, 6)

def aplicar_casas_especiais(posicao,jogador):
    sem_jogar = 0
    auxiliar = posicao
    casas_malditas = [12,17,23,28,34,42]
    
    if posicao%3 == 0:
        valor_subtrair= randint(1,4)
        print(f"Casa {posicao} é amaldiçoada , o jogador {jogador} retrocedeu {valor_subtrair} casas .")
        posicao -= valor_subtrair

        if posicao <0:
            posicao = 0

        linha = auxiliar // 10
        coluna = (auxiliar % 10)-1

        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
        
        tabuleiro[linha][coluna] = auxiliar

        linha = posicao // 10
        coluna = (posicao % 10)-1

        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
        
        tabuleiro[linha][coluna] = jogador
        return posicao,sem_jogar

    elif posicao%5 == 0:
        valor_adicionar= randint(1,4)
        print(f"Casa {posicao} é abençoada , o jogador {jogador} avançou {valor_adicionar} casas .")
        posicao += valor_adicionar

        if posicao <0:
            posicao = 0

        linha = auxiliar // 10
        coluna = (auxiliar % 10)-1
        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
            
        tabuleiro[linha][coluna] = auxiliar

        linha = posicao // 10
        coluna = (posicao % 10)-1
        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
        
        tabuleiro[linha][coluna] = jogador
        return posicao,sem_jogar

    elif posicao in casas_malditas:
        valor = randint(1,3)
        sem_jogar = valor
        print(f"A casa {posicao} é maldita o jogador {jogador} fica {sem_jogar} vezes sem jogar .")
        linha = auxiliar // 10
        coluna = (auxiliar % 10)-1
        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
            
        tabuleiro[linha][coluna] = auxiliar

        linha = posicao // 10
        coluna = (posicao % 10)-1
        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
        
        tabuleiro[linha][coluna] = jogador
        return posicao,sem_jogar
    
    else:
        
        for i in range(5):
            for j in range(10):
                if tabuleiro[i][j] == jogador and j>0:
                    tabuleiro[i][j] = (i*10) + (j+1)
                else:
                    if tabuleiro[i][j] == jogador and j==0:
                        tabuleiro[i][j] = (i*10) + j
                  
        linha = posicao // 10
        coluna = (posicao % 10)-1
        if linha < 0:
            linha = 0
        elif coluna < 0:
            coluna = 0
        
        tabuleiro[linha][coluna] = jogador
        return posicao,sem_jogar

def verificar_vitoria(posicao, jogador):
    if posicao >= 49:
        print(f"\n🎉 Jogador {jogador} venceu o Jogo da Glória! 🎉\n")
        return True
    return False

def jogo():
    while True:
        try: 
            jogador_1 = input("Introduza a peça que deseja usar (A-Z): ").upper()
            jogador_2 = input("Introduza a peça que deseja usar (A-Z): ").upper()
            
            if jogador_1 == jogador_2:
                print("As peças não podem ser iguais. Tente novamente.")
                continue
            else: 
                break

        except ValueError: 
            print("Apenas caracteres de A-Z são válidos.")
    
    jogador_1_pos = -1
    jogador_2_pos = -1
    sem_jogar_1 = 0
    sem_jogar_2 = 0

    while True:

        if sem_jogar_1 == 0:
            input(f"\n{jogador_1}, pressione ENTER para lançar o dado.")
            jogador_1_pos += lancar_dado()
            jogador_1_pos, sem_jogar_1 = aplicar_casas_especiais(jogador_1_pos, jogador_1)
            if verificar_vitoria(jogador_1_pos, jogador_1):
                break
            else:
                print(f"{jogador_1} está agora na posição {jogador_1_pos}.")
        else:
            print(f"{jogador_1} perde esta rodada ({sem_jogar_1} restantes).")
            sem_jogar_1 -= 1

        if sem_jogar_2 == 0:
            input(f"\n{jogador_2}, pressione ENTER para lançar o dado.")
            jogador_2_pos += lancar_dado()
            jogador_2_pos, sem_jogar_2 = aplicar_casas_especiais(jogador_2_pos, jogador_2)
            if verificar_vitoria(jogador_2_pos, jogador_2):
                break
            else:
                print(f"{jogador_2} está agora na posição {jogador_2_pos}.")
        else:
            print(f"{jogador_2} perde esta rodada ({sem_jogar_2} restantes).")
            sem_jogar_2 -= 1

        mostrar_tabuleiro()