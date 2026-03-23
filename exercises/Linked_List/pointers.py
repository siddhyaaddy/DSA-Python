# num1 = 11
# num2 = num1

# print("before num 2 value is updated: ")
# print("num1  =", num1)
# print("num2  =", num2)

# print("\n num1 points to:", id(num1))
# print("num2 points to:", id(num2))

# num2 = 22

# print("after num 2 value is updated: ")
# print("num1  =", num1)
# print("num2  =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))



dict1 = {'value': 11}
dict2 = dict1

print("before num 2 value is updated: ")
print("dict1  =", dict1)
print("dict2  =", dict2)

print("\n dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("after num 2 value is updated: ")
print("dict1  =", dict1)
print("dict2  =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))



