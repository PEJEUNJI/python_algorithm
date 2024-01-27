#value를 diction 에 저장 후 value가 있는지 없는지 확인
input()

#in검색시 빠른 검색을 위해 set으로 전환, 시간 복잡도가 O(1)로 줄어든다
input_data = set(input().split()) 

input()
target_data = input().split()

for value in target_data :
   print(1 if value in input_data else 0,end=' ')
