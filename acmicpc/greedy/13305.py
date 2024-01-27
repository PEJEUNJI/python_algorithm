loop = int(input())-1
distances = list(map(int,input().split()))
costs = list(map(int,input().split()))


min_cost = costs[0]
total = 0
for i in range(loop) :
    # 가장 저렴한 주유비보다 더 저렴한 주유소가 있으면
    if costs[i] < min_cost :
        min_cost = costs[i]#가장 저렴한 비용 갱신
    #온 거리만큼 최소 주유값으로 주유  
    total += min_cost*distances[i] 
print(total)


