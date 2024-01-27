
while True :
    number = int(input())
    
    if number == -1 : break
    number_list = []
    for i in range(1,number):
        if number%i == 0 : number_list.append(i)
            
    if sum(number_list) == number : 
        print(number,end=' = ')
        print(' + '.join(map(str,number_list)))
    else :
        print(f'{number} is NOT perfect.')
    
        