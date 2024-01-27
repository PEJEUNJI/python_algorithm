loop = int(input())

group_count = 0
for _ in range(0,loop) :
    word = input()
    #문자열 하나하나 저장하는 diction
    ch_diction = {}
    word_len = len(word)
    group_flag = True

    for index,ch in enumerate(word) :
          
        if ch in ch_diction and ch_diction[ch] + 1 != index :
            group_flag = False
            break

        ch_diction[ch] = index

    group_count += group_flag
    
print(group_count)
    

