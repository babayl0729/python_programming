pets = ["dog", "cat", "lion", "bird", "eagle", "snake", "tarantula", "horse", "cow"]
print(pets)
#['lion', 'bird', 'eagle', 'snake', 'tarantula', 'horse', 'cow']
print(pets[2:])
print(pets[:2]) # ['dog', 'cat']

print("---------------guitars---------------")

guitars = ["tele", "ibanez", "jazzmaster", "strat", "jaguar", "les paul", "mustang", "casino"]
print(guitars)
print(guitars[:2]) # ['tele', 'ibanez']
print(guitars[1:3]) # ['ibanez', 'jazzmaster']

print("-----------negative numbers----------------")

guitars2 = ["tele", "ibanez", "jazzmaster", "strat", "jaguar", "les paul", "mustang", "casino"]
print(guitars2)
#['tele', 'ibanez', 'jazzmaster', 'strat', 'jaguar', 'les paul', 'mustang']
print(guitars2[:-1])
#['ibanez', 'jazzmaster', 'strat', 'jaguar', 'les paul', 'mustang']
print(guitars2[1:-1])

print("-------------word number--------------")

word_number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
print(word_number)
# ['two', 'four', 'six', 'eight', 'ten']
print(word_number[1::2])
# ['one', 'three', 'five', 'seven', 'nine']
print(word_number[::2])

print("------------tricks with slices-----------")

string1 = "This is fun"
print(string1)
print(string1[::-1]) # nuf si sihT

print("--------modifying portion of list--------")
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']
#[1, 'a', 'b', 'c', 4, 5]
print(numbers)

print("---------bonus slices trick---------")

color = ['red','blue','yellow','pink','black','purple']
print(color)
#yellow
print(color[2])
#wolley
print(color[2][::-1])

#hell
print('helllllooooo'[:4])
#hllo
print('helllllooooo'[::3])

print("---------swapping values---------")

namesss = ["James", "Michelle"]
['James', 'Michelle']
print(namesss)
namesss[0],namesss[1] = namesss[1], namesss[0]
['Michelle', 'James']
print(namesss)



