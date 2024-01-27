target_num = int(input())
n = 1
while n < target_num and target_num - n > n :
    target_num -=  n
    n += 1
    
print(n)

