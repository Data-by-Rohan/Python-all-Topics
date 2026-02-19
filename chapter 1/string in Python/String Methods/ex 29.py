#  count vowels in a string

s = "Programming"
vowels = "aeiouAEIOU"
count = 0

for i in s:
    if i in vowels:
        count +=1
print("number of vowels in the string :", count)