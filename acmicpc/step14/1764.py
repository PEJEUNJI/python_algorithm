import sys
#한줄 패스
first,second = map(int,sys.stdin.readline().split())
input_diction = {}

#key값이 중복되는 경우엔 value를 늘린다
count = 0
for _ in range(first+second) :
    data = sys.stdin.readline().strip()
    if data in input_diction.keys() :
        count += 1 #명단수 카운트
        input_diction[data] += 1
    else :
        input_diction[data] = 1

#key기준으로 정렬
sorted_diction = dict(sorted(input_diction.items(), key=lambda data :data[0]))

print(count)
for key,value in sorted_diction.items() :
    #value 2보다 큰 경우    
    if value == 2 : 
        #key를 출력
        print(key)
