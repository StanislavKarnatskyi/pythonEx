while True:
    first = input("Enter first number: ")
    if first.isdigit():
        first = int(first)
        break
    else:
        print("You can enter only numbers")


while True:
    oper = input("Enter mathematical operation: ")
    if oper == "*" or oper == "/" or oper == "+" or oper == "-":
        break
    else:
        print("Enter only valuable operations")

while True:
    second = input("Enter second number: ")
    if second.isdigit():
        second = int(second)
        break
    else:
        print("You can enter only numbers")


if oper == "*":
    n = first * second
    print(first, '*', second, ' = ', n)
elif oper == "/":
    n = first / second
    print(first, '/', second, ' = ', n)
elif oper == "+":
    n = first + second
    print(first, '+', second, ' = ', n)
elif oper == "-":
    n = first - second
    print(first, '-', second, ' = ', n)