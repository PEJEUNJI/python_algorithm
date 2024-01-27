list = [10,5,8,6,7,9,1,2,3,4]

def merge_divide(target_list):
    if len(target_list) <= 1 : 
        return target_list

    mid_index  =  len(target_list) // 2

    left = target_list[:mid_index]
    right = target_list[mid_index:]

    #계속해서 호출하면서 반씩 나눈다.
    #시간 복잡도는  O(n log n) -> 높이가 2의 제곱근만큼만 필요
    left = merge_divide(left)
    right = merge_divide(right)

    return merge(left, right)



def merge(left, right):
    result = []
    right_index, left_index = 0,0
    left_legth = len(left)
    right_legth = len(right)

    #오른쪽 , 왼쪽 배열을 비교해서 작은값만 result에 넣는다
    while right_index < right_legth and left_index < left_legth :
        if left[left_index] < right[right_index] :
            result.append(left[left_index])
            left_index += 1
        else :
            result.append(right[right_index])
            right_index += 1
    #남은 값들을 left먼저 추가
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

print(merge_divide(list))


