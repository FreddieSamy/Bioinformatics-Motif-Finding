def motifFinding(L,n,t,DNAs):
    startingPositions="0"*L #to get first starting positions then 
    
    
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
