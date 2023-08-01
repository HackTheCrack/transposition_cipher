import time, os, sys, tranpositionencrypt, transpositiondecrypt

def main():
    inputFilename = input('Please Add the file name: ')
    myMode = input('Please Specify encrypt or decrypt: ')
    if (myMode == 'encrypt'):
        outputFilename = inputFilename + '.encrypted.txt'
    elif (myMode == 'decrypt'):
        outputFilename = inputFilename + '.decrypted.txt'
    myKey = int(input('Please Specify the Key for Encryption or Decryption: '))

    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    startTime = time.time()

    if myMode == 'encrypt':
        translated = tranpositionencrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositiondecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))


    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
    main()