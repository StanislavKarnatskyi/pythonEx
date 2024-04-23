user_word = input("Enter the word: ")
user_word_arranged = []
user_word_sym = []
user_word_sym2 = []
user = ""
for i in user_word:
    user_word_sym += i
user = "".join(user_word_sym)
print(user_word_sym, user)
    #user_word_aranged += [user_word]
#print(user_word_aranged)

for i in range(len(user_word)):
    user_word_sym2 += user_word_sym[-i+1]
print(user_word_sym2)
