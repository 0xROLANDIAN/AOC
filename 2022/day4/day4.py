#!/usr/bin/python3
import string
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

for items in assignments:
    #print(items)
    #split item on string
    item = list(items.split(","))
    firstPair = item[0].split("-")
    secondPair = item[1].split("-")
    taskrangeFirst =  list(range(int(firstPair[0]), int(firstPair[1])))
    taskrangeSecond =  list(range(int(secondPair[0]), int(secondPair[1])))
    print(str(taskrangeFirst).strip(',')+ ' ' + str(taskrangeSecond).strip(','))
    common = ''.join(set(str(taskrangeFirst)).intersection(str(taskrangeSecond)))
    print(common)
    print(common.strip("[],"))
