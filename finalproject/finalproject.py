#!/usr/bin/env python3

"""Python Final Project - Go Fish | Jesse Ryan"""


from card_deck import *
from collections import Counter
import random
deck = ["A♦", "A♣", "A♥", "A♠", "2♦", "2♣", "2♥", "2♠", "3♦", "3♣", "3♥", "3♠", "4♦", "4♣", "4♥", "4♠", "5♦", "5♣", "5♥", "5♠", "6♦", "6♣", "6♥", "6♠", "7♦", "7♣", "7♥", "7♠", "8♦", "8♣", "8♥", "8♠", "9♦", "9♣", "9♥", "9♠", "10♦", "10♣", "10♥", "10♠", "J♦", "J♣", "J♥", "J♠", "Q♦", "Q♣", "Q♥", "Q♠", "K♦", "K♣", "K♥", "K♠"]
pond = []
p1hand = []
p2hand = []
p1matches = []
p1score = 0
p2matches = []
p2score = 0

#view the contents of the deck before dealing
print("The deck contains: ", deck)

#Uncomment the lines below to incorporate user permissions. Leaving commented to work on the game mechanics
#ready = ["yes", "y"]
#start = input("Are you ready to play 'Go Fish'?").lower

print("\n")

#else:
 #   print("Please try again. Enter 'y' or 'yes'")
#  break

#Shuffle the deck
print("Shuffling the deck...")
print("\n")
random.shuffle(deck)

#d.shuffle()

#Visualize the shuffled deck
print("The deck contains: ", deck)
print("\n")

#Deal 5 cards to 2 players
print("Dealing...")
print("\n")

for x in range(5):
    deal = random.choice(deck)
    p1hand.append(deal)
    deck.remove(deal)

for x in range(5):
    deal = random.choice(deck)
    p2hand.append(deal)
    deck.remove(deal)


#old code - uses card_deck package -hands = d.deal(2, 5)

#create objects for each player's hand,player matches, and the pond
#p1hand = hands[0]
#p2hand = hands[1]
#p1matches = []
#p1score = 0
#p2matches = []
#p2score = 0
#pond = d

#validate that cards were transferred from the deck to the pile
print("FOR TESTING PURPOSES - COMMENT OUT - The players are holding: ","\n","Player 1: ", p1hand, "\nPlayer 2: ", p2hand, "\n")
print("\n")
print("FOR TESTING PURPOSES - COMMENT OUT - The pond contains: ",pond)
print("\n")
print("You have: ", p1hand)
print("\n")
print("Player 1 score: ", p1score)
print("\n")
print("Player 2 score: ", p2score)



#guess = input("What card would you like to ask for?")
#response = Card.get_from_typeable_name(guess)

#print(response)

# 'face', 'get_face_from_typeable_name', 'get_from_typeable_name', 'get_suit_from_typeable_name', 'get_typeable_name', 'suit'

#for x in p1hand:
 #   y= x.__str__()
  #  if guess in y:
   #     print(y)
   # else:
       # print("go fish!")

#print(guess)


#if guess in p1hand:
