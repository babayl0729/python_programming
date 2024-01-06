def product(x,y):
    return x*y

def return_day(day):
    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else:
        return None

# def last_element(l):
#     if l:
#         return l[-1]
#     return None

def number_compare(num1,num2):
    if num1 > num2:
        return "First is greater"
    elif num2 > num1:
        return "Second is greater"
    return "Numbers are equal"

def single_letter_count(word,letter):
    if word:
        return word.lower().count(letter.lower())
    return 0

def multiple_letter_count(keys):
    let = 'aemosw'
    nums = 1,2,1,1,1,1
    keys = {let[i]: nums[i] for i in range(0, len(let))}
    return keys.count(let)

# solution
def multiple_letter_count2(string):
    return {letter: string.count(letter) for letter in string}

def list_manipulation(list=[1,2,3],command="remove",location="end",value=0):
    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "beginning":
        list.insert(-3,value)
        return list
    elif command == "add" and location == "end":
        list.append(value)
        return list
    else:
        None
   

print(f"product = {product(6,9)}")
print(f"The day today is {return_day(8)}")
# print(f"Last element {last_element(1)}")
print(number_compare(1,5))
print(single_letter_count('Isabella','L'))
#print(f"multiple letters {multiple_letter_count('awesome')}")
print(f"multiple letters {multiple_letter_count2('awesome')}")
print(list_manipulation([1,2,3],"add","end",30))