empty_dict = {}

person = {"name": "Alice", "age": 30, "city": "NYC"}

dict_constructor = dict(name="Bob", age=25)

from_tuples = dict([("a", (1,2,3)), ("b", 2)])

print(dict_constructor)
print(from_tuples)

squares = {x: x**2 for x in range(5)}


print(squares)
print(squares[3])

# print(person[0]) dictionary cannot be accessing using index



# Accessing into Dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"]) # Alice
print(person.get("age")) # 30
print(person.get("country", "Unknown")) # Unknown (default)
