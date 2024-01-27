
loop = int(input())
input_data = []

for _ in range (loop) :
    input_data.append(input())
    
input_data = sorted(set(input_data))
input_data.sort(key=len)

print(*input_data,sep='\n')
