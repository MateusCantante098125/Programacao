import random

banco_de_palavras = ["PROGRAMACAO", "PYTHON", "COMPUTADOR", "TECLADO", "INTERNET", "ALGORITMO"]

desenhos_forca = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def mostrar_forca(erros, letras_certas, palavra_secreta):
    print(desenhos_forca[erros])
    print("Palavra: ", end="")
    for letra in palavra_secreta:
        if letra in letras_certas:
            print(f"{letra} ", end="")
        else:
            print("_ ", end="")
    print("\n" + "-" * 30)

def pedir_letra(letras_usadas):
    while True:
        try:
            tentativa = input("Escolha uma letra: ").upper().strip()
            if len(tentativa) != 1 or not tentativa.isalpha():
                print("Entrada inválida. Introduza apenas uma letra.")
                continue
            if tentativa in letras_usadas:
                print("Já tentaste essa letra. Escolhe outra.")
                continue
            return tentativa
        except ValueError:
             print("Erro na entrada.")

def verificar_vitoria(palavra_secreta, letras_certas):
    ganhou = True
    for letra in palavra_secreta:
        if letra not in letras_certas:
            ganhou = False
            break
    if ganhou:
        print("\nPARABÉNS! Venceste o jogo!")
        print(f"A palavra era: {palavra_secreta}\n")
        return True
    return False

def jogo():
    menu = {"1": "Novo Jogo", "2": "Sair"}
    print("\n--- JOGO DA FORCA ---")
    for n, t in menu.items():
        print(f"{n}. {t}")

    while True:
        op = input("Opção: ").strip()
        if op in menu: break

    if op == "1":
        palavra = random.choice(banco_de_palavras)
        letras_certas = []
        letras_erradas = []
        letras_usadas = []
        erros = 0
        
        while True:
            mostrar_forca(erros, letras_certas, palavra)
            print(f"Erros: {', '.join(letras_erradas)}")
            
            tentativa = pedir_letra(letras_usadas)
            letras_usadas.append(tentativa)

            if tentativa in palavra:
                letras_certas.append(tentativa)
            else:
                erros += 1
                letras_erradas.append(tentativa)

            if verificar_vitoria(palavra, letras_certas):
                break
            
            if erros >= 6:
                mostrar_forca(erros, letras_certas, palavra)
                print(f"\nPERDESTE! A palavra era: {palavra}\n")
                break
    elif op == "2":
        exit()
