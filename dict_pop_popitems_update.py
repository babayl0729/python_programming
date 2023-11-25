print("""Pop - 
      Takes a single argument corresponding to a key
      and removes that key-value pair from 
      dictionary. Returns the value corresponding
      to the key that was removed.\n""")


user1 = {'name': 'Ern', 'owns_dog': True, 
         'num_courses': 4, 'favorite_food': 'pizza',
         'is_lazy': False, 'black': 'my favorite color!'}

print(user1)

print("\nwill remove is_lazy")
print(user1.pop('is_lazy'))

print(user1)

#you will get an error if you do this:
#print(user1.pop())

#you will get a keyError with this:
#print(user1.pop("address"))

print("\npopitem - removes a random key in a dictionary:")
print(user1.popitem())

print(user1)

#you will get an TypeError if you do this:
#print(user1.popitem('name'))

print("""\nupdate - Update keys and values in a dictionary
      with another set of key value pairs.""")

car = {"car_brand": "Honda"}
car.update(user1)
print(car)
user1.update(car)
print(user1)

print("\nExercise:")
inventory = {'croissant': 19, 'bagel': 4, 
             'muffin': 8, 'cake': 1}

print(inventory)
stock_list = inventory.copy()
print("This is the stock_list:")
print(stock_list)

#added 'cooki': 18 in stock_list
stock_list['cookie'] = 18
print(stock_list)
#removed cake from stock_list
stock_list.pop('cake')
print(stock_list)

