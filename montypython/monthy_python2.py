#!/usr/bin/env python3

round = 0 #initial round is zero

while True:     #sets up an infinite loop condition
    round = round +1  #increase the round counter with each incorrect guess
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input("Your guess --> ")  #collect user input
    if answer == 'Brian': #check user input for correct answer
        print('Correct')
        break #escapes the while loop
    elif round == 3: #logic to ensure the round has not reached 3
        print("Sorry, the answer was Brian.")
        break #escapes the while loop
    else: #if answer is wrong and round is not yet 3
        print("Sorry! Try Again!")

