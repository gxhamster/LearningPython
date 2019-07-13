import random

users = []


def createUserID():
    id = random.seed()
    userID = ''
    for i in range(0, 6):
        rNumber = random.randint(0, 9)
        userID += str(rNumber)
    
    return userID

def addUser():
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    gender = input('Enter gender: ')
    userID = createUserID()

    dict = {'name': name, 'age': age, 'gender': gender, 'id': userID}
    users.append(dict)
    return dict


def delUser(user):
    pass


# Main program loop
# while True:
#     print('\n1) To add user')
#     option = int(input('\nEnter here: '))
#     if option == 1:
#         print(addUser())
#     elif option == 'q':
#         break

userData = []
for i in range(0, 1000):
    userData.append(addUser())
