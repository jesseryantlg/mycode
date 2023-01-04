#!/usr/bin/env python3


def main():

    #Dictionary - Character Attributes
    marvelchars=    {
            "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},

            "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    
             "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
             }


    character = input("Which character do you want to know about? (Starlord, Mystique, Hulk)" )
   
    char_stat = input("What attribute do you want to know about? (real name, powers, archenemy)" )

    print(f"{character}'s {char_stat} is: {marvelchars[character][char_stat]}")

#call main function
main()
