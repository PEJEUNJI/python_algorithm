input_data = sorted(map(int,input().split()))

while input_data[0] + input_data[1] <= input_data[2] :
    input_data[2] -= 1
    input_data.sort()
    
print(sum(input_data))
