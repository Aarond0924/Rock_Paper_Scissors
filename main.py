import random

choice = ["rock", "paper", "scissors"]


def game():
    # user_choice = input('Choice: ')
    while True:
        user_choice = input('Choices: ').lower()
        if user_choice not in choice:
            print('Not a choice. Try again')
            game()
        else:
            break

    pc_choice = random.choice(choice)
    print("PC chose: " + pc_choice)
    if user_choice == "rock":
        if pc_choice == "paper":
            print('You Lose!')
        if pc_choice == 'rock':
            print("It's a tie")
        if pc_choice == 'scissors':
            print('You Win!')
    if user_choice == 'paper':
        if pc_choice == 'paper':
            print("It's a Tie!")
        if pc_choice == 'rock':
            print('You Win!')
        if pc_choice == 'scissors':
            print('You Lose!')
    if user_choice == 'scissors':
        if pc_choice == 'paper':
            print('You Win!')
        if pc_choice == 'rock':
            print('You Lose!')
        if pc_choice == 'scissors':
            print("It's a Tie!")
    print('Would you like to play again?')
    answer = input().lower()
    if answer == 'yes' or 'y':
        game()
    else:
        return


game()

