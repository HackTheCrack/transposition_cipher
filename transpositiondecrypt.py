import math, pyperclip

def main():
    myMessage = input('Please Enter the Message: ')
    myKey = int(input('Please Specify the key number between 0-9 for decryption: '))
    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    numofColumns = math.ceil(len(message) / key)
    numofRows = key
    numofShadedBoxes = (numofColumns* numofRows) - len(message)
    plaintext = [''] * numofColumns
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numofColumns) or (col == numofColumns - 1 and row >= numofRows - numofShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)
if __name__ == '__main__':
    main()