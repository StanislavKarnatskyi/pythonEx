def userNum():
    while True:
        user_num = input("For how much you want to change?\n")
        if user_num.isdigit():
            return int(user_num)
        else:
            print("You can enter only numbers")

#шифрування
def encrypt():
    user_num = userNum()
    text_encrypted = ""
    user_text = input("Print the text you want to encrypt\n")
    for char in user_text:
        text_encrypted += chr(ord(char) + user_num)
    print(text_encrypted)

#дешифрування
def decrypt():
    user_num = userNum()
    print(user_num)
    text_decrypted = ""
    user_text = input("Print the text you want to decrypt\n")
    for char in user_text:
        text_decrypted += chr(ord(char) + user_num)
    print(text_decrypted)


user_choise = input("This is encryption/decryption program. What do you want? Encrypt or Decrypt?\n")
while True:
    user_choise = user_choise.lower()
    if user_choise == "encrypt":
        encrypt()
        break
    elif user_choise == "decrypt":
        decrypt()
        break
    else:
        user_choise = input("Please, enter only valid option\n")


