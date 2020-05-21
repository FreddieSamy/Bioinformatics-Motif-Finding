def consensusScore(strings):
    dic={'a':0,'c':0,'t':0,'g':0}
    profileMatrix=list()
    for i in range(len(strings[0])):
        profileMatrix.append(dic.copy())
    #profileMatrix[#digit][#char]
    #profileMatrix[0]['c']
    for i in strings:
        for j in range(len(i)):
            profileMatrix[j][i[j]]+=1
    cosensusString=""
    score=0
    for i in profileMatrix:
        for char, num in i.items():
            if num == max(i.values()):
                cosensusString+=char
                score+=num
                break #make only one possible solution
                      #if there exist multiple Maximum values .. it will take first one only
    return cosensusString,score

############################################################################################
    
def motifFinding(L,n,t,DNAs):
    s=""
    for i in range(n-L+1): #to get string with all possible starting positions
        s+=str(i)
    import itertools
    startingPoints=list(itertools.product(s,repeat=t))
    bestCosensusString=list()
    bestScore=[0]
    bestStartingPoints=list()
    k=1
    for i in startingPoints:
        print(f"{k/len(startingPoints)*100:.1f} %")
        strings=list()
        for j in range(len(i)):
            strings.append(DNAs[j][int(i[j]):int(i[j])+L])
        tempConsensusString,tempScore=consensusScore(strings)
        if tempScore>bestScore[0]:
            bestScore=[tempScore]
            bestCosensusString=[tempConsensusString]
            bestStartingPoints=[i]
        #this block to get equal highest scores
        '''elif tempScore==bestScore[0]:
            bestScore.append(tempScore)
            bestCosensusString.append(tempConsensusString)
            bestStartingPoints.append(i)'''
            
        k+=1
    return bestCosensusString,bestScore,bestStartingPoints

############################################################################################
    
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

cosensusString,score,startingPoints=motifFinding(8,len(DNAs[0]),len(DNAs),DNAs)
for i in range(len(cosensusString)):#if we wanna get equal highest scores
    print("\ncosensusString "+str(i+1)+" : ",cosensusString[i])
    print("score :",score[i])
    print("startingPoints :",startingPoints[i])
