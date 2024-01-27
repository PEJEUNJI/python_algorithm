loop = int(input())
input_data = sorted(map(int,input().split()))

result_data = [0]
for index,value in enumerate(input_data) :
    result_data.append(result_data[index] + value)
    
print(sum(result_data))