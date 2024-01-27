import random

lotto = []

count = int(input('which numbers do you want?'))

for _ in range(count):
    pickNum = random.randint(1,45)
    if pickNum not in lotto :
        lotto.append(pickNum)
    if len(lotto) >= 6 :
        break

for num in lotto :
    print(f'number {num}')