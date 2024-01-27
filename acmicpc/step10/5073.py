import sys

def print_result(target) :
    length = len(set(target))
    
    if target[0] + target[1] <= target[2] :
        return 'Invalid'
    else :
        if length == 1 :
            return 'Equilateral'
        elif length == 2 :
            return 'Isosceles'
        else :
            return 'Scalene'
        
    
for i in sys.stdin :
    x,y,z = map(int,i.split())
    if(x == y == z == 0):break
    else : print(print_result(sorted([x,y,z])))
    
