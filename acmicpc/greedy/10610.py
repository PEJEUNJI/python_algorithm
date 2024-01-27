target = sorted([ch for ch in input()],reverse = True)

#0이 없으면 30의 배수가 될수 없음
if '0' not in target : 
    print(-1)
else :
    #각 자리수의 합이 3의 배수이면
     if sum(int(value) for value in target) % 3 == 0 :
            print(*target,sep='')
     else : print(-1)
            
            
    

