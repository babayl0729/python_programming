from random import choice #DON'T CHANGE!

print("---clear---\n")

d = dict(a=1,b=2,c=3)
print(d.clear())

print("\n----copy----")

user1 = {
    "name": "Isabella",
    "own_dog": True,
    "grade": 5,
    "favorite_language": "Python",
    "is_short": False,
    29: "my favorite number!"
}

user2 = user1.copy()
print(user2)


print("\n----fromkeys----\n")
# creates key-value pairs 
# from comma separated values:

#{'name': 'unknown', 'own_dog': 'unknown', 'grade': 'unknown', 'favorite_language': 'unknown', 'is_short': 'unknown'}
user3 = {}.fromkeys(['name','own_dog','grade','favorite_language','is_short'], 'unknown')
print(user3)

user4 = user3.fromkeys(['name'], 'Isabella')
print(user4)

user5 = {}.fromkeys('phone','unknown')
print(user5)

print("\n----get----")
# Retrieves a key in an object and reuturn None
# instead of a KeyError if the key does not exist.

# Isabella
print(user1.get('name'))
# None
print(user1.get('age'))

user6 = user1.get('email')
# True
print(user6 is None)

print("\n----exercise 1----\n")

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't have that")


print("---using get---")

foods = bakery_stock.get(food)

if foods:
    print(f"{foods} left")
else:
    print("We don't have that")

print("\n----exercise 2----")

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", 
                   "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", 
                   "minutes_played", "notifications", "achievements"] 

initial_game_state = {}.fromkeys(game_properties, 0)

print(initial_game_state)




