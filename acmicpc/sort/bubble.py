list = [10,5,8,6,7,9,1,2,3,4]

length = len(list)
for first in range (length) :
    #가장 큰 값을 뒤로 보내면서 순환, 시간 복잡도 : n*n
    for second in range (length-first-1) :
        if list[second] > list[second+1] :
            list[second],list[second+1] = list[second+1],list[second]

print(list)