import sys
max = 0
total = 0
for value in sys.stdin :
    minus,plus = map(int,value.split())
    total += plus-minus
    if total > max : max = total

print(max)