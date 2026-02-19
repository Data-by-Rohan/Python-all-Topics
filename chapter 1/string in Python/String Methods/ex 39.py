#  Count uppercase, lowercase, digits, and special characters

s= input("Enter a string :" )
upper = 0
lower =0
digits = 0
special = 0

for ch in s:
    if ch.isupper():
        upper +=1
    elif ch.islower():
        lower +=1
    elif ch.isdigit():
        digits +=1
    else:
        special +=1

print("uppercase letters :",upper)
print("lowercase letter : ",lower)
print("digits :",digits)
print("special caharacters :",special)