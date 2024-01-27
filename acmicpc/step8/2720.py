loop = int(input())

for i in range(loop) :
    change = int(input())
    quarter,change = divmod(change,25)
    dime,change = divmod(change,10)
    nickel,change = divmod(change,5)
    penny = change
    print(f'{quarter} {dime} {nickel} {penny}')
    
    