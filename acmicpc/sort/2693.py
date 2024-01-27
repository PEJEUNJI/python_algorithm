
import sys
loop = int(sys.stdin.readline().strip())

#역 정렬을 위한 함수
def getSortList(list):
    length = len(list)
    #버블정렬
    for first in range (length) :
        #한번 정렬 한 후에는 루프 횟수를 점점 줄이면서 앞의 남은 원소들을 정렬
        for second in range (length-first-1) :
            if list[second] < list[second +1] : 
                list[second],list[second +1] = list[second+1],list[second]
    return list
                
for _ in range(loop) :
    input_data = list(map(int,sys.stdin.readline().split()))
    print(getSortList(input_data)[2])
    
