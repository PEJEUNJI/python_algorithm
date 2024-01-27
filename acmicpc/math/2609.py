import sys

num1, num2 = map(int,sys.stdin.readline().split())

minnum = min(num1, num2)
num3, num4 =  num1, num2

GCD  = 1

#작은 수로 루프를 돌면서 나머지가 0인수로 약수를 찾아서 약수를 곱하면 최대 공약수
for index in range(2, minnum + 1) :
    #이미 했던 index도 또 나누어 질수 있으므로 반복 해야 함
    while num1 % index == 0 and num2 % index == 0 :
        GCD *= index 
        num1 = num1 // index
        num2 = num2 // index
print(GCD)
#최대 공약수에 나누고 남은 몫을 곱하면 최소 공배수
print(GCD*num1*num2)