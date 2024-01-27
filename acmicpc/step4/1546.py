# 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100

length = int(input())

list_data = list(map(int,input().split()))

max_num = max(list_data)

print(sum(score/max_num *100 for score in list_data)/length)

