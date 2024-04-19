import random

print("It's game where you guess the number. You can choose from 1 to 100")

def enter_num():
    while True:
        user_num = input("Enter your guess: ")
        if user_num.isdigit():
            user_num = int(user_num)
            if user_num > 100:
                print("Your number is greater than expected")
            elif user_num < 1:
                print("Your number is lower than expected")
            else:
                return user_num
        else:
            print("You can enter only number")


rand_num = random.randrange(1, 100)

user_num = enter_num()
while True:
    if rand_num == user_num:
        print("Congrats, you won!")
        break
    elif rand_num > user_num:
        print("Higher")
    elif rand_num < user_num:
        print("Lower")
    user_num = enter_num()