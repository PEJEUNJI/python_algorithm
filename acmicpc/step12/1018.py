row, col = map(int,input().split())

input_data = []
result = []
for _ in range (row) :
    input_data.append(input())

print(input_data)
    
for i in range (row-7) :
    for j in range (col-7):
        first_black = 0
        first_white = 0
 
        for r in range (i, i+8) :
            for c in range (j, j+8) :
                print(input_data[r][c])
                #짝수 확인 [0,0],[0,2]
                if (r+c)%2 == 0 :
                    #시작을 B 로 할때
                    if input_data[r][c] != 'B':
                        first_black += 1
                    #시작을 W 로 할때
                    if input_data[r][c] != 'W':
                        first_white += 1
                #홀수 인덱스 확인 [0,1],[0,3]
                else :
                    #시작을 B로 할때는 W로 시작
                    if input_data[r][c] != 'W':
                        first_black += 1
                    #시작을 W로 할때
                    if input_data[r][c] != 'B':
                        first_white += 1   

        result.append(first_black)
        result.append(first_white)

print(min(result))