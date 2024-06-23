

print("Welcome to the simple calculator program!")

#要不要再計算
done = False
while not done:

    fn = float(input("Enter the first number:"))
    sn = float(input("Enter the second number:"))
    op = input("Select an arithmetic operation(+, -, *, /):")

#排除除以零
    while True:
        if (sn == 0) and (op == "/"):
            print("Error: Division by zero!")
            fn = float(input("Enter the first number:"))
            sn = float(input("Enter the second number:"))
            op = input("Select an arithmetic operation(+, -, *, /):")
        else:
            break
    
    result = 0
    if op == "+":
        result = fn + sn
    if op == "-":
        result = fn - sn
    if op == "*":
        result = fn * sn
    if op == "/":
        result = fn / sn
    print("Result: %f" % result)
    again = input("Do you want to perform another calculation?(yes or no):")
    done = (again != "yes")
print("Goodbye!")