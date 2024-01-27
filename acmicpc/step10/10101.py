input_data = []
for _ in range(3) :
    input_data.append(int(input()))
    
sum = sum(input_data)

if input_data.count(60) == 3 :
    print('Equilateral')
elif sum == 180 :
    length = len(input_data)
    set_length = len(set(input_data))
    if length - set_length == 1 :
        print('Isosceles')
    else :
        print('Scalene')
else :
    print('Error')
    