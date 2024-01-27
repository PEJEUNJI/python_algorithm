import sys
input()
input_diction = {}
for line in sys.stdin :
    name, action = map(str, line.split())
    if action == 'enter' : 
        input_diction[name] = action
    else :
        del input_diction[name]
        
print(*sorted(list(input_diction.keys()),reverse=True),sep='\n')

