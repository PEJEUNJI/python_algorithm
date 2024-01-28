import sys
loop = int(sys.stdin.readline().strip())

input_data = list(map(int,sys.stdin.readline().split()))
add,sub,mul,div = map(int,sys.stdin.readline().split())
#결과를 저장할 set
result = set()

#count: 연산의 횟수가 loop 같아지면 연산결과를 저장, 1부터 시작 , 최초값은 total에 입력해서 전달
#count를 1씩 증가하고, total에는 연산 결과를 입력한다.
def recur(count,total):
    global add,sub,mul,div
    if count == loop :
        result.add(total)
    else :
        if add > 0 :
            add -= 1
            recur(count+1,total + input_data[count])
            #다음 재귀 호출을 위해 원복
            add += 1
        if sub > 0 :
            sub -= 1
            recur(count+1,total - input_data[count])
            sub += 1
        if mul > 0 :
            mul -= 1
            recur(count+1,total * input_data[count])
            mul += 1
        if div > 0 :
            div -= 1
            recur(count+1,int(total / input_data[count]))
            div += 1

recur(1,input_data[0])

print(max(result))
print(min(result))
    