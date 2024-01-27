
loop,target = map(int,input().split())

input_data = sorted([int(input()) for _ in range(loop)],reverse = True)
input_data.sort(reverse=True)
count = 0
for value in input_data :
    if value <= target :
        count += target // value
        target %= value
    if target == 0 : break
        
print(count)