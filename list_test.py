vafriends_list = ['eunji','dajeong','seungmin']


friends_list.append('momo')

print('friends_list',friends_list)
friends_list.insert(2,'nana')
print('friends_list',friends_list)
del friends_list[2]
print('friends_list',friends_list)
remove = friends_list.pop(2)
print(f'remove : {remove}, {friends_list}')


def add_data(name) :
    friends_list.append(name)

add_data('gaga')
print('friends_list',friends_list)