# Accessing into Dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"]) # Alice

print(person.get("age")) # 30
print(person.get("country", "Empty")) # Unknown (default)
country = person.get("country")
if country == None:
    country = "Empty inside IF"
print(country)
# print(person["country"]) this code will give error due to cannot find the key in dict

user = {}

# how to add or update
user["username"] = "Soknoy"
user.update({"password": 123456, "username": "Soknoy Updated", "capcha": "12345"})
user.setdefault("username", "Soknoy") # setdefault value add only the key not exist it will not update
user.setdefault("age", 10)
print(user)

# how to remove it

# removedValue = user.pop("username")
# print(removedValue)
# print(user)

# removedValue = user.popitem()
# print(removedValue)
# print(user)

# How to iterate over dictionaries

# Looping through key
for key in user:
    print(f'Key is {key} Value is {user[key]}')

# Looping through items can get both key, value from item inside dictionary
print("-_______________________________")
for key, val in user.items():
    print(f'Key is {key} Value is {val}')

# Looping through dict using only value
print("-_______________________________")
for val in user.values():
    print(f'Value is {val}')