import sys
loop = int(input())
input_data = []
for line in range(loop) :
    x,y = map(int,input().split())
    input_data.append((x,y))
    
sorted_data = sorted(input_data, key=lambda point : (point[0],point[1]))

for data in sorted_data :
    print(data[0],data[1])