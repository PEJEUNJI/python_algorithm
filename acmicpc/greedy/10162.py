target_time = int(input())
times = [300,60,10]
result_data = []
for time in times :
    result_data.append(target_time//time)
    target_time %= time
    
print(-1) if target_time != 0 else print(*result_data)
