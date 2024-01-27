import sys
input_loop = sys.stdin.readline().strip()
input_data = {}

for key in sys.stdin.readline().split() :
    #이미 key값이 존재하면 value 값을 1 늘린다
    if key in input_data.keys() :
        input_data[key] += 1
    else : input_data[key] = 1

target_loop = sys.stdin.readline().strip()
target_data = sys.stdin.readline().split()

for value in target_data :
    try :
        print(input_data[value],end=' ')
    except Exception :
        print(0,end=' ')
        
    

