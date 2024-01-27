import sys
loop = int(input())
input_data = []
for index,value in enumerate(sys.stdin) :
    age, name = map(str,value.split())
    input_data.append((int(age), name, index))
    
sorted_data = sorted(input_data, key=lambda data : (data[0],data[2],data[1]))

for data in sorted_data :
    print(data[0],data[1])
    