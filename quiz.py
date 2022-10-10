#layout for every question
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("+++++++++++++++++++++++++++++++++++++")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#answer checker
def check_answer(answer, guess):

    if answer == guess:
        print("You are correct!")
        return 1
    else:
        print("Sorry, that is wrong!")
        return 0

#score calculator and output
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Your overall results:")
    print("-------------------------")

    print("Correct Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your Answers: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your total score is: "+str(score)+"%")

#end of the quiz options
def play_again():

    print("If you would like to play again, type yes")
    print("If you are satisfied with your score, type no to proceed to main menu")
    response = input("Please type your response (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        print("Enjoy!")
        import runningoutoftime.py
    
#question and answer bank


questions = {
 "1. Which is the correct order, starting with the smallest and ending with the largest?: ": "A",
 "2. Which is the third planet from the Sun?: ": "C",
 "3. Which force keeps the planets in orbit?: ": "B",
 "4. Why does an astronaut weigh less on the Moon than on the Earth?: ": "C",
 "5. What is the weight of a 20kg box on the Earth?": "C",
 "6. The orbits of the planets are": "C",
 "7. The further away from the Sun": "C",
 "8. Why is a day on Mars about 37 minutes longer than a day on Earth": "B",
 "9. In which direction does the Earth spin?In which direction does the Earth spin?": "A",
 "10.Why do we have seasons on Earth?Why do we have seasons on Earth?": "C"

}

options = [["A. Planet - star - galaxy", "B. Planet - galaxy - star", "C. BStar - planet - galaxy", "D. None of the above"],
          ["A. Mars", "B. Venus", "C. Earth", "D. None of the above"],
          ["A. Friction", "B. Gravity", "C. Magnetic", "D. None of the above"],
          ["A. The Moon has no atmosphere","B. The Moon has no gravity", "C. The force of gravity is weaker on the surface of the Moon than on the surface of the Earth", "D. None of the above"],
          ["A. 2N", "B. 20N", "C. 200N", "D. None of the above"],
          ["A. Perfect circles", "B. Slightly squashed circles", "C. Spheres", "D. None of the above"],
          ["A. The faster the planet moves", "B. The hotter the planet is", "C. The longer the planet's orbit takes", "D. None of the above"],
          ["A. Martian watches don't keep very good time", "B. Mars spins more slowly on its axis than Earth does", "C. Mars spins faster on its axis than Earth does", "D. None of the above"],
          ["A. From west to east", "B. From east to west", "C. From north to south", "D. None of the above"],
          ["A. The Earth is closer to the Sun in summer than it is in winter", "B. The Sun is brighter in summer than it is in winter", "C. The Earth's axis is tilted", "D. None of the above"]]
           
new_game()

while play_again():
    new_game()

print("Bye!")
