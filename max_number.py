import random
print("Finder biggest number in list")
while True:
    user_num = input("Enter list length of number you wanted: ")
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num < 1:
            print("Your number is lower than 1. You should enter greater")
        else:
            break
    else:
        print("You can enter only positive number")

num_list = []

for i in range(user_num):
    num_list += [random.randrange(1, 100)]

print(num_list)
max_num = 0

for i in range(user_num):
    if num_list[i] > max_num:
        max_num = num_list[i]

print("Maximum number on the list:",max_num)