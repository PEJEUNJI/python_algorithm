
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597    
number = int(input())
result = []

#0번쨰는 1번 루프, 1번째는 2번 루프 따라서 +1
for index in range (number+1) :
    if index < 2 : result.append(index)
    #2번 index부터 n-2 + n-1규칙
    else : result.append(result[index-2] + result[index-1])

print(result[-1])