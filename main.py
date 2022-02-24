result = ''
choice = ''
message = ''
# Standard P68 Encryption Software
while choice != 0:
    choice = input("1 to encrypt, 2 to decrypt or 0 to exit program. ")
    if choice == '1':
        message = input('Enter message for encryption:')
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 272)
        print(result)
        result = ''
    if choice == '2':
        message = input("Enter message to decrypt:")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 272)

        print(result)
        result = ''
