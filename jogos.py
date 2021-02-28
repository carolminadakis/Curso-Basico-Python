import forca
import adivinhacao

def escolhe_jogo():
    print("************************************")
    print("** Escolha um jogo e divirta-se! **")
    print("************************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Digite o número referente ao jogo desejado: "))

    if(jogo == 1):
        forca.jogar()
    else:
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()