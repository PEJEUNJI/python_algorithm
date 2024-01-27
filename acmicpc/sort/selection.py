list = [10,5,8,6,7,9,1,2,3,4]

length = len(list)
min_index = 0
for first in range (length) :
    min_num = max(list)
    #가장 작은 값을 앞으로 보내면서 순환, 시간 복잡도 : n*n
    #다음 탐색은 가장 값 뒤부터 이뤄줘야 하므로, range (first,length) 설정
    for second in range (first,length) :
        #가장 작은 값을 찾는 로직, 해당 index도 기억해야 함
        if min_num > list[second] :
            min_num = list[second]
            min_index = second
    #가장 작은 값을 찾았으면 현재 index와 교환해줘야 함
    list[first],list[min_index] = list[min_index],list[first]

print(list)