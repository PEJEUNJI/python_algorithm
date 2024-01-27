list_data = [-1 for _ in range(1,27)]
input_data = input()

seq = 0
for i in input_data : 
    print(i)
    if list_data[ord(i) - 97] == -1 :
        list_data[ord(i) - 97] = seq
    seq += 1
    
print(*list_data)
