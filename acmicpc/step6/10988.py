
#입력값을 string 넣고 reverse한 값이 이전과 같은지 비교
input_data = input()
print(f'input_data-->{input_data}')
reversed_data = input_data[::-1]
print(f'reversed_data-->{reversed_data}')
print(1 if input_data == reversed_data else 0)