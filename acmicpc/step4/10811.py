import sys

length,_ = map(int, sys.stdin.readline().split())


list_data = [i for i in range(1,length+1)]

for i in sys.stdin :
    start_index, end_index = map(int,i.split())
    list_data[start_index-1:end_index]  = list_data[start_index-1:end_index][::-1]

print(*list_data)
    
    