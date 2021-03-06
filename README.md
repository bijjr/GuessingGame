# guessing_game.py

Normal Mode

Your goal for tonight is to create a number guessing game. Your program will pick a random number between 1 and 100 and repeatedly ask you for guesses.

Requirements

If your guess is lower than the computer's number, it needs to tell you that your guess was too low.
If your guess is higher than the computer's number, it needs to tell you that your guess was too high.
If your guess is correct, the program needs to tell you that you win and the game is over.
After 5 incorrect guesses, the program needs to tell you that you lose and the game is over.
If you guess the same number twice, the program needs to ask you if you're feeling all right (or something similarly sarcastic).
The program must output the number of turns you took.
Your code must include at least two functions.
This game will be run from the command line by typing python3 guessing_game.py.

Advanced Mode (optional)

Complete all of the requirements of Normal Mode.
In normal mode, you will probably use the random.randint function. In advanced mode, find another way!
Tell the user if their guess is close.
The program must also comment on your behavior if you make a guess that doesn't help you. For example, you might say "50" and then be told "that's too low." If you then guess "25," you're just wasting a guess.

Epic Mode (optional)

Write the opposite program as well: you, the user, pick a number between 1 and 100 and the computer takes guesses at what the number is.

All of the same rules as the Normal Mode apply to the computer.

You tell it whether it's too high, too low, or correct after each guess.
The computer gets five guesses.
The computer will tell you if you are lying to it. (e.g. Computer guesses 50, you say "High." Computer then guesses 49 and you say "Low." You'd be lying, as there are no numbers between them.)

Impossible Mode (optional)

Complete all requirements of Epic Mode AND optimize the computer's strategy so it improves it's performance and guesses in fewer turns.
