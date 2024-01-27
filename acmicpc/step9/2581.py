def is_prime(number):
    loop = int(number**0.5)
    if number < 2 :
        return False
    for i in range(2,loop+1) :
        #소수가 아니라는 뜻
        if number%i == 0 : 
            return False
    return True
            
start_num = int(input())
end_num  = int(input())

#first_number
#sum :  소수의 합을 저장
#list_data 소수를 저장
first_number = 0
sum = 0
for i in range(start_num, end_num+1):
    if is_prime(i) :
        first_number = i if first_number == 0 else first_number
        sum += i

if first_number == 0 : print(-1)
else :
    print(sum)
    print(first_number)
            