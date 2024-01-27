target_count, input_count = map(int,input().split())

target_data = {input() for _ in range (target_count)}
input_data = [input() for _ in range (input_count)]

count = sum(1 if value in target_data else 0 for value in input_data)
print(count)

