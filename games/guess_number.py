import random

count = 1
num = random.randint(0, 100)

play_again = "Y"

while play_again == 'Y':
    user_guess = int(input("Guess a number in between 0 - 100: "))
    while num != user_guess:
        if user_guess > num:
            user_guess = int(input("Too big! Try again: "))
        else:
            user_guess = int(input("Too small! Try again: "))
        count += 1

    print(f"You've guessed it! You took {count} tries to get it!")
    play_again = input('Enter "Y" to play again: ')

