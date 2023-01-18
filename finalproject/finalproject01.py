#!/usr/bin/env python3
"""TLG Final Project - Go Fish | Jesse Ryan"""

"""Chad's  TO DO: how to group cards by face values into "books"- groups of
four matching cards- and tallying how many books a player has to
determine the winner """

#from card_deck import *
from easy_timing import timer 
from time import sleep
import pyinputplus as pyip
import random
from finalprojectdata import fishlogo, gamelogo,success, carddeck, suits, cardvalues, suiticons

# Create a "card deck" object
#d = Deck() #from imported module - commenting out to try making my own deck
#print("Card Deck: ", carddeck)
#print("Card values: ", cardvalues)
#print("Suit Icons: ",suiticons.values())
#print("Suit Keys: ", suits.keys())

pond = []
p1hand = []
p2hand = []
p1matches = []
p2matches = []
p1score = 0
p2score = 0

suits = ["H", "S", "C", "D"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#FOR TESTING - COMMENT OUT #
print("FOR TESTING - COMMENT OUT - Visualize current lists. \n")
print("The deck contains: ",carddeck) #Visualize the deck of cards
print("Player 1 is holding: ", p1hand)
print("Player 2 is holding: ",p2hand)
print("PLayer 1's matches: ",p1matches)
print("Player 2's matches: ", p2matches)
print("Player 1's score: ",p1score)
print("Player 2's score: ",p2score)

#Introduction/Greeting
print("Intro TBD -...He challenges you to a single game of 'Go Fish' to settle everything for good. \n")
print(gamelogo)
print("\n")

#define an object for the user's input
start_game =  pyip.inputYesNo("    Are you ready to play 'Go Fish'? \n >>'Yes or No' \n >>> ") 

#For TESTING - COMMENT OUT
#print("TO BE COMMENTED OUT - INPUT VALUE IS ", start_game)

#Verify that the player would like to begin
while start_game != "yes":
    start_game = pyip.inputYesNo("Are you ready to play 'Go Fish'? \n  >>>")
else:
    sleep(.5)
    print("\n Great! Let's start!! \n")
    print(fishlogo)
#Shuffle the deck
random.shuffle(carddeck)
print("\n Shuffling \n")
print("\n")
print("       Everyday I'm shuffling...\n")
sleep(1)     
print("                                 Shuffling...\n")
sleep(1)
print("                                              Shuffling...\n")
sleep(1)

#Deal 5 cards to 2 players
#hands = d.deal(2, 5)
print("## COMMENT OUT - DEAL TO PLAYER 1")
print(carddeck)

print("The card deck has",len(carddeck), "cards")
#pond = [ #d # remaining cards in the pile

for x in range(5):
    p1deal = random.choice(carddeck)
    p1hand.append(p1deal)
    carddeck.remove(p1deal)

#Deal to Player 2 and count the number of cards in the deck
#There should be 47

print("## COMMENT OUT - DEAL TO PLAYER 2")
print(carddeck)
print("The card deck has",len(carddeck), "cards")

for x in range(5):
    p2deal = random.choice(carddeck)
    p2hand.append(p2deal)
    carddeck.remove(p2deal)

print(carddeck)
print(p1hand)
print(p2hand)

#p1hand = hands[0] # assigns the first five card hand to a player
#p2hand = hands[1] # assigns the second five card hand to a player
colors = ["blue", "yellow", "red"]

go_first = random.choice(colors) 

#Count the number of cards remaining in the pond after dealing. 
#There should be 42.

print("The pond  has",len(carddeck), "cards") 

print("Decide who goes first. What is the color of the day?", "\n" )

choice = pyip.inputChoice(colors)

print("You chose: ", choice, "\n")

print("The color of the day is:  ", go_first, "\n")

if choice == go_first:
    print("You chose wisely. You go first. \n For which card would you like to ask Player 2 if they have a match? \n >>> ")
    for card in p2hand:
        #if card(0) != suits
        print(card)0
        cardvalue= 
        print("Card Value: ", cardvalue)
        p1facevalues= list(cardvalue)
        print(p1facevalues)
        p1guess = pyip.inputChoice(p1facevalues)

else: 
    print("You chose poorly. Player 2 goes first. \n")
    for card in p2hand:
        cardvalue= card.get_typeable_name()
        p2options= list(cardvalue)
        print("P2 Options: ", p2options)
        #cardvalue= list(cardvalue.split())
        p2facevalues = list(cardvalue)
        #for i in range(len(facevalue):
              
        print("P2 Face Values:", p2facevalues)
        p2guess = random.choice(p2facevalues)
        print("P2 Guess:", p2guess[0])

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
print(" \n FOR TESTING \n")
print("Player 1's hand:", p1hand)
print("HIDDEN - Player 2's hand:", p2hand)
print("HIDDEN - Pond:", pond)
print("Player 1's matches: ", p1matches)
print("Player 2's matches: ", p2matches)

