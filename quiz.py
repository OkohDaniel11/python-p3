def do_you_want_to_play():
    """
    Check if player wants to run game
    """
    print('Welcome to my Quiz Game 🙂')
    for i in range(3):
        playing = input("Do you want to play ? (yes/no): \n")
        if playing.lower() == "yes":
            return run_game()
        elif playing.lower() == "no":
            break
        else:
            print(f'Are you sure ?{"(Try again)"if i > 2 else ""}')
    print("Then another time. Have a nice day 🙂")
    return False


def run_game():
    """
    Gives user 3 questionnaire to pick if user enters something different
    tries again
    """
    print("Alright! Let us Begin :)\n")
    print("Here are a list of questionnaires you can run:\n"
          "a) General knowledge\n"
          "b) Geography\n"
          "c) Computer")
    while True:
        choice = input("Please pick one of the questions you want to answer: \n")
        if choice.lower() in ["a","b","c"]:
            break
        else:
            print("Invalid input. Please use 'a', 'b' or 'c'.")

    if choice.lower() == "a":
        general_questions()
    elif choice.lower() == "b":
        geography_questions()
    elif choice.lower() == "c":
        computer_questions()


def q_restart(score, questionnaire):
    """
    Ask user if they want to try different questions when getting full marks
    or ask user if they want to try the same questions when failing
    """
    if score == 5:
        response = input("Congratulations! You got a perfect score! "
                         "Do you want to try a different questionnaire? "
                         "(yes/no): ")
        if response.lower() == "yes":
            run_game()
        else:
            print("Thanks for playing!")
    else:
        response = input(f"Do you want to try the {questionnaire} "
                         "questionnaire again? "
                         "(yes/no): ")
        if response.lower() == "yes":
            if questionnaire == "General knowledge":
                general_questions()
            elif questionnaire == "Geography":
                geography_questions()
            elif questionnaire == "Computer":
                computer_questions()
            else:
                print("Invalid questionnaire type.")
        else:
            return run_game()


def general_questions():
    """
    If user picks general questions it calls out general questions
    """
    print("So you have picked General Knowledge. "
          "Welcome let us see what you know. 🙂")

    score = 0
    # question 1
    print("First question...\n")
    answer = input("Which is the only body part that is "
                   "fully grown from birth? \n")
    if answer.lower() == "eyes":
        print('MMM so that is your answer...')
        print('.........')
        print('Good job. You got it correct 🙂\n')
        score += 1
    else:
        print('MMM so that is your answer...')
        print('Sighhh you got it wrong :(. Correct answer is Eyes.')

    # question 2
    print("Second question...\n")
    answer = input("In what country was Elon Musk born?\n")
    if answer.lower() == "south africa":
        print('MMM so that is your answer...')
        print('.........')
        print('Well done. You got it correct 🙂\n')
        score += 1
    else:
        print('MMM so that is your answer...')
        print('Boo you got it wrong :(. Correct answer is South Africa.\n')
    # question 3
    print("Third question...\n")
    answer = input("How many hearts does an octopus have? \n")
    if answer.lower() == "3":
        print('MMM so is this your answer...')
        print('.........')
        print('Well Well. You got it correct 🙂\n')
        score += 1
    else:
        print('MMM so is this your answer...')
        print('Boo you got it wrong :(. Correct answer is 3.\n')
    # question 4
    print("Fourth question...\n")
    answer = input("What planet is closest to the sun? \n")
    if answer.lower() == "mercury":
        print('MMM so is that the answer you came to...')
        print('.........')
        print("I'm astounded. You got it correct 🙂\n")
        score += 1
    else:
        print('MMM so is that the answer you came to...')
        print('Boo you got it wrong :(. Correct answer is Mercury.\n')
    # question 5
    print("Fifth question...\n")
    answer = input("What is a group of crows called? \n")
    if answer.lower() == "a murder":
        print('MMM so that is your answer...')
        print('.........')
        print("I can't believe it. You got it correct 🙂\n")
        score += 1
    else:
        print('MMM so that is your answer...')
        print('Boo you got it wrong :(. Correct answer is A murder\n')

    print('You got ' + str(score) + ' out of 5 questions right!')
    print('You got ' + str((score / 5) * 100) + ' %')
    q_restart(score, "General knowledge")


def geography_questions():
    print("Interesting pick Welcome to Geography")
    print("For this questionnaire all you will have to "
          "type out is one letter a-d.\n")

    score = 0
    # question 1
    print("First question...\n")
    answer = input("What is the name of the tallest mountain in the world?\n"
                   "a) Mount Everest\nb) K2\nc) Lhotse\nd) Makalu\n")
    if answer.lower() == "a":
        print('..... Hmmm.')
        print('Correct you got it right 🙂\n')
        score += 1
    else:
        print("....... I can't believe it I really cannot believe it")
        print('BOO you got it wrong :(. Correct answer is Mount Everest\n')
    # question 2
    print("Second question...\n")
    answer = input("Which country has the largest population in the world?\n"
                   "a) India\nb) USA\nc) Russia\nd) China\n")
    if answer.lower() == "d":
        print('....... I see.')
        print('Correct you got it right 🙂\n')
        score += 1
    else:
        print('.... is this not easy. HOW?')
        print('BOO you got it wrong :(. Correct answer is China\n')
    # question 3
    print("Third question...\n")
    answer = input("Where are the Spanish Steps located?\n"
                   "a) Madrid, Spain\nb) Bogota, Colombia\n"
                   "c) Quito, Ecuador\nd) Rome, Italy\n")
    if answer.lower() == "d":
        print('.... Well will you look at that.')
        print('Correct you got it right 🙂\n')
        score += 1
    else:
        print('.... only natural.')
        print('BOO you got it wrong :(. Correct answer would is Rome, Italy\n')
    # question 4
    print("Fourth question...\n")
    answer = input("What countries border directly north of Hungary?\n"
                   "a) Turkey\nb) Switzerland\nc) Ukraine\nd) Serbia\n")
    if answer.lower() == "c" or answer.lower() == "d":
        print('..... Never expected it!')
        print('Correct you got it right 🙂\n')
        score += 1
    else:
        print('..... Should I be shocked.')
        print("BOO you got it wrong :(. Correct"
              " answer would be Serbia or Ukraine.\n")
    # question 5
    print("Fifth question...\n")
    answer = input("What season does Australia experience in December?\n"
                   "a) Winter\nb) Spring\nc) Summer\nd) Fall\n")
    if answer.lower() == "c":
        print('...... You keep leaving me shocked.')
        print('Correct you got it right 🙂\n')
        score += 1
    else:
        print('....... As expected.')
        print('BOO you got it wrong :(.Correct answer is Summer\n')

    print('You got ' + str(score) + ' out of 5 questions right!')
    print('You got ' + str((score / 5) * 100) + ' %\n')
    q_restart(score, "Geography")


def computer_questions():
    print('So you have picked Computer Questionnaire Welcome.\n')
    score = 0
    # question 1
    print('First question....\n')
    answer = input("What do you call a portable computer?\n")
    if answer.lower() == "laptop":
        print('⭐Correct you got it right 🙂⭐\n')
        score += 1
    else:
        print('BOO you got it wrong :(. Correct answer is laptop\n')
    # question 2
    print('Second question....\n')
    answer = input("What do you use to read CDs/DVDs?\n")
    if answer.lower() == "cd and dvd player":
        print('⭐Correct you got it right 🙂⭐\n')
        score += 1
    else:
        print('BOO you got it wrong :(. Correct answer is cd and dvd player\n')
    # question 3
    print('Third question....\n')
    answer = input("What memory below is the largest?\na) 1TB\nb)"
                   " 1GB\nc) 55000Bytes\nd) 10GB\n")
    if answer.lower() == "a":
        print('⭐Correct you got it right 🙂⭐\n')
        score += 1
    else:
        print('BOO you got it wrong :(. Correct answer is a\n')
    # question 4
    print('Fourth question....\n')
    answer = input("You need an internet browser to access "
                   "the Internet. (True/False)\n")
    if answer.lower() == "true":
        print('⭐Correct you got it right 🙂⭐\n')
        score += 1
    else:
        print('BOO you got it wrong :(. Correect answer is true.\n')
    # question 5
    print('Fifth question....\n')
    answer = input("A software comes with a product key.(True/False\n")
    if answer.lower() == "true":
        print('⭐Correct you got it right 🙂⭐\n')
        score += 1
    else:
        print('BOO you got it wrong :(. Correct answer is true\n')

    print('You got ' + str(score) + ' out of 5 questions right!')
    print('You got ' + str((score / 5) * 100) + ' %\n')
    q_restart(score, "Computer")


if __name__ == "__main__":
    do_you_want_to_play()

