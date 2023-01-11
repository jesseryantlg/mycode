#!/usr/bin/env python3

"""Python Final Project - Go Fish | Jesse Ryan"""


from card_deck import *

#Deck()
#Deal 5 cards from the deck to three different players
d = Deck()

#view the contents of the deck before dealing
print("The deck contains: ", d)

#Uncomment the lines below to incorporate user permissions. Leaving commented to work on the game mechanics
#ready = ["yes", "y"]
#start = input("Are you ready to play 'Go Fish'?").lower

print("\n")



print("Dealing...")


#else:
 #   print("Please try again. Enter 'y' or 'yes'")
#  break
#Shuffle the deck

print("Shuffling the deck...")

d.shuffle()
print("The deck contains: ", d)

#Deal 5 cards to two players. 
#Define the pile

hands = d.deal(2, 5)


#validate that cards were transferred from the deck to the pile
print("The players are holding: ", hands)
print("\n")

print("The deck contains: ", d)

print("\n")
print("Player one has: ", hands[0])


#pile = d.remove(hands) # - hands

#p = Pile(d.deal(1,52))
#hands = p.deal(2,5)


#print("The pile contains: ", pile)

#print("The deck contains: ", d) 
##print the player's hand only
#print(hands[0])

#print player 2's hand
#print(hands[1])

#print the pile
#print(p)




