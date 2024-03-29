import random
import sys
import os
import re
import io, csv
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as pltl
from collections import defaultdict
import numpy as np
#from gui import progressbar

trials = int(sys.argv[4])

#variables
choices = []
templist = []
stLines = []
averagesList = []
#maxlengthList = []
d = defaultdict(int)

# def progress(currentValue):
#     progressbar["value"]=currentValue
#
# maxValue = trials
# currentValue=0
# progressbar["value"]=currentValue
# progressbar["maximum"]=maxValue



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
#print(sCount)
aCount = int(sys.argv[2])
#print(aCount)
tCount = int(sys.argv[3])
#print(tCount)


'''
# debug using console
sCount = int(input("S: "))
aCount = int(input("A: "))
tCount = int(input("T: "))
'''

#number of tests
for x in range(trials):
    finalList = []
    finalList2 = []
    stLines = []
    #S counter
    sCounter = sCount
    #T counter
    tCounter = tCount

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

    random.shuffle(finalList)

    #print(finalList)

    #debugging
    #print(len(sList), " ", len(aList), " ", len(tList))
    #print(finalList)

    while sCounter > 0 and tCounter > 0:

        #if there's nothing in finalList, that means all tiles glued to each other; break
        #if(len(finalList) < 2):
        #    break

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
                sCounter -= 1
                tCounter -= 1
            else:
                finalList.append(finalTempList)


    sums = 0
    maxlength = 2
    for line in stLines:
        sums += len(line)
        d[len(line)] = d[len(line)] + 1
    average = sums / len(stLines)
    #print("Average length of ST Lines: ", str(average))
    averagesList.append(average)
    #maxlengthList.append(max(stLines, key = len))
    #progress.after(100, progress(currentValue))
    #progressbar.update()
    print(finalList)
    print(stLines)
    print("Average Length of ST lines: ", str(average))

#TEST
#divide number of lines counted by number of trials to get average count


#calculate average of averages
avgSum = 0
for avg in averagesList:
    avgSum += avg
mainAverage = avgSum / len(averagesList)
print("Average of all averages: ", mainAverage)

#calculate max length of ST lines
#maxlength = max(maxlengthList, key = len)
#maxlength = len(maxlength)
#print("Max length: ", maxlength)
print("Number of lines of st length: ", sorted(d.items()))

#Sort dictionary by key, return list of tuples.
lists = sorted(d.items())
print(lists)
#Unpack a list of pairs into two tuples.
x, y = zip(*lists)

#Calculate percentages for comparison.
values = d.values()
total = sum(values)
#new = [value * 100. / total for value in values]
#print(new)

print("Length of lines and percentages:")

#for i, v in enumerate(y):
#    print(i+2, (v * 100.)/total)

#pltl.bar(x, y)
#pltl.xlabel("Length of ST Lines")
#pltl.ylabel("Number of ST Lines per Length")
#pltl.autoscale()
# fig, ax = pltl.subplots()
# ax.autoscale(enable=True)


#for i, v in enumerate(y):
#    pltl.text(i + 2, v + .22, "{0:.2f}%".format((v * 100.)/total), color='blue', fontweight='bold', size = 7)


#pltl.show()
#pltl.savefig("STSim.png")

#printing out what was chosen (debug)
# choices = random.choices(finalList, k=2)
# for choice in choices:
#    #finalList.remove(choice)
#    print(Tile.getTiletype(choice))
#print(len(finalList))


#TEST
width = 0.85
fig, ax = pltl.subplots()
rects1 = ax.bar(x, y, color='b', width=0.8)

ax.set_ylabel('Number of ST Lines per Length')
ax.set_title('Insert Title Here')
#ax.set_xticks(np.add(x,(width/2))) # set the position of the x ticks
#ax.set_xticklabels(x)
#ax.autoscale(enable=True)


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                "{0:.1f}%".format((height * 100)/total),
                ha='center', va='bottom', size=5)

autolabel(rects1)

pltl.xlabel("Length of ST Lines")
pltl.show(dpi=300)
