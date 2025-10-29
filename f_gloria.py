import random
import time

# Configuração básica
NUM_CASAS = 30
jogadores = ["X", "O"]
posicoes = {"X": 0, "O": 0}
perde_turno = {"X": False, "O": False}

casas_especiais = {
    5: 3,    # Avança 3 casas
    10: -2,  # Volta 2 casas
    15: 5,   # Avança 5 casas
    20: -3,  # Volta 3 casas
    25: "perde_turno"  # Perde o próximo turno
}

def mostrar_tabuleiro():
    print("\n=== TABULEIRO ===")
    for i in range(1, NUM_CASAS + 1):
        marcador = ""
        for jogador, pos in posicoes.items():
            if pos == i:
                marcador += f"[{jogador}]"
        if marcador == "":
            marcador = f"[{i}]"
        print(marcador, end=" ")
        if i % 10 == 0:
            print()
    print("=================\n")

def lancar_dado():
    return random.randint(1, 6)

def aplicar_casa_especial(jogador):
    casa = posicoes[jogador]
    if casa in casas_especiais:
        efeito = casas_especiais[casa]
        if efeito == "perde_turno":
            perde_turno[jogador] = True
            print(f"{jogador} caiu numa casa que faz perder o próximo turno!")
        elif efeito > 0:
            posicoes[jogador] += efeito
            print(f"{jogador} avança {efeito} casas extras!")
        elif efeito < 0:
            posicoes[jogador] += efeito
            if posicoes[jogador] < 0:
                posicoes[jogador] = 0
            print(f"{jogador} volta {abs(efeito)} casas!")
        time.sleep(1)

def verificar_vitoria(jogador):
    if posicoes[jogador] >= NUM_CASAS:
        print(f"\n🎉 Jogador {jogador} venceu o Jogo da Glória! 🎉\n")
        return True
    return False

def iniciar_jogo():
    jogo_ativo = True
    while jogo_ativo:
        for jogador in jogadores:
            mostrar_tabuleiro()
            
            if perde_turno[jogador]:
                print(f"{jogador} perdeu este turno.\n")
                perde_turno[jogador] = False
                continue

            input(f"{jogador}, pressione ENTER para lançar o dado...")
            dado = lancar_dado()
            print(f"{jogador} lançou o dado e tirou {dado}!")
            posicoes[jogador] += dado

            aplicar_casa_especial(jogador)

            if verificar_vitoria(jogador):
                mostrar_tabuleiro()
                jogo_ativo = False
                break
            time.sleep(1)
