friends = ['eunji','dajeong','seungmin','park','choi']

def delete_friends(position) :
    if position < 0 or position > len(friends) :
        print('out of index')
        return
    
    list_len = len(friends)
    friends[position] = None

    for i in range(position, list_len-1) :
        friends[i] = friends[i+1]

    del friends[list_len-1]

delete_friends(1)
print(friends)