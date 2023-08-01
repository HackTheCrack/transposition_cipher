import pyperclip

def main():
    myMessage = input('Please Enter the message: ')
    myKey = int(input('Please Specify the key number between 0-9 for encryption:'))
    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
