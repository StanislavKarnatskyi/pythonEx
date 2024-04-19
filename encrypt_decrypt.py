def userNum():
    while True:
        user_num = input("For how much you want to change?\n")
        if user_num.isdigit():
            num = int(user_num)
            if 1 <= num <= 26:
                return num
            else:
                print("Please enter a number between 1 and 26.")
        else:
            print("You can enter only numbers")

#шифрування
def encrypt():
    user_num = userNum()
    text_encrypted = ""
    user_text = input("Print the text you want to encrypt\n")
    for char in user_text:
        if char.isalpha():
            text_encrypted += chr((ord(char) - ord('a') + user_num) % 26 + ord('a'))
        else:
            text_encrypted += char
    print(text_encrypted)

#дешифрування
def decrypt():
    user_num = userNum()
    print(user_num)
    text_decrypted = ""
    user_text = input("Print the text you want to decrypt\n")
    for char in user_text:
        if char.isalpha():
            text_decrypted += chr((ord(char) - ord('a') + user_num) % 26 + ord('a'))
        else:
            text_decrypted += char
    print(text_decrypted)


user_choose = input("This is encryption/decryption program. What do you want? Encrypt or Decrypt?\n")
while True:
    user_choose = user_choose.lower()
    if user_choose == "encrypt":
        encrypt()
        break
    elif user_choose == "decrypt":
        decrypt()
        break
    else:
        user_choose = input("Please, enter only valid option\n")


