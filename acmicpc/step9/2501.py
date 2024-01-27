target,order = map(int,input().split())
sequence = 0
for i in range(1,target+1) :
    if target%i == 0 : 
        sequence += 1
        if(sequence == order) :
            print(i)
            break

if sequence < order :
    print(0)