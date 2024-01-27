friends  = ['eunji','dajeong','seungmin']


def insert_data(position, name) :
    if position < 0 or position > len(friends) :
        print('out of index')
        return
    
    friends.append(None)
    list_len = len(friends)

    for i in range(list_len-1, position,-1) : 
        friends[i] = friends[i-1]
        friends[i-1] = None

    friends[position] = name

insert_data(2,'momo')
print(friends)