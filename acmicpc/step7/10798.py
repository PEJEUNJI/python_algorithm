import sys
input_data = []
col_max_length = 0

for i in sys.stdin:
    input_data.append([ch for ch in i.strip()])

col_max_length = max(len(row) for row in input_data)

for i in range(col_max_length):
    print(''.join(row[i] if i < len(row) else '' for row in input_data),end='')