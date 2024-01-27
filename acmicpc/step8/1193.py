target = int(input())

loop = 1
startNo = 1
endNo = 1
top = 1
bottom = 1
if target == 1 :
    print('1/1')
else :
    while not(startNo<=target and target<=endNo) :
        startNo = endNo + 1
        loop += 1
        endNo = endNo + loop
        
    if loop%2 == 0 :
        term = target - startNo
        bottom = loop - term
        top = 1+term
    else :
        term = target - startNo
        top = loop - term
        bottom = 1+term
    print(f'{top}/{bottom}')