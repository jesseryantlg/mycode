#!/usr/bin/env python3
"""A quiz to understand yourself in the context of 'The Office' | Jesse Ryan"""

#Prompt user with a welcome
print("\nWhich character from 'The Office' would be your best friend? \n ")

q1= {"question": "Pick a type of paper:",
        "card stock": "Michael",
        "printer paper": "Jim ",
        "newspaper": "Stanley ", 
        "wrapping paper": "Angela",
        "glossy paper": "Pam",
        "papyrus": "Andy ", 
        "sandpaper": "Dwight",
        "paper bag": "Kevin",
        "rolling paper": "Creed",
        }

userprofile= []
responses = 0

while responses <= 0:  

    #Display the first question
    print(q1["question"])

    #Convert q1 keys to a list
    q1_list= list(q1.keys())

    #print keys 2-9 from the list
    print(q1_list[1])
    print(q1_list[2])
    print(q1_list[3])
    print(q1_list[4])
    print(q1_list[5])
    print(q1_list[6])
    print(q1_list[7])
    print(q1_list[8])

    #ask for a response and format to lowercase 
    q1_response= input(">>>").lower()
   
    #check the user input against the q1 dictionary
    if q1_response not in q1:

        print(" Please check your spelling and try again")
        q1_response= input(">>>").lower()   
    else:
        break

userprofile.append(q1[q1_response])
responses = responses + 1

#A successful response on q1 allows the user to proceed to q2
while responses == 1: 
    
    q2= {"question": "Pick a home:",
        "lighthouse":"Creed",
        "barn":"Dwight",
        "frat house": "Andy",
        "private jet": "Michael",
        "city apartment": "Jim",
        "brownstone": "Stanley ",
        "duplex": "Kevin ",
        "country mansion": "Angela",
        "quirky cottage":"Pam "}

    print(q2["question"])
    
    #Convert q2 keys to a list
    q2_list= list(q2.keys())
 
    #print keys 2-9 from the list
    print(q2_list[1])
    print(q2_list[2])
    print(q2_list[3])
    print(q2_list[4])
    print(q2_list[5])
    print(q2_list[6])
    print(q2_list[7])
    print(q2_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q2_response= input(">>>").lower()
 
    #check the user input against the q2 dictionary
    if q2_response not in q2:
  
        print(" Please check your spelling and try again")
        q2_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q2[q2_response])
responses = responses + 1

print(userprofile)
print("q3")       
print(responses)
print(userprofile)


#remove the comment to test formatting
#print(q1_response)

#q2= {"question": "Pick a home:",
 #       "lighthouse":"Creed",
  #      "barn":"Dwight",
#        "frat house": "Andy",
 #       "private jet": "Michael",
  #      "city apartment": "Jim",
   #     "brownstone": "Stanley ",
    #    "duplex": "Kevin ",
     #   "country mansion": "Angela",
      #  "quirky cottage":"Pam "}






#check the response against the available options
#if q1_response in q1_list:
    










#convert

#q2= {"question": "Pick a home:",
       # "lighthouse":"Creed",
       # "barn":"Dwight",
       # "frat house": "Andy",
       # "private jet": "Michael",
       # "city apartment": "Jim",
       # "brownstone": "Stanley ",
       # "duplex": "Kevin ",
       # "country mansion": "Angela",
       # "quirky cottage":"Pam "}

# q3= {"question": "Pick a party theme:",
       # "Mardi Gras":"Michael",
       # "pirates":"Creed",
       # "tea":"Angela",
       # "football":"Jim",
      #  "casino":"Stanley",
       # "medieval":"Dwight",
       # "burlesque":"Kevin",
       # "artistic":"Pam ",
       # "crab boil":"Andy"
       # ]

# q4= {"question": "Pick a career:",
 #       "graphic designer": "Pam",
  #      "professor": "Stanley",
  #      "writer": "Angela",
  #      "survivalist": "Dwight",
  #      "bartender": "Kevin",
  #      "actor": "Andy",
  #      "bitcoin developer": "Creed",
  #      "CEO": "Michael",
  #      "sports agent": "Jim"
  #      }

# q5= {"question": "How will you probably die?"
 #       "alcohol poisoning":"Michael",
  #      "sleeping":"Pam ",
   #     "heart attack":"Kevin", 
    #    "autoerotic asphyxiation": "Creed ",
     #   "NOT POSSIBLE": "Dwight",
      #  "lost at sea": "Andy ",
       # "car accident": "Jim ",
       # "sugar overdose": "Stanley",
       # "eaten by cats": "Angela ",
       # }
# q6= {"question": "Pick one thing for your freezer:",
 #       "steak": "Andy",
  #      "ice cream": "Jim",
   #     "ice": "Angela ",
    #    "cookie dough": "Kevin",
     #   "money": "Creed",
      #  "bananas": "Pam",
       # "microwave jalapeno poppers": "Stanley",
       # "venison": "Dwight",
       # "frozen dinner": "Michael",
       # }

# q7= {"question": "How did you get in trouble in high school?",
 #       "not participating":"Pam",
  #      "talking":"Andy",
   #     "pulling pranks":"Jim",
    #    "eating in class":"Stanley",
     #   "absence":"Creed ",
      #  "bullying":"Michael",
       # "skipping gym": "Kevin",
       # "arguing with teachers": "Dwight",
       # "didn't happen": "Angela"
       # }
