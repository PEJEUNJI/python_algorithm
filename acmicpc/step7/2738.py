import sys
n,m = map(int,input().split())
length = n*m

first_data =[]
second_data=[]
for index,data in enumerate(sys.stdin):
    if(index < n) :
        first_data += list(map(int,data.split()))
    elif(index >= n) :
        second_data += list(map(int,data.split()))

total_data = [first + second for first, second in zip(first_data,second_data)]

for i in range(0,length,3):
    print(' '.join(map(str,total_data[i:i+3])))

