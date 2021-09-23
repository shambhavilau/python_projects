import random
films = ['Anand', 'Drishyam', 'Sholay', 'Jab we Met', 'Golmal', 'Ajab Prem ki Gajab Kahani',
         'Humpty Sharma ki Dhulaniya', 'Yeh Jawani Hai deewani', 'Guzarish', 'Amar Akbar Anthony',
         'Amdani Atthani Kharcha Rupiya', 'Welcome', 'Patiala House', 'Luck By Chance', 'Black Friday', 'Dangal',
         'Sooryavansham', 'Mohabbatein', 'taare zameen par']
movies = []
# convert all to lower case
for i in films:
    movies.append(i.lower())
print(movies)


def create_question(pm):
    # encode the movie name
    movie_length = len(pm)
    letters = list(pm)
    temp_list = []
    for j in range(movie_length):
        if letters[j] == " ":
            temp_list.append(" ")
        else:
            temp_list.append("_")
    ques = ''.join(str(x) for x in temp_list)  # join letters together to form question
    return ques


def is_present(l, pm):
    # check if letter is present in movie name
    count = pm.count(l)
    if count == 0:
        return False
    else:
        return True


def unlock(mod_q, pm, l):
    reference_list = list(pm)
    print(reference_list)
    ques_list = list(mod_q)
    temp_list = []
    movie_len = len(pm)
    for j in range(movie_len):
        if reference_list[j] == ' ':
            temp_list.append(' ')
            print(temp_list)
        elif reference_list[j] == l:
            temp_list.append(reference_list[j])
            print(temp_list)
        else:
            if ques_list[j] == '_':
                temp_list.append('_')
                print(temp_list)
            else:
                temp_list.append(reference_list[j])
                print(temp_list)
    ques = ''.join(str(x) for x in temp_list)
    return ques


def play():
    player1_name = input("Enter name of PLAYER 1:")
    player2_name = input("Enter name of PLAYER 2:")
    player1_points = 0
    player2_points = 0
    turn = 0
    will = True
    while will:
        if turn % 2 == 0:
            # its player 1's turn
            turn += 1
            print(player1_name, ", its your turn to guess! ")
            picked_movie = random.choice(movies)
            question = create_question(picked_movie)
            print(question)
            modified_question = question
            not_answered = True
            while not_answered:
                letter = input("Enter a letter: ")
                if is_present(letter, picked_movie):
                    # place the letter in correct position
                    modified_question = unlock(modified_question, picked_movie, letter)
                    print(modified_question)
                    decide = int(input("Press 1 to Guess Movie and 2 to unlock another letter"))
                    if decide == 1:
                        answer = input("Enter movie name")
                        answer = answer.lower()
                        if answer == picked_movie:
                            player1_points += 1
                            print("You guessed it right")
                            not_answered = False
                            print(player1_name, "Your score is: ", player1_points)
                        else:
                            print("Oops! wrong guess. Try again")
                else:
                    print(letter, " not found")
            continue_choice = int(input("Press 1 to continue or 0 to quit"))
            if continue_choice == 0:
                print(player1_name, " thanks for playing along. Your score is: ", player1_points)
                print(player2_name, " thanks for playing along. Your score is: ", player2_points)
                will = False
        else:
            # player2
            turn += 1
            print(player2_name, ", its your turn to guess! ")
            picked_movie = random.choice(movies)
            question = create_question(picked_movie)
            print(question)
            modified_question = question
            not_answered = True
            while not_answered:
                letter = input("Enter a letter: ")
                if is_present(letter, picked_movie):
                    # place the letter in correct position
                    modified_question = unlock(modified_question, picked_movie, letter)
                    print(modified_question)
                    decide = int(input("Press 1 to Guess Movie and 2 to unlock another letter"))
                    if decide == 1:
                        answer = input("Enter movie name")
                        answer = answer.lower()
                        if answer == picked_movie:
                            player2_points += 1
                            print("You guessed it right")
                            not_answered = False
                            print(player2_name, "Your score is: ", player2_points)
                        else:
                            print("Oops! wrong guess. Try again")
                else:
                    print(letter, " not found")
            continue_choice = int(input("Press 1 to continue or 0 to quit"))
            if continue_choice == 0:
                print(player1_name, " thanks for playing along. Your score is: ", player1_points)
                print(player2_name, " thanks for playing along. Your score is: ", player2_points)
                will = False

            turn += 1


play()
