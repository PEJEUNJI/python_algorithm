target = int(input())
startNo = 2
loop = 1 
endNo = 6*loop -1 + startNo

if(target == 1) :
    print(1)
else :
    while not(startNo<=target and target<=endNo) :
        startNo = endNo + 1
        loop += 1
        endNo = 6*loop -1 + startNo

print(loop+1)