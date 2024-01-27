input()

input_data = list(map(int,input().split()))
sorted_data = sorted(set(input_data))
result_data = []
#input_data[i]의 데이터를 sorted_data 에서 찾아서 인덱스 출력

# 딕셔너리를 생성하여 각 값의 인덱스 저장
index_dict = {value: index for index, value in enumerate(sorted_data)}

# 시간 복잡도 O(n)
result_data = [index_dict[value] for value in input_data]

print(*result_data,sep=' ')