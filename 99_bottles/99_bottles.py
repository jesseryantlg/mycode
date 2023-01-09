#!/usr/bin/env python3
"""Use range to print 99 bottles of beer | Jesse Ryan"""

import time
with open("99bottles.txt", "w") as doc:
    for bottles in range (99,-1,-1):
        print(bottles, "bottles of beer on the wall!", bottles, "bottles of beer! You take one down, pass it around!")
        print(bottles, "bottles of beer on the wall!\n")
        """99 bottles of beer for loop"""

#Wes's code
#import time

#try:
#    bottles = input("How many bottles do you have on your wall? (No more than 100 please)\n"))
# bottles = int(bottles)   
# if bottles > 100:
#        print("Whoa there, you don't have that many bottles on your wall.")
 #   elif bottles > 0 < 100:
  #      for count in range(0,bottles):
   #         print(f"{bottles} of beer on the wall!! {bottles} of beeeeeer!")
    #        print(f"Take one down, pass it around. {bottles} of beer on the wall.")
     #       bottles -= 1
      #      time.sleep(1)
      #  if bottles == 0:
       #     print("No more bottles of beer on the wall! No more bottles of beeeeer!")
       #     print("Now I'm sad, and probably an alcoholic. No more bottles of beer on the wall.")           
#except:
 #  print(f"That wasn't a number! I can't count down from {bottles}")


#Angel's code
#!/usr/bin/env python3

#song= True
#while song:
 #   beers_number= (input("How many beers you want to start counting from?: "))
 #   try:
  #      beers_number= int(beers_number)
   #     if beers_number < 1 or beers_number > 100:
   #         print("It has to be a number in the range of 1 to 100, Please try again!")
    #    else:
     #       for number in range(beers_number, 0, -1):
      #          print(f"{number} bottles of beer on the wall! {number} bottles of beer! You take one down, pass it around!")
   # except:
    #    print("Input is not a number, it needs to be a number in the range of 1 to 100!")


