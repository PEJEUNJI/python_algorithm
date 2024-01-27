
import sys
length, loop = map(int,sys.stdin.readline().split())
list_data = [i for i in range(1,length+1)]

for i in sys.stdin :
    
    num1, num2 = map(int,i.split())

    list_data[num1-1],list_data[num2-1] = list_data[num2-1],list_data[num1-1]
   

print(*list_data)