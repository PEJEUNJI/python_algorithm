while True : 
    first_num, second_num = map(int,input().split())
    if(first_num == 0 and second_num == 0 ) : break
    #first_num, second_num, first : second%first_num == 0, or first_num%second_num
    if first_num%second_num == 0 :
        print('multiple')
    elif second_num%first_num == 0 :
        print('factor')
    else :
        print('neither')