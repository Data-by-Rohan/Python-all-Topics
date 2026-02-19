# Rent Calculator in using user input function


# inputs we need from the user
# 1. total rent
# 2 total food expenses
# 3.electricity units spent
# 4. elctricity cost per unit
# 5. total persons sharing the rent

# output
# total amount to be paid by the user

rent = float(input("Enter the Hostel/room rent:    "))
food = float(input("Enter the total food expenses:    "))
electricity_spent = float(input("Enter the total electricity units spent:    "))
electricity_cost_per_unit = float(input("Enter the electricity cost per unit:    "))
persons = int(input("Enter the total number of persons sharing the rent:    "))

total_electricity_cost = electricity_spent * electricity_cost_per_unit
output = (rent + food + total_electricity_cost) / persons
print("The total amount to be paid by each person is:", output)
