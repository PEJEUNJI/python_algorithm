list_data = list(input().upper())
map_count = {}
for i in list_data :
    map_count[i] = map_count.get(i,0) + 1

max_value = max(map_count.values())

count = sum(1 for value in map_count.values() if value == max_value)
if count > 1 :
    print('?')
else :
     for key, values in map_count.items() :
         if values == max_value :
             print(key)
