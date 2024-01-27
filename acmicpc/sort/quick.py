list = [10,5,8,6,7,9,1,2,3,4]

#평균적인 경우, 퀵 정렬의 시간 복잡도는 O(n log n)이지만
#피벗의 값이 최소값, 최대값이 되는 경우는 최악의 경우에는 O(n^2)가 될수 있다.
def quickSort(target_list) :
    if len(target_list) <= 1 : return target_list
    #중간값을 기준값으로 설정
    pivot = target_list[len(target_list)//2]
    #기준값보다 작은 값들을 추출
    left = [value for value in target_list if value < pivot]
    #기준값과 같은 값들을 추출
    middle = [value for value in target_list if value == pivot]
    #기준값보다 큰 값들을 추출
    right = [value for value in target_list if value > pivot]

    #반복해서 정렬
    return quickSort(left) + middle + quickSort(right)

print(quickSort(list))

