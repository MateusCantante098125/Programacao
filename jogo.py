import os

os.system("cls")

menu ={
    "1": "Jogo Do Galo",
    "2": "Jogo 4 em linha",
    "3": "Jogo da Gloria",
}

print("Menu de Jogos:")
print("----------------")
for numero,texto in menu.items():
    print(f"{numero} - {texto}")
    
escolha = input("Escolha o jogo que pretende jogar: ")
os.system("cls")
if escolha == "1":
    import jogo_galo
    jogo_galo.jogo()
    
elif escolha == "2":
    import jogo_4Linha
    jogo_4Linha.jogo()
    
elif escolha == "3":
    import jogo_gloria
    jogo_gloria.jogo()