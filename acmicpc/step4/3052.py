import sys
#set
data_set = set()

for i in sys.stdin :
    data_set.add(int(i)%42)
    print(f'int(i)%45->{int(i)%45}')
    print(f'len(data_set)->{len(data_set)}')