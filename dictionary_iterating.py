user1 = {
    "name": "Isabella",
    "own_dog": True,
    "grade": 5,
    "favorite_language": "Python",
    "is_short": False,
    29: "my favorite number!"
}

print("----to iterate keys need to use keys()----")

for key in user1.keys():
    print(key)

print("----to access values need to use values()----")

for value in user1.values():
    print(value)

print("----to print both keys and values need to use items()----")

for key,val in user1.items():
    print(f"{key}: {val}")

print("----exercise----")

donations = dict(sam=25.0, lena=88.99, chuck=13.0,
                 linus=99.5, stan=150.0, lisa=50.25,
                 harrison=10.0)

total_donations = 0

for x in donations.values():
    total_donations+=x
print(total_donations)