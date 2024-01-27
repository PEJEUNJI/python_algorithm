target = int(input())

def getName(input_target):
    if input_target == 0 : return 0
    
    else :
        start = 0
        count = 0
        while count < input_target :
            start += 1
            if '666' in str(start)  :
                count += 1
        return start

print(getName(target))