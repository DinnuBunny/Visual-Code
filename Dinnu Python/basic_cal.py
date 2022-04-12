num_1 = int(input("Enter 1st number: "))
operator = input("Enter Operator: ")
num_2 = int(input("Enter 2nd number: "))

if operator in ["+","-","*","/"]:
    if operator == "+":
        print(num_1	 + num_2)
    elif operator == "-":
        print(num_1	 - num_2)
    elif operator == "*":
        print(num_1	 * num_2)
    elif operator == "/":
        print(num_1	 / num_2)
else:
    print("Wrong Operator Enter (=,-,*,/)")