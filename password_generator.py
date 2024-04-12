import random

ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

ps = ''

num = int(input("Enter the length of the password you want: "))

for i in range(1, num + 1):
    ps += random.choice(ch)

print(ps)