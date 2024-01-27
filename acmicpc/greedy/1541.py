import re
#-부호를 만날때마다 그룹핑, 그룹핑한 숫자들끼리 합한 후 뺀다.
#-,+ 포함해서 리스트에 넣어줘야 함으로 () 추가
input_data = re.split(r'([-+])',input()) 
part_sum = 0
result_data =[]

for value in input_data :
    #숫자인 경우 합한다.
    try :
        part_sum += int(value)
    except Exception :
    #숫자가 아닌경우, 마이너스가 나온 경우 지금까지 구한 합을 저장
        if value == '-' :
            result_data.append(part_sum)   
            part_sum = 0 
#마지막 부분합까지 리스트에 적용하면 완료                
result_data.append(part_sum)

print(result_data[0]-sum(result_data[1:]) if len(result_data) > 1 else result_data[0])