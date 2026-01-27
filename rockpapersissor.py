import random

choices = { 1 : ('✊', 3),
            2 : ('✋', 1),
            3 : ('✌️', 2),
            }

play_again = 'Yes'

while play_again == 'Yes':

    n = int(input('1) ✊\n2) ✋\n3) ✌️\nPick a number: '))
    cpu = random.randint(1, 3)

    if cpu == n:
        print(f"You chose: {choices[n][0]}\n"
            f"CPU chose:{choices[cpu][0]}\n"
            f"Tie!")

    elif cpu == choices[n][1]:
        print(f"You chose: {choices[n][0]}\n"
            f"CPU chose:{choices[cpu][0]}\n"
            f"You win!")

    else:
        print(f"You chose: {choices[n][0]}\n"
            f"CPU chose:{choices[cpu][0]}\n"
            f"Cpu win!")

    play_again = input('Play again?')