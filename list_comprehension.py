nums = [1,2,3]
print(nums)
nums1 = [nums1*10 for nums1 in nums]
print(nums1)

# numbers = [1,2,3,4,5]
# doubled_numbers = []
# for num in numbers:
#     doubled_number = num*2
#     doubled_numbers.append(doubled_number)
# print(doubled_numbers)

print("----for loop to list comprehension----")

numbers = [1,2,3,4,5]
doubled_numbers = [x*2 for x in numbers]
print(doubled_numbers)

print("---capitalize caharacters in name---")

name = "loyd"
name1 = [name1.upper() for name1 in name]
print(name1)

print("----capitalized first char in friends name----")

friends = ['isabella','zander','jaiden','william']
friend = [friend[0].upper() for friend in friends]
print(friend)

print("----using range---")

numss = [numss*10 for numss in range(1,6)]
print(numss)

print("----using bool----")

#[False, False, False]
booly = [bool(val) for val in [0,[], '']]
print(booly)

print("---convert int in list to str---")

numsss = [1,2,3,4]
#['1', '2', '3', '4']
str_numsss = [str(num) for num in numsss]
print(str_numsss)





