
#diction이용, 저장시 중복제거
#길이가 짧은거부터 나열 , 같으면 사전순, key에 값을 넣고, value에 길이를 넣고, sort 처리
#사전순은 유니코드로 확인

loop = int(input())
input_data = {}

#길이가 짧은거부터 나열 , 같으면 사전순, key에 값을 넣고, value에 길이를 넣고, sort 처리
for _ in range (loop) :
    value = input()
    input_data[value] = len(value)
    
input_data = sorted(input_data.items(), key=lambda item: item[1])
length = len(input_data)

def get_count_value(target):
    return sum(1 if value == target else 0 for key, value in input_data)

def resorted(start,end,input_data) :
    part_to_sort = input_data[start:end]

    # 특정 인덱스부터 끝까지의 키를 기준으로 정렬
    part_sorted = sorted(part_to_sort, key=lambda item: item[0])

    # 앞부분과 정렬된 부분을 합쳐서 새로운 리스트 생성
    input_data = input_data[:start] + part_sorted + input_data[end:]
    return input_data

index = 0
while(index < length) :
    #같은 길이의 데이터가 있는지 확인
    index_key,index_value = input_data[index]
    same_count = get_count_value(index_value)
    if same_count > 1 : 
        #비교 값까지 포함된 갯수를 넘긴다
        input_data = resorted(index,index+same_count,input_data)
        index += same_count
    else : index += 1  


for key,value in input_data :
    print(key)
