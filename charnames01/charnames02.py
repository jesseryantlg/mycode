#!/usr/bin/env python3

#this requests the users input. It must match a dictionary key, so names are provided.
char_name= input(" Which character do you want to know about? (Starlord, Mystique, Hulk)")

#this redefines the variable by ensuring the first letter is capitalized to match the keys
char_name= char_name.title()

#this requests user input to find the key's corresponding value
char_stat= input("What statistic do you want to know about? (real name, power, archenemy)")

#this is the dictionary
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "adrenaline"}
             }


#this prints the value in a preferred format
print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

#print(char_name, "'s ", char_stat, " is: ", marvelchars[char_name][char_stat], sep="")

