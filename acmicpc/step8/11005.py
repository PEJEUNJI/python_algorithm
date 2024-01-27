number, n = map(int, input().split())

base_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result_string = ''
while number > 0 :
    remainder = number % n
    result_string = base_string[remainder] + result_string
    number //= n
    
print(result_string)