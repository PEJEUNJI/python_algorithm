
import sys
start = int(sys.stdin.readline().strip())
end = int(sys.stdin.readline().strip())

prime_list = []

def isPrime(number) :
    if number < 2 : return False
    else :
        for index in range (2,int(number**0.5)+1) :
            if number % index == 0 : return False
    return True

#true인 경우만 list에 담는다 
prime_list = [value for value in range(start, end+1) if isPrime(value)]

if len(prime_list) > 0 :
    print(sum(prime_list))
    print(min(prime_list))
else : print(-1)