
import random


def play():
    player1 = input("Player 1 pls,enter your name: ")
    player2 = input("Player 2 pls,enter your name: ")
    player1_points = 0
    player2_points = 0
    turn = 0
    while (1):
        selected_word = choose()
        question = jumble(selected_word)
        print(question)
        # player 1
        if turn % 2 == 0:
            print(player1, " its your turn")
            answer = input('Guess what is on my mind! ')
            if answer == selected_word:
                player1_points = player1_points + 1
                print("Your score is: ", player1_points)
            else:
                print("You guessed it wrong!.The correct word is: ", selected_word)
            choice = int(input("Press 1 to continue and 0 to quit: "))
            if choice == 0:
                thank(player1, player2, player1_points, player2_points)
                break
        else:
            print(player2, " its your turn")
            answer = input('Guess what is on my mind! ')
            if answer == selected_word:
                player2_points = player2_points + 1
                print("Your score is: ", player2_points)
            else:
                print("You guessed it wrong!.The correct word is: ", selected_word)
            choice = int(input("Press 1 to continue and 0 to quit: "))
            if choice == 0:
                thank(player1, player2, player1_points, player2_points)
                break
        turn = turn + 1


def thank(player1, player2, player1_points, player2_points):
    print(f'Thank you {player1} , {player2}! your score is {player1_points}, and {player2_points} respectively')


def choose():
    word_list = ['computer','water','fashion','science','costume','rainbow','brownie','condition','activity',
                 'dentist','design','danger','pastel','icecream','gallery','module','leader','dairy','volume','heart']
    select = random.choice(word_list)
    return select


def jumble(selected_word):
    jumbled_word = "".join((random.sample(selected_word, len(selected_word))))
    return jumbled_word


play()
