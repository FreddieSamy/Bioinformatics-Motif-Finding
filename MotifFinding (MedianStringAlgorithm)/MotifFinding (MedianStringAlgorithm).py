def minHammingDistance(DNA,String):
    #return startingPosition,hammingDistance
    hammingDistance=len(String)
    startingPosition=-1
    for i in range(len(DNA)-len(String)+1):
        tempHammingDistance=0
        for j in range(len(String)):
            if DNA[i+j].lower()!=String[j].lower():
                tempHammingDistance+=1
        if tempHammingDistance<hammingDistance:
            hammingDistance=tempHammingDistance
            startingPosition=i
    return startingPosition,hammingDistance

###########################################################################################

def MedianString(DNAs,L):
    import itertools
    Strings=list(itertools.product("actg",repeat=L))
    bestTotalDistance=len(Strings[0])
    bestStartingPositions=list()
    bestString=""
    k=1
    for j in Strings:
        print(f"{k/len(Strings)*100:.1f} %")
        totalDistance=0
        startingPositions=list()
        for i in DNAs:
            temp,temp2=minHammingDistance(i,j)
            startingPositions.append(temp)
            totalDistance+=temp2
        if totalDistance<bestTotalDistance:
            bestTotalDistance=totalDistance
            bestStartingPositions=startingPositions.copy()
            bestString=j
        k+=1
    return "".join(bestString),bestTotalDistance,bestStartingPositions

###########################################################################################
f=open("DNA Sequences.txt","r")
DNAs=list()
for i in f:
    i=i.strip()
    i=i.strip("\n")
    i=i.lower()
    if len(i)==0:
        continue
    DNAs.append(i)
f.close()
bestString,bestTotalDistance,bestStartingPositions=MedianString(DNAs,8)
print("bestString : ",bestString)
print("bestTotalDistance : ",bestTotalDistance)
print("bestStartingPositions : ",bestStartingPositions)

