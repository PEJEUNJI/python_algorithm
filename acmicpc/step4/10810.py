import sys

length, count = map(int,sys.stdin.readline().split())
diction_data = {key:1 for key in range(1,length+1)}
print('data -> ',*diction_data.items())

for i in sys.stdin :
    from_basket, to_basket, ball_number = map(int,i.split())
   
   re for i in range(from_basket,to_basket+1,1) :
        diction_data[i] = ball_number

    print('data -> ',*diction_data.values())
     