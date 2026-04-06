n = int(input("Please type your first number: "))
m = int(input("please type your second number: "))
operator = input("Please input your operator (+, -, *, /): ")

if operator == "+":
    addition = n+m
    print (f"the addition of {n} and {m} is :{addition}")
elif operator == "-":
    subtraction = n-m
    print (f"The subtraction of {n} - {m} is : {subtraction}")
elif operator == "*":
    multipication = n*m
    print (f"the multiplication of {n} * {m} is: {multipication}")
elif operator == "/":
    if m != 0:
        division = n/m
        print (f"Division of {n} / {m} is: {division}")
    else:
        print ("Please  enter a non-zero number for division.")
