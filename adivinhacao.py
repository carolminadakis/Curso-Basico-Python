import random

def jogar():

    print("***************************************")
    print("** Bem-vindo ao jogo de Adivinhação! **")
    print("***************************************")

    numero_secreto = round(random.randrange(1, 101))
    tentativas = 0
    pontos = 1000

    print("Escolha um nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 7
    elif(nivel == 3):
        tentativas = 2
    else:
        print("Opção inválida!")

    # for in range é usado para o laço for,
    #vc atribui a variável, entre parênteses o número inicial, a variável e o +1 se dá pelo falo de que
    #o último número atribuído a variável não entra no laço.

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100!")
            continue

        acertou = (chute == numero_secreto)
        numero_maior = (chute > numero_secreto)
        numero_menor = (chute < numero_secreto)

        if (acertou):
            print("Parabéns, você acertou o número secreto e fez {} pontos!".format(pontos))
            break
        else:
            if (numero_maior):
                print("Você errou, seu chute é maior do que o número secreto!")
                if(rodada == tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            elif (numero_menor):
                print("Você errou, seu chute foi menor do que o número secreto!")
                if(rodada == tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos = pontos - abs(numero_secreto - chute)

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()



