state1 = ['CA','NJ','RI']
state2 = ['California','New Jersey','Rhode Island']
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
answer = {state1[i]:state2[i] for i in range(0,len(state1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
answer1 = {k: v for k,v in person}
print(answer1)

# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
answer2 = dict(person)
print(answer2)

vowels = 'aeiou'
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
dict_vowels = {}.fromkeys(vowels,0)
print(dict_vowels)

# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
answer3 = {char:0 for char in 'aeiou'} 
print(answer3)

answer4 = {k: chr(k) for k in range(65,91)}
print(answer4)

    
