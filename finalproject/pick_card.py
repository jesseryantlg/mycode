
p1hand = [3,4,5]
p1matches = [1]
p2hand = [3,6,7,8,2,9,10]
p2matches = []

def playerchoice():
    

#   Ask Card
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