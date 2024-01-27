list_data=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
# 알파벳의 숫자를 구한다.
input_data = input()
phone_number = []
for c in input_data :
    phone_number.append(list_data[ord(c) - 65])
# 숫자의 길이?를 구한다.
# 1 ->2초, 2 ->2초 +1 3->2초 +1+1, 4->2초 +1+1+1
sum = 0
for i in phone_number :
    sum += 2 + i-1
    
print(sum)