target = int(input())

def digitsum(number) :
    return sum(map(int,str(number)))
    

#0 9 까지 len(target)의 숫자를 뽑는다
def findresult(target) :
    for i in range(2,target) :
        if i+digitsum(i) == target :
            return i
    return 0

print(findresult(target))     
        
        
    
    