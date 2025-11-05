import random

def jogo():
    palavras = ["python", "programador", "forca", "computador", "teclado", "codigo"]

    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    print("_ " * len(palavra))

    while tentativas > 0:
        tentativa = input("\nAdivinha uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, insere apenas uma letra.")
            continue

        if tentativa in letras_adivinhadas:
            print("Já tentaste essa letra.")
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            print("Boa! Acertaste uma letra.")
        else:
            tentativas -= 1
            print(f"Erraste! Restam {tentativas} tentativas.")

        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_adivinhadas:
                palavra_mostrada += letra + " "
            else:
                palavra_mostrada += "_ "
        print(palavra_mostrada.strip())

        if "_" not in palavra_mostrada:
            print("\n🎉 Parabéns! A palavra era:", palavra)
            break
    else:
        print("\n💀 Perdeste! A palavra era:", palavra)
