# text = ["hello world"]
# char_count = {}
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1
# print(char_count)

# clean_text = text.replace(" ", "")
# print(clean_text)

# before_join = text.split(" ")
# print(before_join)
# clean_text1 = "".join(text.split(" "))
# print(clean_text1)
# print("".join(before_join))


def merge_dicts(dict1, dict2):
    result = dict1 # assign by reference store memory 
    #result = dict1.copy() # assign by reference store memory 

    for key, val in dict2.items():
        if result.get(key) == None:
            result[key] = val   
        else:
            result[key] = result[key] + val
    return result


# Create a function that merges two dictionaries. If a key exists in both, sum the values.
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 3, "c": 4, "d": 5}
merge_dicts(d1, d2)
#print(merge_dicts(d1, d2)) # {"a": 1, "b": 5, "c": 7, "d": 5}