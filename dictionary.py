user_info = {
    'name': 'Isabella',
    'last': 'Babay',
    'age': 10,
    'grade': 4
}

print(user_info)

print("-----Accessing Individual Values-----")

print(user_info['name']) # Isabella
print(user_info['age']) # 10
# print(user_info['address']) # KeyError

full_name = user_info['name'] + " " +user_info['last']
print(full_name)