while True:
    ch = int(input("1. Fahrenheit 2. Celsius\n"))
    if ch == 1:
        far = int(input("Enter the Fahrenheit value\n"))
        print(((far+40)/1.8)-40)
        break
    elif ch == 2:
        cel = int(input("Enter the Celsius value\n"))
        print(((cel + 40) * 1.8) - 40)
        break
    else:
        print("Enter a valid value")
        continue
