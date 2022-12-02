#!/usr/bin/python3

#############################
#
# AOC Day two
#
##############################

#A Rock  1
#B Paper 2
#C Scissors 3
#X Rock  1
#Y Paper 2
#Z Scissors  3

#Lose
#A Z 3 
#B X 1
#C Y 2
#Win
#A Y 2 
#B Z 3
#C X 1
#Draw
#A X 1
#B Y 2
#C Z 3

def dataset():
   with open('input.txt') as f:
        lines = f.readlines()
        f.close()
        return lines

game = dataset();

lose = [['AZ',3,],['BX',1],['CY',2]]
win = [['AY',2],['BZ',3],['CX',1]]
draw = [['AX',1],['BY',2],['CZ',3]]

# Test
#game = [['AY'],['BX'],['CZ']]

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
                print("Win:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))
    elif drawres == True:
        for idx, match in enumerate(draw):
            if str(match[0]) == roundStr:
                shapeScore = int(match[1]) 
                roundScore = shapeScore + 3
                totalScore = totalScore + roundScore
                print("Draw:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))
    elif losres == True:
        for idx, match in enumerate(lose):
            if str(match[0]) == roundStr:
                shapeScore = int(match[1]) 
                roundScore = shapeScore + 0
                totalScore = totalScore + roundScore
                print("Lose:" + str(shapeScore) +" "+ str(roundScore) + " "+ str(totalScore))
