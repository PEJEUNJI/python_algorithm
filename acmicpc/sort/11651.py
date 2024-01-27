import sys
loop  = int(input())
input_data = []
for data in sys.stdin :
    x,y = map(int,data.split())
    input_data.append((x,y))

sorted_data = sorted(input_data, key=lambda data : (data[1],data[0]))

for data in sorted_data :
    print(data[0],data[1])