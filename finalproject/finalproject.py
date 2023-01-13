#!/usr/bin/env python3
"""TLG Final Project - Go Fish | Jesse Ryan"""

"""Chad's  TO DO: how to group cards by face values into "books"- groups of
four matching cards- and tallying how many books a player has to
determine the winner """

from card_deck import *
from easy_timing import timer 
from time import sleep
import pyinputplus as pyip
import random

# Create a "card deck" object
d = Deck()
p1hand = []
p2hand = []
p1matches = []
p2matches = []
p1score = 0
p2score = 0

#FOR TESTING - COMMENT OUT #
print("FOR TESTING - COMMENT OUT - Visualize current lists. \n")
print("The deck contains: ",d) #Visualize the deck of cards
print("Player 1 is holding: ", p1hand)
print("Player 2 is holding: ",p2hand)
print("PLayer 1's matches: ",p1matches)
print("Player 2's matches: ", p2matches)
print("Player 1's score: ",p1score)
print("Player 2's score: ",p2score)

#Introduction/Greeting
print("Intro TBD -...He challenges you to a single game of 'Go Fish' to settle everything for good. \n")
#define an object for the user's input
start_game =  pyip.inputYesNo("    Are you ready to start? \n >>'Yes or No' \n ") 

#For TESTING - COMMENT OUT
#print("TO BE COMMENTED OUT - INPUT VALUE IS ", start_game)

#Verify that the player would like to begin
while start_game != "yes":
    start_game = pyip.inputYesNo("Are you ready to play 'Go Fish'? \n  >>>")
else:
    sleep(.5)
    print("\n Great! Let's start!! \n")
 
#Shuffle the deck
d.shuffle()
print("       Everyday I'm suffling...\n")
sleep(1)     
print("                                 Shuffling...\n")
sleep(1)
print("                                              Shuffling...\n")
sleep(1)

#Deal 5 cards to 2 players
hands = d.deal(2, 5)

p1hand = hands[0] # assigns the first five card hand to a player
p2hand = hands[1] # assigns the second five card hand to a player
pond = d # remaining cards in the pile

colors = ["blue", "yellow", "red"]

go_first = random.choice(colors) 

print("Decide who goes first. What is the color of the day?", "\n" )

choice = pyip.inputChoice(colors)

print("You chose: ", choice, "\n")

print("The color of the day is:  ", go_first, "\n")

if choice == go_first:
    print("You chose wisely. You go first. \n For which card would you like to ask Player 2 if they have a match? ")
    for card in p1hand:
        cardvalue= card.get_typeable_name()
        print(cardvalue)
else: 
    print("You chose poorly. Player 2 goes first. \n")



#while True:
 #   guess= input(">")
    # for testing purposes, we'll let player 2 ask for as many cards as they want
    # until we type "stop"
#    if guess == "stop":
 #       break
  #  found= False

    # loop over all card objects in p1hand to check if they have the card(s) we asked for
   # for card in p1hand:
        # return the card as a string so its easier to check
    #    cardvalue= card.get_typeable_name()

        # we will check if the value of "guess" (for example, "2","K","A", etc.)
        # is in the name of the "cardvalue" variable (for example, "2D","KC")
        # NOTE: "2D" is two of diamonds, "KC" is king of clubs, etc.

     #   if guess in cardvalue:
      #      print(card)         # announce what card is a match (printing card and not cardvalue shows the lil card emoji)
       #     found= True         # set a boolean as a flag that a match was made
        #    p2hand.append(card) # add that matching card to player 2's hand
         #   p1hand.remove(card) # remove that card from player 1's hand
                                # all of this will repeat over all other cards in player 1's hand

    # if found == False (no matches)
   # if not found:
        # announce that the other player can pound sand
    #    print("Go fish, sucka!")

        # grab a card from the "pond" variable
     #   new_card= pond.pop()   # this grabs the first card in the deck

        # add that new card to player 2's hand
      #  p2hand.append(new_card)

# debug output displaying all cards in both players' hands and in the remaining deck
print("Player 1's hand:", p1hand)
print("HIDDEN - Player 2's hand:", p2hand)
print("HIDDEN - Pond:", pond)
print("Player 1's matches: ", p1matches)
print("Player 2's matches: ", p2matches)

