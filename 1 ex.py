import random

numbers = []


while True:
    userInMin = input("Enter the minimum number: ")

    if userInMin.isdigit():
        userInMin = int(userInMin)
        break
    else:
        print("Enter the correct value")


while True:
    userInMax = input("nter the maximum number: ")
    if userInMax.isdigit():
        userInMax = int(userInMax)
        if userInMax > userInMin:
            break
        else:
            print("Enter a value greater than the minimum")
    else:
        print("Enter the correct value")


while True:
    userInQ = input("Enter the number of numbers to be generated: " )

    if userInQ.isdigit():
        userInQ = int(userInQ)
        if userInQ > 0:
            break
        else:
            print("Enter a value greater than 0")
    else:
        print("Enter the correct value")



for i in range(userInQ):
    numbers.append(random.randrange(userInMin, userInMax))

print("Random numbers: ", numbers)