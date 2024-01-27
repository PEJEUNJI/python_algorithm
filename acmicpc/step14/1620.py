import sys
input_data_len, target_data_len  = map(int,sys.stdin.readline().split())
#index, value
input_data = {}
#value, index
input_data_reverse = {}

for index in range(1,input_data_len+1):
    value = sys.stdin.readline()
    input_data[index] = value
    input_data_reverse[value] = index

for _ in range (target_data_len) :
    value = sys.stdin.readline()
    #입력값이 숫자인 경우
    try :
        print(input_data[int(value)])
    #입력값이 문자인 경우
    except Exception :
        print(input_data_reverse[value])