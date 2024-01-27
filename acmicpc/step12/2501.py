target,order = map(int,input().split())
sequence = 0
#n 번째 약수 구하기
for i in range(1,target+1) :
    if target%i == 0 : 
        sequence += 1
        if(sequence == order) :
            print(i)
            break
#n번째 약수가 없는 경우
if sequence < order :
    print(0)