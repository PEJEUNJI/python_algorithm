list_x = []
list_y = []

loop = int(input())
for _ in range (loop) :
    x,y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
    
x = max(list_x) - min(list_x)
y = max(list_y) - min(list_y)
print(x*y)