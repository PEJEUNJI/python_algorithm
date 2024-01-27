
import sys
A_len, B_len = map(int,sys.stdin.readline().split())
A = set(sys.stdin.readline().split())
B = set(sys.stdin.readline().split())

for value in A :
    if value in B :
        A_len -= 1

for value in B :
    if value in A :
        B_len -= 1
        
print(A_len+B_len)