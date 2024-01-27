
import sys
loop,target  = map(int,sys.stdin.readline().split())


input_data = list((map(int,sys.stdin.readline().split())))
input_data.sort(reverse=True)

max_result = 0
for first in range(loop) :
    for second in range (first+1, loop) :
        for third in range (second +1, loop) :
           result = sum([input_data[first],input_data[second],input_data[third]])
           if result <= target :
                 if max_result < result :
                    max_result = result 
                  
print(max_result)                
