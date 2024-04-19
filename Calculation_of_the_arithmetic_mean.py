list_of_number = []
sum = 0

print("Calculation of the arithmetic mean\nIf you want to stop entering number, just enter word \"Stop\"")

while True:
    num = input("Enter numbers: ")
    if num.isdigit():
        num = int(num)
        list_of_number += [num]
    elif num == "Stop" or num == "stop":
        break

lenn = len(list_of_number)

for i in range(lenn):
    sum += list_of_number[i]

mean = sum / lenn
print("Arithmetic mean:", mean)