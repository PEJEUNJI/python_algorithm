length = int(input())

for _ in range(length) :
    loop, input_str = input().split()
    for c in input_str :
        print(c*int(loop),end='')
    print()

 
    