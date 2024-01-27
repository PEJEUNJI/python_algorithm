paper = [[0]*100 for _ in range(100)]

loop = int(input())

for j in range(loop) :
    x,y = map(int,input().split())
    for x_index in range(x-1,10+x-1):
        for y_index in range(y-1,10+y-1): 
            paper[x_index][y_index] = 1
            
total_count = sum(row.count(1) for row in paper)


print(total_count)