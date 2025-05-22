import random

while True:
    choices = ["pedra", "papel", "tesoura"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("pedra, papel, ou tesoura?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Empate!")

    elif player == "pedra":
        if computer == "papel":
            print("computer: ", computer)
            print("player: ", player)
            print("Você perdeu!")
        if computer == "tesoura":
            print("computer: ", computer)
            print("player: ", player)
            print("Você ganhou!")

    elif player == "tesoura":
        if computer == "pedra":
            print("computer: ", computer)
            print("player: ", player)
            print("Você perdeu!")
        if computer == "papel":
            print("computer: ", computer)
            print("player: ", player)
            print("Você ganhou!")

    elif player == "papel":
        if computer == "tesoura":
            print("computer: ", computer)
            print("player: ", player)
            print("Você perdeu!")
        if computer == "pedra":
            print("computer: ", computer)
            print("player: ", player)
            print("Você ganhou!")

    play_again = input("Gostaria de jogar novamente? (sim/nao): ").lower()

    if play_again != "sim":
        break

print("Bye!")
