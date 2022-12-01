#!/usr/bin/python3

#############################
#
# AOC Day one
#
##############################

def dataset():
    with open('input.txt') as f:
        lines = f.readlines()
        f.close()
        return lines

def sumcalories(calories, elfcaloriessum):
    elflist = []
    for calorie in calories:
        if calorie == "\n":
            elflist.append(elfcaloriessum)
            elfcaloriessum = 0
        else:
            elfcaloriessum = elfcaloriessum + int(calorie)
        #f.close()
    return elflist

def topthree(elflist):
    elflist.sort()
    elflisttopthree = sum(elflist[-3:])
    elflist = []
    return elflisttopthree

def maximum(elflist):
    elf = max(elflist)
    elflist = []
    return elf

print ("Top three calories sum: " + str(topthree(sumcalories(dataset(), 0))))
print("Maximum calories in list: " + str(maximum(sumcalories(dataset(), 0))))
