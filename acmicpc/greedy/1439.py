target = input()
#list에 연속된 숫자가 나올때마다 숫자를 저장 1,0,1,0 식으로
#count결과가 작은것이 정답
count_repeated = []
length = len(target)
previous_ch = None
for index, ch in enumerate(target) :
    if previous_ch != None and previous_ch != ch :
        count_repeated.append(previous_ch)
    if index == length - 1 :
        count_repeated.append(ch)
    previous_ch  = ch

print(count_repeated)

print(min(count_repeated.count('1'),count_repeated.count('0')))