DNA=input("enter DNA sequance : ")
Motif=input("enter a motif : ")
hammingDistance=len(Motif)
pos=-1
for i in range(len(DNA)-len(Motif)+1):
    tempHammingDistance=0
    for j in range(len(Motif)):
        if DNA[i+j].lower()!=Motif[j].lower():
            tempHammingDistance+=1
    if tempHammingDistance<hammingDistance:
        hammingDistance=tempHammingDistance
        pos=i
print("Motif is : "+DNA[pos:pos+len(Motif)])
print("at starting position : "+str(pos))
print("with number of mutations : "+str(hammingDistance))
