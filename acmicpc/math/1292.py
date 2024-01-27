import sys
start,end = map(int,sys.stdin.readline().split())

number_list = []
number = 1
loop = 0
#end숫자랑 같아지면 더이상 리스트를 만들지 않는다.
while not loop == end :
    for _ in range (number) :
        #number만큼 number를 list에 넣는다
        number_list.append(number)
        loop += 1
        #end숫자랑 같아지면 더이상 리스트를 만들지 않는다.
        if loop == end : break
    number += 1

print(sum(number_list[start-1:end]))
    