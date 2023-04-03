# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 15:34:29 by phijano-          #+#    #+#              #
#    Updated: 2023/03/14 16:05:27 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

number = randint(1, 99);

print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

guess_try = 0
while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        exit()
    elif not guess.isnumeric():
        print("That's not a number.")
        guess_try += 1
    elif int(guess) == number:
        if guess_try == 0:
            if number == "42":
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            else:
                print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in " + str(guess_try + 1) + " attempts!")
        exit()
    elif int(guess) < number:
        print("Too low!")
        guess_try += 1
    else:
        print("Too high!")
        guess_try += 1
