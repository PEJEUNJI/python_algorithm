list_x=[]
list_y=[]

def find(list,target) :
    if target in list :
        list.remove(target)
    else :
        list.append(target)

for _ in range(3) :
    x,y = map(int, input().split())
    find(list_x,x)
    find(list_y,y)

print(list_x[0],list_y[0])