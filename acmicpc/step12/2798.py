loop,target = map(int,input().split())

input_data = sorted(map(int,input().split()),reverse = True)
max_result = 0
result = 0
for i in range (loop-2) :
    for j in range (i+1,loop-1) :
        for k in range (j+1, loop) :
            result = sum([input_data[i],input_data[j],input_data[k]])
            if result <=target : 
                if max_result < result : 
                    max_result = result
                    break


print(max_result)