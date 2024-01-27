
target = int(input())
width = 2*(target-1) +1
for i in range(1,target+1,1) :
    print((i*'*').rjust(target,' '),end='')
    print((i-1)*'*')
    
for i in range(target-1,-1,-1) :
    print((i*'*').rjust(target,' '),end='')
    print((i-1)*'*')