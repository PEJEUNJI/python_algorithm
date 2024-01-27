import sys

input_data = []
for value in sys.stdin :
    input_data.append(int(value.strip()))

input_data.sort(reverse=True)
#전체 합에서 2명을 뺐을때 100이 나오면 됨
total = sum(input_data)
for first in range(9) :
    for second in range(first+1, 9) :
        if total-(input_data[first] + input_data[second]) == 100 :
            #index는 큰값부터 제거
            if first > second : 
                input_data.pop(first)
                input_data.pop(second)
            else :
                input_data.pop(second)
                input_data.pop(first)
            input_data.sort()
            print(*input_data,sep='\n')
            sys.exit()
        
    