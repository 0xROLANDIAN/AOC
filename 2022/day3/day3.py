#!/usr/bin/python3
import string
#############################
#
# AOC Day Three
#
##############################

def dataset():
    with open('input.small.txt') as f:
        lines = f.read().splitlines() 
        f.close()
        return lines

totalScore = 0
rucksack = dataset()
alphabetLower = list(string.ascii_lowercase)
alphabetUpper = list(string.ascii_uppercase)

for items in rucksack:
    splitIndex = round(len(items)/2)
    cmptOne = items[:splitIndex]
    cmptTwo = items[splitIndex:]
    resultList = ''.join(
    set(cmptOne).intersection(cmptTwo)
    )
    if len(resultList) != 0:
        if str(resultList[0]).islower() is True:
            lowerindex = alphabetLower.index(resultList[0]) + 1
            #print('lowercase score:' + str(resultList[0]) + ' ' + str(lowerindex))
            totalScore = totalScore + lowerindex
        else:
            upperindex = alphabetUpper.index(resultList[0]) + 27
            #print('uppercase score:' + str(resultList[0]) + ' ' + str(upperindex))
            totalScore = totalScore + upperindex

print('Total Score for an item in both rucksacks: ' + str(totalScore))

elfGroups = []
totalScore  = 0

for i in range(0, len(rucksack), 3):
    elfGroups.append(rucksack[i:i + 3])

for elfGroup in elfGroups:
    #print ('elf group: ' + str(elfGroup));
    try:
        common = ''.join(set(elfGroup[0]).intersection(elfGroup[1],elfGroup[2])) 
        #print(common + ' : ' + str(lowerindex)) 
        if str(common).islower() is True:
            lowerindex = alphabetLower.index(common) + 1
            #print('lowercase score:' + str(resultList[0]) + ' ' + str(lowerindex))
            totalScore = totalScore + lowerindex
            print(common + ':' + str(lowerindex))
        else:
            upperindex = alphabetUpper.index(common) + 27
            #print('uppercase score:' + str(resultList[0]) + ' ' + str(upperindex))
            totalScore = totalScore + upperindex
            print(common + ':' + str(upperindex))
    except:
            print("error")

print('Total Score for an item in three rucksacks: ' + str(totalScore))
