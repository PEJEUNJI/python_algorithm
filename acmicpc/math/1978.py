import sys
count = int(sys.stdin.readline().strip())
input_data = (list(map(int,sys.stdin.readline().split())))

def isPrime(value):
    #value가 0,1 인 경우는 소수에 들어가지 않으므로 패스
    if value < 2 : return False
    #자기 자신은 들어가지 않도록 설정
    else :
        #제곱근까지만 확인하면 된다, 소수가 아니라면 제곱근 이하의 약수가 반드시 존재한다
        for j in range(2,int(value**0.5)+1):
            #자기 자신이 아닌 숫자로 나누어 졌으면 소수가 아니므로 for문 중단후 다음 값 진행
            if value%j == 0 : return False
    return True

print(sum(1 if isPrime(value) else 0 for value in input_data))