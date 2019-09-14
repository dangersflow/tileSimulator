import random

#variables
choices = []
lines = []

#tile class with tile type and glues
class Tile:
    def __init__(self, tileType, westGlue, eastGlue):
        self.tileType = tileType
        self.eastGlue = eastGlue
        self.westGlue = westGlue
    def __str__(self):
        return "Tile Type: " + self.tileType + "\n" + "West Glue: " + self.westGlue + "\n" + "East Glue: " + self.eastGlue
    def getTiletype(self):
        return self.tileType
    def getWestGlue(self):
        return self.westGlue
    def getEastGlue(self):
        return self.eastGlue

def tilesCanBeGlued(_choices):
    if (_choices[0].getEastGlue() == _choices[1].getWestGlue() and _choices[0] != ""):
        return True
    elif(_choices[1].getEastGlue() == _choices[0].getWestGlue() and _choices[0] != ""):
        #rearrange both tiles
        global choices
        #debug
        print(choices[0], choices[1])
        choices = [_choices[1], _choices[0]]
        return True
    else:
        return False


        #tile type, and east or west glues FOR THIS SPECIFIC SIMULATION CASE
S = Tile("S", "", "a")
A = Tile("A", "a", "a")
T = Tile("T", "a", "")

#gather counts for the tile types
sCount = input("Enter S count: ")
aCount = input("Enter A count: ")
tCount = input("Enter T count: ")

#place that many tiles into its respective list
#S list
sList = []
for tileCount in range(int(sCount)):
    sList.append(S)
#A list
aList = []
for tileCount in range(int(aCount)):
    aList.append(A)
#T list
tList = []
for tileCount in range(int(tCount)):
    tList.append(T)
#concat all lists into a final big list
finalList = sList + aList + tList

#debugging
print(len(sList), " ", len(aList), " ", len(tList))
print(len(finalList))

#select two items at random from the list
choices = random.choices(finalList, k=2)

#can they be glued together?
if tilesCanBeGlued(choices):
    
#printing out what was chosen (debug)
for choice in choices:
    finalList.remove(choice)
    print(choice)
print(len(finalList))