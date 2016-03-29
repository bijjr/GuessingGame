import random
def game():
    number = random.randint(1,101)
    guesses = []

    while len(guesses) < 5:
        try:
            guess = int(input("Guess? "))
        except:
            print("{} is not a number".format(guess))
        if int(guess) == number: break
        elif int(guess) in guesses: print("Are you sleeping?")
        elif int(guess) < number: print("Too low")
        elif int(guess) > number: print("Too high")
        guesses.append(int(guess))
    else:
        def loser():
            print("You lost!")
            print("The number was {}".format(number))
            exit()
        loser()

def winner():
    print("Correct!")
    print("It only took you {} guesses".format(len(guesses)))
    exit()
game()
