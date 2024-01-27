import sys
score_map = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.0,'F':0.0}
# for  값 입력   _,score,grade= input().split()
# sum(score if grade != 'p' else  
#ProblemSolving 4.0 a
total = 0
my_total = 0
for line in sys.stdin :
    _,score,grade= line.split()
    print(f'grade-->{grade},score_map[grade]-->{score_map[grade]}')
    total += float(score)*score_map[grade] if grade != 'P' else 0  
    my_total +=float(score)if grade != 'P' else 0  
    
print(total/my_total)
