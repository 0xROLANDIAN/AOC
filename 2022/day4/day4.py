#!/usr/bin/python3
import string
import re
#############################
#
# AOC Day Four
#
##############################

def dataset():
    with open('input.txt') as f:
        lines = f.read().splitlines() 
        f.close()
        return lines

assignments = dataset()
totalMatch = 0
totalOverlap = 0

for items in assignments:
    item = list(items.split(","))
    firstPair = item[0].split("-")
    secondPair = item[1].split("-")
    taskLeft = set(range(int(firstPair[0]),int(firstPair[1])+1))
    taskRight = set(range(int(secondPair[0]),int(secondPair[1])+1))
    common = taskLeft.intersection(taskRight)
    isEmpty = (len(common) == 0)
    if isEmpty:
        print("Set is empty")
    else:
        totalOverlap = totalOverlap + 1
        print(str(taskLeft) + ' ' + str(taskRight))
        result = taskLeft.union(taskRight)
        if result == taskLeft or result == taskRight:
            totalMatch = totalMatch + 1
print('Total Match of range within range is: ' + str(totalMatch))
print('Total Match of range overlaps is: ' + str(totalOverlap))

