#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
#리스트에 각각의 갯수를 지정
need_data = [1,1,2,2,2,8]
#데이터를 읽으면서 value 를 맞추자 need_data[i] - input_data= answer 저장할 list 필요
input_data = list(map(int,input().split()))
for i in range(0,6) :
    print(need_data[i] - input_data[i],end=' ')