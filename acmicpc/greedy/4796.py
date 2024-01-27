import sys

#5 8 20
#5 ,3, 5, 3, 4
def getDays(term, limit, days) :
    loop = days//limit
    use_days = term * loop
    rest_days = (limit - term)*loop
    remain_days = days - use_days - rest_days
    #사용가능한 연차가 사용 가능한 휴일보다 적으면, 사용가능한 연차만 더한다
    if remain_days < term :
        return remain_days + use_days
    #사용가능한 연차가 사용 가능한 휴일보다 많으면, 사용가능한 더한다
    else :
        return term + use_days

loop = 0
for i in sys.stdin :
    term, limit, days = map(int,i.split())
    if term == limit == days == 0 : break
    else : 
        loop += 1 
        print(f'Case {loop}: {getDays(term, limit, days)}')
#term + (limit-term) ->반복 days가 되는 순간 종료
#days//limit 으로 loop를 구하고 term * loop후 나머지 날짜를 더한다