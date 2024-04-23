word = input()
list_mover = []
temp = ""
list_container = []
list_sliced = []

to_list = list(word)
print(to_list)

for i in range(len(word)):
    to_list = [to_list[-1]] + to_list[:-1]
    list_sliced = to_list[1:]
    for j in range(len(word) - 2):
        list_sliced = [list_sliced[-1]] + list_sliced[:-1]
        temp = to_list[0] + "".join(list_sliced)
        list_container += [temp]
    list_container.append("".join(to_list))

print(list_container)