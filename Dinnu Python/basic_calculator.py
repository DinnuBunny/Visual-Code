num_1 = (input("Enter 1st number: "))
operator = input("Enter Operator: ")
num_2 = (input("Enter 2nd number: "))

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
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
        print("Wrong Operator, Enter (=,-,*,/)")
else:
    print("Please Enter a Valid number")