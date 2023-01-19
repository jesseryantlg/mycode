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
p2matches = []
p1score = len(p1matches)
p2score = len(p2matches)
suits = ["H", "S", "C", "D"]                                            
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
colors = ["blue", "yellow", "red"]

# Introduce players to the game
def gamesetup():
    print("Intro....\n")
    print(gamelogo, "\n")
    # define an object for the users input
    start_game = pyip.inputYesNo("  Are you ready to play 'Go Fish'? \n >>>")
    # Allow the player to opt-in when ready to play
    while start_game != "yes":
        start_game = pyip.inputYesNo("I see. Are you ready to play now? \n >>>")
    else: 
        sleep(.5)
        print("\n Great! Let's start! \n")
        print(fishlogo)
    
    #Choose a color of the day and have the player guess to determine who goes first

    go_first = random.choice(colors)

    #print("Decide who goes first. What color am I thinking of? \n")
    choice = pyip.inputChoice(colors)

    print("You chose: ", choice, ".  The color was: ", go_first, ". \n")

    if choice == go_first:
        print("You chose...wisely.You go first. \n")
        print("You are holding: ", p1hand, "\n")
    else:
        print("You chose...poorly. Player 2 goes first. \n")
        
    # Count the number of cards and shuffle the card deck
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
    # Deal 7 Cards to 2 Players
    for x in range(7):
        p1deal = random.choice(carddeck)
        p1hand.append(p1deal)
        carddeck.remove(p1deal)
    for x in range(7):
        p2deal = random.choice(carddeck)
        p2hand.append(p2deal)
        carddeck.remove(p2deal)
    print("P1 Card Sets:", p1matches)
    print("P2 Card Sets:", p2matches)

def CheckforMatches(hand):
    if len(hand) != len(set(hand)):
        card_set = [card for card in hand if hand.count(card) == 4]
        if card_set:
            return True
    else:
        return False

def evalmatches(hand, matches):
    books = CheckforMatches(hand)
    if books:
        print("You have matches \n")
        # Identify matching number
        card_set = list(set([card for card in hand if hand.count(card) == 4]))
        set_number = card_set[0]
        # add matching number to matches list
        matches.append(set_number)
        # remove number from player hand
        while set_number in hand:
            hand.remove(set_number)
        print(p1matches)
        print(hand)
        print(len(p1matches))
    else:
        print("You do not have matches right now. \n")
gamesetup()
print(p1hand)
print(p2hand)

#print the number of cards remaininig in the pond and the number of cards in each player's hand

print("Player 1 is holding", len(p1hand), "cards.")
print("Player 2 is holding", len(p2hand), "cards.")
print("The pond contains", len(carddeck), "cards. \n")

def game():
   # while True:
    # Player Turn: 
    #   Check Matches
        evalmatches(p1hand, p1matches)
        evalmatches(p2hand, p2matches)
        print(p1matches)
        print(p2matches)
        print(p1score)
        print(p2score)
        print(success)


    #   Prompt the player for which card to play 
        #guess = pyip.inputChoice("Which card would you like to play? ", p1hand)

    #       a. input validation
    #           1. is card in hand?
    #       b. check p2 hand
    #           1. in p2 hand
    #               a. move card to p1 hand
    #                   1. check matches
    #                   2. check win
    #                       a. deck == 0 or p1hand == 0 or p2hand == 0
    #                           1. break
    #                   3. ask again
    #           2. not in p2 hand
    #               a. draw card
    #               b. end turn
    # 
    # Bot turn:
    #   Check Matches
        evalmatches(p2hand, p2matches)
    #       a. Yes matches
    #           1. move card to player sets
    #       b. no matches
    #           1. continue
    #   Ask Card
    #       a. bot choose random card
    #       b. check p1 hand
    #           1. in p1 hand
    #               a. move card to p2 hand
    #                   1. check matches
    #                   2. check win
    #                       a. deck == 0 or p1hand == 0 or p2hand == 0
    #                   3. ask again
    #           2. not in p1 hand
    #               a. draw card
    #               b. end turn
    # 
    # Win:
    #  1. count player sets vs bot sets
    #  2. determine winner
    #  3. Print winner
    # 
    # 

game()

#Choose a color of the day and have the player guess to determine who goes first


#go_first = random.choice(colors)

#print("Decide who goes first. What color am I thinking of? \n")
#choice = pyip.inputChoice(colors)

#print("You chose: ", choice, ".  The color was: ", go_first, ". \n")


#if choice == go_first:
 #print("You chose...wisely.You go first. \n")
  #  print("You are holding: ", p1hand, "\n")
    

   # pyip.inputChoice("Which card would you like to play? \n", p1hand)

#else:
 #   print("You chose...poorly. Player 2 goes first. \n")
  #  print("Player 2 is holding: ", p2hand, "\n")
   # pyip.inputChoice("Which card would you like to play? \n", p2hand)
