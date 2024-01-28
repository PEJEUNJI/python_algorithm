import sys

row, col = map(int,sys.stdin.readline().split())
input_data = list(map(int,sys.stdin.readline().split()))

total = 0
#현재 땅의 좌우 가장 높은 벽을 확인한다.
for current in range(1,col-1) :
    #현 좌표의 왼쪽값 중에서 가장 높은 벽
    left = max(input_data[:current])
    #현 좌표의 오른쪽값 중에서 가장 높은 벽
    right = max(input_data[current+1:])
    #낮은 벽 만큼만 물이 찰 수 있으므로
    min_height = min(left,right)

    #현 좌표의 높이가 가장 낮은 벽보다 낮다면 물이 찬다.
    if input_data[current] < min_height :
        total += min_height - input_data[current]

print(total)