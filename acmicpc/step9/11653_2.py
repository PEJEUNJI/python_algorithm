target = int(input())

loop = int(target**0.5)

for i in range(2,loop+2) :
    while target%i == 0 :
        print(i)
        target //=i

if target != 1 : print(target)