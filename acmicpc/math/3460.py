import sys
loop = int(sys.stdin.readline().strip())

result_data = []
for i in range(loop) :
    target = int(sys.stdin.readline().strip())
    result_data.clear()
    while target > 1 :
        #2로 나눈 나머지를 순서대로 저장
        result_data.append(target%2)
        #2로 나눈 몫으로 변경
        target = target//2
    result_data.append(target)

    length = len(result_data)
    for index, value in enumerate(result_data):
        if value == 1 : print(index,end=' ')
    print()