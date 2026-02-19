age = int(input("Enter your age: "))    
income  = float(input("Enter Your income: "))
credit_score = int(input("Enter Your credit score: "))
if age >=18 and age <=60:
    if income >= 25000:
        if credit_score >= 750:
            print("Loan Approved")
        elif credit_score >= 650:
            print("Loan Approved with higher interest rate")
        else:
            print("loan rejected due to low credit score")
    else:
        print("Loan rejected due to low income")
else:
    print("Loan rejected due to age restrictions")
