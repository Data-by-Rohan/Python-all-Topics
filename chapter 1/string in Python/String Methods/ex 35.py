#  find dublicate charector in a string

s= "programming"
dublicate = []
for i in s:
    if s.count(i)> 1 and i not in dublicate:
        dublicate.append(i)
print("dublicate charector in the string :", dublicate)