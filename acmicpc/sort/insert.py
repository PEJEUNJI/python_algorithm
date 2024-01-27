list = [1,10,2,5,2,6,7]

length = len(list)

#시간복잡도 : n*n (버블, 선택 중에선 가장 빠름, 거의 정렬이 되어 있는 경우는 변경하는 경우가 적으므로)\
#삽입 >선택>버블 : 효율적인 순
for index in range (length) :
    inner_index = index
    # 내 앞엔 무족건 정렬 됐다는 전제하에 내앞의 값들을 비교하면서 자리 이동
    while inner_index > 0 and list[inner_index-1] > list[inner_index] :
        list[inner_index] , list[inner_index-1]  = list[inner_index-1] ,list[inner_index] 
        inner_index -= 1

print(list)
