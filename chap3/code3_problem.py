friends = [('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

def insert_data(name, num) :
    for i , (friend_name, friend_num) in enumerate (friends) :
        if(friend_num <= num) :
            friends.insert(i,(name, num))
            break


insert_data('모모',30)
print(friends)

        

