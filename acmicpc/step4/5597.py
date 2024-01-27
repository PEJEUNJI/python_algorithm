import sys

list_data = [0 for _ in range(1,31)]

for i in sys.stdin :
    list_data[int(i)-1] = 1
    
seq = 0
for i in list_data :
    seq += 1
    if int(i)==0 :
        print(' '.join(map(str,[seq])))