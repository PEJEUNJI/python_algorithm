import sys

input_data = []
for i in sys.stdin :
    input_data.append(list(map(int,i.split())))
    
max_value, max_row, max_col = max((input_data[i][j], i, j)
                                  for i, row in enumerate(input_data) 
                                  for j, value in enumerate(row))

print(max_value)
print(max_row+1, max_col+1)
    

    
