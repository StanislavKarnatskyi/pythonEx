import random
print("Game 'Rock, paper, scissors'")

while True:
    userIn = int(input("What you choose?\n1. Rock 2. Paper 3. Scissors\n"))
    if userIn == 1:
        userIn = "Rock"
        break
    if userIn == 2:
        userIn = "Paper"
        break
    if userIn == 3:
        userIn = "Scissors"
        break
    elif userIn != 1 or userIn != 2 or userIn != 3:
        userIn = int(input("Choose on of them\n1. Rock 2. Paper 3. Scissors\n"))
        if userIn == 1:
            userIn = "Rock"
            break
        if userIn == 2:
            userIn = "Paper"
            break
        if userIn == 3:
            userIn = "Scissors"
            break
        continue


els = ['Rock', 'Paper', 'Scissors']
el = random.choice(els)
print("User choose", userIn, "\nComputer choose", el)


#too much if -_-...
if userIn == els[0] and el == els[0]:
    print("Draw")
elif userIn == els[0] and el == els[1]:
    print("Lose")
elif userIn == els[0] and el == els[2]:
    print("Won")
elif userIn == els[1] and el == els[1]:
    print("Draw")
elif userIn == els[1] and el == els[2]:
    print("Lose")
elif userIn == els[1] and el == els[0]:
    print("Won")
elif userIn == els[2] and el == els[2]:
    print("Draw")
elif userIn == els[2] and el == els[0]:
    print("Lose")
elif userIn == els[2] and el == els[1]:
    print("Won")