target = int(input())

#넘버를 2부터 나누기 시작,나머지가 0인 경우만 출력

list_prime = []
def get_prime (number):
    primes = [True] * (number + 1)
    primes[0] = primes[1] = False

    loop = int(number**0.5)
    for i in range (2,loop+1) :
        if primes[i] :
            for j in range(i*i,number+1,i) :
                primes[j] = False

    return [num for num in range (number+1) if primes[num]]

go_flag = True
if target == 1 : 
    go_flag = False

i = 0  
if go_flag : 
    list_prime = get_prime(target)

while go_flag :
    
    if target%list_prime[i] == 0 :
        target //= list_prime[i]
        print(list_prime[i])
    else :
        i += 1

    if target in list_prime :
        print(target)
        break

    if target < 2 : break
    