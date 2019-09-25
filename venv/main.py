import random
import sys
import os
import re
import io, csv
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as pltl
from collections import defaultdict

#variables
choices = []
templist = []
stLines = []
averagesList = []
maxlengthList = []
d = defaultdict(int)

#tile class with tile type and glues
class Tile:
    def __init__(self, tileType, westGlue, eastGlue):
        self.tileType = tileType
        self.eastGlue = eastGlue
        self.westGlue = westGlue
    def __str__(self):
        return "Tile Type: " + self.tileType + "\n" + "West Glue: " + self.westGlue + "\n" + "East Glue: " + self.eastGlue
    def __repr__(self):
        return self.tileType
    def __len__(self):
        return 1
    def getTiletype(self):
        return self.tileType
    def getWestGlue(self):
        return self.westGlue
    def getEastGlue(self):
        return self.eastGlue

def tilesCanBeGlued(_choices):
    #global choices
    global choices
    #check for list cases
    #case for if a list is the first choice only
    if (isinstance(_choices[0], list) and not isinstance(_choices[1], list)):
        if(_choices[0][-1].getEastGlue() == _choices[1].getWestGlue() and _choices[0][-1].getEastGlue != ""
                and _choices[1].getWestGlue() != ""):
            return True
        elif(_choices[1].getEastGlue() == _choices[0][0].getWestGlue() and _choices[1].getEastGlue() != ""
                and _choices[0][0].getWestGlue() != ""):
            #rearrange tiles
            #debug
            #print(choices[0], choices[1])
            choices = [_choices[1], _choices[0]]
            return True
        else:
            return False
    #case if list is only second choice
    if (not isinstance(_choices[0], list) and isinstance(_choices[1], list)):
        if(_choices[0].getEastGlue() == _choices[1][0].getWestGlue() and _choices[0].getEastGlue != ""
                and _choices[1][0].getWestGlue() != ""):
            return True
        elif(_choices[1][-1].getEastGlue() == _choices[0].getWestGlue() and _choices[1][-1].getEastGlue() != ""
                and _choices[0].getWestGlue() != ""):
            #rearrange tiles
            #debug
            #print(choices[0], choices[1])
            choices = [_choices[1], _choices[0]]
            return True
        else:
            return False
    #case if both choices are lists
    if (isinstance(_choices[0], list) and isinstance(_choices[1], list)):
        if(_choices[0][-1].getEastGlue() == _choices[1][0].getWestGlue() and _choices[0][-1].getEastGlue != ""
                and _choices[1][0].getWestGlue() != ""):
            return True
        elif(_choices[1][-1].getEastGlue() == _choices[0][0].getWestGlue() and _choices[1][-1].getEastGlue() != ""
                and _choices[0][0].getWestGlue() != ""):
            #rearrange tiles
            #debug
            #print(choices[0], choices[1])
            choices = [_choices[1], _choices[0]]
            return True
        else:
            return False

    #case for two single tiles
    if (_choices[0].getEastGlue() == _choices[1].getWestGlue() and _choices[0].getEastGlue() != "" and _choices[
        1].getWestGlue() != ""):
        return True
    elif (_choices[1].getEastGlue() == _choices[0].getWestGlue() and _choices[1].getEastGlue() != "" and _choices[
        0].getWestGlue() != ""):
        # rearrange both tiles
        # debug
        #print(choices[0], choices[1])
        choices = [_choices[1], _choices[0]]
        return True
    else:
        return False


#tile type, and east or west glues FOR THIS SPECIFIC SIMULATION CASE
S = Tile("S", "", "a")
A = Tile("A", "a", "a")
T = Tile("T", "a", "")

#grab values from gui
#gather counts for the tile types
sCount = int(sys.argv[1])
print(sCount)
aCount = int(sys.argv[2])
#print(aCount)
tCount = int(sys.argv[3])
#print(tCount)

'''
# debug using console
sCount = input("S: ")
aCount = input("A: ")
tCount = input("T: ")
'''

#number of tests
for x in range(1000):
    finalList = []
    finalList2 = []
    stLines = []

    #place that many tiles into its respective list
    #S list
    for tileCount in range(int(sCount)):
        finalList.append(S)
    #A list
    for tileCount in range(int(aCount)):
        finalList.append(A)
    #T list
    for tileCount in range(int(tCount)):
        finalList.append(T)

    #print(finalList)

    #debugging
    #print(len(sList), " ", len(aList), " ", len(tList))
    #print(len(finalList))

    for n in range((sCount + tCount) * aCount):

        #if there's nothing in finalList, that means all tiles glued to each other; break
        if(len(finalList) < 2):
            break

        #loop selecting two items at random from the list
        choices = random.sample(finalList, 2)

        #can they be glued together?
        if tilesCanBeGlued(choices):
            #Glue both tiles, and put them back into final list.
            #Note that each side is glued to the other tile, updating this info.
            #put into list, then stick inside final list.
            templist = choices
            #remove choices from finalList
            for choice in choices:
                finalList.remove(choice)
            #create one full array from templist, if templist contains a list
            finalTempList = []
            if(isinstance(templist[0], list) or isinstance(templist[1], list)):
                for set in choices:
                    if(isinstance(set, list)):
                        for tile in set:
                            finalTempList.append(tile)
                    else:
                        finalTempList.append(set)
            else:
                finalTempList = templist

            #if we glue two things together, and it becomes an ST line, send it to an ST line list
            if(finalTempList[0].getTiletype() == "S" and finalTempList[-1].getTiletype() == "T"):
                stLines.append(finalTempList)
            else:
                finalList.append(finalTempList)


    sum = 0
    maxlength = 2
    for line in stLines:
        sum += len(line)
        # if len(line) > maxlength:
        #     maxlength = len(line)
        #Depending on len(line), add one to their respective number in list.
        d[len(line)] = d[len(line)] + 1
    average = sum / len(stLines)
    #print("Average length of ST Lines: ", str(average))
    averagesList.append(average)
    maxlengthList.append(max(stLines, key = len))

#calculate average of averages
avgSum = 0
for avg in averagesList:
    avgSum += avg
mainAverage = avgSum / len(averagesList)
print("Average of all averages: ", mainAverage)

#calculate max length of ST lines
maxlength = max(maxlengthList, key = len)
maxlength = len(maxlength)
print("Max length: ", maxlength)
print("Number of lines of st length: ", d.items())

plt.plot(range(2, maxlength+1), d)
plt.show()

#printing out what was chosen (debug)
# choices = random.choices(finalList, k=2)
# for choice in choices:
#    #finalList.remove(choice)
#    print(Tile.getTiletype(choice))
#print(len(finalList))
