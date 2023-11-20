# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
num = {num: num ** 2 for num in [1,2,3,4,5]}
print(num)

str1 = 'ABCD'
str2 = '1234'
# {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

human = {'name': 'loyd', 'state': 'md', 'color': 'black'}
# {'NAME': 'LOYD', 'STATE': 'MD', 'COLOR': 'BLACK'}
humanoid = {key.upper(): value.upper() for key,value in human.items()}
print(humanoid)


print("----conditional logic----")

num_list = [1,2,3,4]
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
num_list1 = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_list1)

humanoid2 = {(key.upper() if key is 'color' else key): value.upper() for key, value in human.items()}
print(humanoid2)