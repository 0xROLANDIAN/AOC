#!/usr/bin/python3

#############################
#
# AOC Day two
#
##############################

#P1 P2
#A  X Rock  1
#B  Y Paper 2
#C  Z Scissors 3

# Lose  # Win   # Draw  
# A Z 3 # A Y 2 # A X 1 
# B X 1 # B Z 3 # B Y 2
# C Y 2 # C X 1 # C Z 3

def dataset():
   with open('input.txt') as f:
        lines = f.readlines()
        f.close()
        return lines

def enumHand(result, resultScore):
    for idx, match in enumerate(result):
        matchStr = str(match[0])
        #print("roundStr is " + str(roundStr[0]) + " is, match is: " + str(matchStr[0]))
        if str(matchStr[0]) == str(roundStr[0]):
            shapeScore = int(match[1]) 
            roundScore = shapeScore + resultScore
            #print("roundScore " + str(roundScore))
            return roundScore

game = dataset();
#game = [['AY'],['BX'],['CZ']]

lose = [['AZ',3,],['BX',1],['CY',2]]
win = [['AY',2],['BZ',3],['CX',1]]
draw = [['AX',1],['BY',2],['CZ',3]]

totalScore = 0

for round in game:
    roundStr = "".join(round).strip()
    #print("Round is: " + roundStr)
    winres = any(roundStr in r for r in win)
    losres = any(roundStr in r for r in lose)
    drawres = any(roundStr in r for r in draw)

    if winres == True:
        for idx, match in enumerate(win):
            if str(match[0]) == roundStr:
                shapeScore = int(match[1]) 
                roundScore = shapeScore + 6
                totalScore = totalScore + roundScore
                #print("Win:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))
    elif drawres == True:
        for idx, match in enumerate(draw):
            if str(match[0]) == roundStr:
                shapeScore = int(match[1]) 
                roundScore = shapeScore + 3
                totalScore = totalScore + roundScore
                #print("Draw:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))
    elif losres == True:
        for idx, match in enumerate(lose):
            if str(match[0]) == roundStr:
                shapeScore = int(match[1]) 
                roundScore = shapeScore + 0
                totalScore = totalScore + roundScore
                #print("Lose:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))

totalScoreOne = totalScore
totalScore = 0

for round in game:
    roundStr = "".join(round).strip()
    #print("Round is: " + roundStr)
    if 'X' in roundStr:
        #print('Score: ' + str(enumHand(lose, 0)))
        totalScore = totalScore + enumHand(lose,0)

    elif 'Y' in roundStr:
        #print('Score: ' + str(enumHand(draw, 3)))
        totalScore = totalScore + enumHand(draw,3)

    elif 'Z' in roundStr:
        #print('Score: ' + str(enumHand(win, 6)))
        totalScore = totalScore + enumHand(win,6)

    else:
        print('Nothing here')

totalScoreTwo = totalScore
totalScore = 0

print('Total score part I: ' + str(totalScoreOne))
print('Total score part II: ' + str(totalScoreTwo))
