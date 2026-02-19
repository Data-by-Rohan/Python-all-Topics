# Remove dublicates from a string


s= "banana"
result= ""
for i in s:
    if i not in result:
        result += i
print("string after removing dublicats :",result)