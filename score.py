while True:
    usser = input("Enter score: ")
    try:
        usser = float(usser)
        if usser <= 1.0 and usser >= 0.0:
            break
        else:
            print("You can enter only number in range 0.0 to 1.0")
    except:
        print("Enter only numeric nuber is range 0.0 to 1.0")

if usser >= 0.9:
    print("A")
elif usser >= 0.8:
    print("B")
elif usser >= 0.7:
    print("C")
elif usser >= 0.6:
    print("D")
elif usser < 0.6:
    print("F")