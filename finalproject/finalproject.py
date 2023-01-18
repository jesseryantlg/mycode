#!/usr/bin/env python3
"""TLG Final Project - Go Fish | Jesse Ryan"""

from easy_timing import timer
from time import sleep
import collections
import pyinputplus as pyip
import random
import re
from finalprojectdata import fishlogo, gamelogo, success, carddeck, suits, cardvalues, suiticons

pond = []
p1hand = []
p2hand = []
p1matches = []
p1score = 0
p2score = 0
suits = ["H", "S", "C", "D"]                                            
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
colors = ["blue", "yellow", "red"]


#Introduce players to the game
print("Intro....\n")
print(gamelogo, "\n")

#define an object for the users input
start_game = pyip.inputYesNo("  Are you ready to play 'Go Fish'? \n >>>")

#Allow the player to opt-in when ready to play
while start_game != "yes":
    start_game = pyip.inputYesNo("I see. Are you ready to play now? \n >>>")
else: 
    sleep(.5)
    print("\n Great! Let's start! \n")
    print(fishlogo)

#Count the number of cards and shuffle the card deck
random.shuffle(carddeck)
print("The card deck contains", len(carddeck), "cards. \n")
sleep(.5)
print(" Shuffling \n")
print("\n")
print("         Everyday I'm shuffling...\n")
sleep(1)
print("                            Shuffling...\n")
sleep(1)
print("                                   Shuffling...\n")

#Deal 7 Cards to 2 Players
for x in range(7):
    p1deal = random.choice(carddeck)
    p1hand.append(p1deal)
    carddeck.remove(p1deal)

for x in range(7):
    p2deal = random.choice(carddeck)
    p2hand.append(p2deal)
    carddeck.remove(p2deal)
    

def CheckforMatches(p1hand):
    if len(p1hand) == len(set(p1hand)):
        return False
    else:
        return True

matches = CheckforMatches(p1hand)
if matches:
    print("You have matches \n")
else:
    print("You do not have matches right now. \n")


print(p1hand)
print(p2hand)

    


#print the number of cards remaininig in the pond and the number of cards in each player's hand

print("Player 1 is holding", len(p1hand), "cards.")
print("Player 2 is holding", len(p2hand), "cards.")
print("The pond contains", len(carddeck), "cards. \n")



#Choose a color of the day and have the player guess to determine who goes first


#go_first = random.choice(colors)

#print("Decide who goes first. What color am I thinking of? \n")
#choice = pyip.inputChoice(colors)

#print("You chose: ", choice, ".  The color was: ", go_first, ". \n")


#if choice == go_first:
 #   print("You chose...wisely.You go first. \n")
  #  print("You are holding: ", p1hand, "\n")
    

   # pyip.inputChoice("Which card would you like to play? \n", p1hand)

#else:
 #   print("You chose...poorly. Player 2 goes first. \n")
  #  print("Player 2 is holding: ", p2hand, "\n")
   # pyip.inputChoice("Which card would you like to play? \n", p2hand)




  #  Which value would you like to ask for? \n")
   # for cards in p1hand:
    #    if values in p1hand:
     #       print(values)
   
        #options = str(values[0])
        #print(options)
        #print(p1hand)
        #guess = pyip.inputChoice(p1hand)
    
# p1guess = pyip.inputChoice(options)

#else: 
 #   print("You chose...poorly. Player 2 goes first. \n")
  #  for cards in p2hand:
   #     if values in p2hand: 
    #    options =    print(values)
    #
     ##   print(options)
      #  print(p2hand)
       # p2guess = pyip.inputChoice(options)
