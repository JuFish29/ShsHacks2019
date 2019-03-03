def encrypt(key,char):
    key = key[0]
    Character =char

    value = ord(Character) + ord(key)

    if (value > 126):
        value = value - 126
        value = value + 32

    return(chr(value))

def decrypt(key,char):
    key = ord(key[0])
    Character = ord(char)

    if ( Character - key < 0):
        Character = Character + 126 - 32
    Character = Character - key

    return(chr(Character))


password = "password"
Choice = 0
if(Choice == 0):
        with open('TextTester.txt') as f:
            while True:
                character = f.read(1)
                if not character:
                    print ("End of file")
                    break
                print(encrypt(password,character))
                print ("Read a character:", character)
                
else:
    with open('TextTester.txt') as f:
        while True:
            character = f.read(1)
            if not character:
                print ("End of file")
                break
        print ("Read a character:", character)
        print(decrypt(password,encrypt(password,character))) 
