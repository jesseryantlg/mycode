#!/usr/bin/env python3
"""A quiz to understand yourself in the context of 'The Office' | Jesse Ryan"""




#Prompt user with a welcome
print("\nWhich character from 'The Office' would be your best friend? \n ")

q1= {"question": "Pick a type of paper:",
        "card stock": "Michael",
        "printer paper": "Jim",
        "newspaper": "Stanley", 
        "wrapping paper": "Angela",
        "glossy paper": "Pam",
        "papyrus": "Andy", 
        "sandpaper": "Dwight",
        "paper bag": "Kevin",
        "rolling paper": "Creed",
        }

userprofile= []
responses = 0

while responses <= 0:  

    #Display the first question
    print(q1["question"])
    print(" \n")
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
    print(" \n")
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
        "lighthouse": "Creed",
        "barn": "Dwight",
        "frat house": "Andy",
        "private jet": "Michael",
        "city apartment": "Jim",
        "brownstone": "Stanley",
        "duplex": "Kevin ",
        "country mansion": "Angela",
        "quirky cottage": "Pam"}

    print(q2["question"])
    print(" \n")
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
    print(" \n") 
    #check the user input against the q2 dictionary
    if q2_response not in q2:
  
        print(" Please check your spelling and try again")
        q2_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q2[q2_response])
responses = responses + 1

#two successful responses allow the user to proceed
while responses == 2:

    q3= {"question": "Pick a party theme:",
    "mardi gras": "Michael",
    "pirates": "Creed",
    "tea": "Angela",
    "football": "Jim",
    "casino": "Stanley",
    "medieval": "Dwight",
    "burlesque": "Kevin",
    "artistic": "Pam",
    "crab boil": "Andy"
    } 

    print(q3["question"])
    print(" \n") 
    #Convert q2 keys to a list
    q3_list= list(q3.keys())
 
    #print keys 2-9 from the list
    print(q3_list[1])
    print(q3_list[2])
    print(q3_list[3])
    print(q3_list[4])
    print(q3_list[5])
    print(q3_list[6])
    print(q3_list[7])
    print(q3_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q3_response= input(">>>").lower()
 
    #check the user input against the q2 dictionary
    if q3_response not in q3:
  
        print(" Please check your spelling and try again")
        q3_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q3[q3_response])
responses = responses + 1

while responses == 3:

    q4= {"question": "Pick a career:",
    "graphic designer": "Pam",
    "professor": "Stanley",
    "writer": "Angela",
    "survivalist": "Dwight",
    "bartender": "Kevin",
    "actor": "Andy",
    "bitcoin developer": "Creed",
    "ceo": "Michael",
    "sports agent": "Jim"
     }

    print(q4["question"])
    print(" \n") 
    
    #Convert q2 keys to a list
    q4_list= list(q4.keys())
 
    #print keys 2-9 from the list
    print(q4_list[1])
    print(q4_list[2])
    print(q4_list[3])
    print(q4_list[4])
    print(q4_list[5])
    print(q4_list[6])
    print(q4_list[7])
    print(q4_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q4_response= input(">>>").lower()
 
    #check the user input against the q2 dictionary
    if q4_response not in q4:
  
        print(" Please check your spelling and try again")
        q4_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q4[q4_response])
responses = responses + 1

while responses == 4:

    q5= {"question": "How will you probably die?", 
        "alcohol poisoning": "Michael",
        "sleeping": "Pam ",
        "heart attack": "Kevin", 
        "autoerotic asphyxiation": "Creed",
        "not possible": "Dwight",
        "lost at sea": "Andy ",
        "car accident": "Jim ",
        "sugar overdose": "Stanley",
        "eaten by cats": "Angela ",
        }
        
    print(q5["question"])
    print(" \n") 
        
    #Convert q5 keys to a list
    q5_list= list(q5.keys())
 
    #print keys 2-9 from the list
    print(q5_list[1])
    print(q5_list[2])
    print(q5_list[3])
    print(q5_list[4])
    print(q5_list[5])
    print(q5_list[6])
    print(q5_list[7])
    print(q5_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q5_response= input(">>>").lower()
 
    #check the user input against the q2 dictionary
    if q5_response not in q5:
  
        print(" Please check your spelling and try again")
        q5_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q5[q5_response])

responses = responses + 1
      

while responses == 5:
    q6= {"question": "Pick one thing for your freezer:",
    "steak": "Andy",
    "ice cream": "Jim",
    "ice": "Angela ",
    "cookie dough": "Kevin",
    "money": "Creed",
    "bananas": "Pam",
    "microwave jalapeno poppers": "Stanley",
    "venison": "Dwight",
    "frozen dinner": "Michael",
    }

    print(q6["question"])
    print(" \n") 
        
    #Convert q6 keys to a list
    q6_list= list(q6.keys())
 
    #print keys 2-9 from the list
    print(q6_list[1])
    print(q6_list[2])
    print(q6_list[3])
    print(q6_list[4])
    print(q6_list[5])
    print(q6_list[6])
    print(q6_list[7])
    print(q6_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q6_response= input(">>>").lower()
 
    #check the user input against the q2 dictionary
    if q6_response not in q6:
  
        print(" Please check your spelling and try again")
        q6_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q6[q6_response])

responses = responses + 1

while responses == 6:
    q7= {"question": "How did you get in trouble in high school?",
    "not participating": "Pam",
    "talking": "Andy",
    "pulling pranks": "Jim",
    "eating in class": "Stanley",
    "absence": "Creed ",
    "bullying": "Michael",
    "skipping gym": "Kevin",
    "arguing with teachers": "Dwight",
    "didn't happen": "Angela"
    }

    print(q7["question"])
    print(" \n") 
        
    #Convert q5 keys to a list
    q7_list= list(q7.keys())
 
    #print keys 2-9 from the list
    print(q7_list[1])
    print(q7_list[2])
    print(q7_list[3])
    print(q7_list[4])
    print(q7_list[5])
    print(q7_list[6])
    print(q7_list[7])
    print(q7_list[8])
    print(" \n")
  
    #ask for a response and format to lowercase 
    q7_response= input(">>>").lower()
 
    #check the user input against the q7 dictionary
    if q7_response not in q7:
        print(" Please check your spelling and try again")
        q7_response= input(">>>").lower()
    else:
        break
 
userprofile.append(q7[q7_response])

responses = responses + 1

print(most_frequent(userprofile))
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
