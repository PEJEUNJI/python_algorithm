target = input()
length = len(target)

#abcde->a,ab,abc,abcd,abcde (0:1,0:2,0:3..0:5)
#abcde->b,bc,bcd,bcde (1:2,1:3..1:5)
#abcde->c,cd,cde (2:3,2:4..2:5)
#abcde->d,de
#abcde->e
result_data= set()

for first_index in range(length) :
    for second_index in range(first_index+1,length+1):
        result_data.add(target[first_index:second_index])
        
print(len(result_data))
