go,down,top = map(int,input().split())
result  = 0
loop = 0
end_flag = True
#top 높이까지 오면 끝  
while end_flag :
    if result < top : 
        result += go
        loop += 1
    else :
        end_flag = False
        
    if result < top :
        result -= down
        
print(loop)