loop = int(input())
input_data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result= []

def dfs(count, now):
    global Max, Min, add, sub, mul, div
  
    if count == loop:
        result.append(now)
    else:
        if add > 0:
            add -= 1
            dfs(count+1, now + input_data[count])
            #재귀 호출이 끝나고 나면 새로운 연산을 위해서 복구 시켜줘야 함
            add += 1
        if sub > 0:
            sub -= 1
            dfs(count+1, now - input_data[count])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(count+1, now * input_data[count])
            mul += 1
        if div > 0:
            div -= 1
            dfs(count+1, int(now / input_data[count]))
            div += 1
            
dfs(1, input_data[0])
  
print(max(result))
print(min(result))