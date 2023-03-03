from collections import OrderedDict
def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

nums = [1,34,332,43,34,23,23412,32,431,223,43,21,321,34,122,31]
print("original lists: ")
print(nums)
result = remove_duplicates(nums)
print("The duplicates are removed")
print(result)
chars = ['a','a','d','d','e','f','g']
print("\nOriginal lists:")
print("Remove duplicates while printing the order ")
print(result)
