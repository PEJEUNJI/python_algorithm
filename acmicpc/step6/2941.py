data_map = {'c=':'č','c-':'ć','dz=':'dž','d-':'đ','lj':'lj','nj':'nj','s=':'š','z=':'ž'}
input_data = input()
data_len = len(input_data)
count = 0
i = 0

for i in data_map.keys():
    input_data = input_data.replace(i,'0')
        
print(len(input_data))