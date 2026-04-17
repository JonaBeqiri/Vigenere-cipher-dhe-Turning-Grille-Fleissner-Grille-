
# (p + k) mod 26 => 0 - 25 (Nje shkronje e alfabetit)
# ord('a') -> 97, res = (ord(p) - 97 + ord(k) - 97) mod 26
# enc_letter = ord('a') + res 

text = input("Enter text to encrypt: ")
key = input("Enter key: ")

key_len = len(key)


def encrypt():

    result = ""

    key_index = 0
    
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                p = ord(text[i]) - ord('a')
                k = ord(key[key_index % key_len].lower()) - ord('a')
                c = (p + k) % 26
                result += chr(c + ord('a'))
            else:
                p = ord(text[i]) - ord('A')
                k = ord(key[key_index % key_len].upper()) - ord('A')
                c = (p + k) % 26
                result += chr(c + ord('A'))

            key_index += 1
        else:
            result += text[i]



    return result 

if not key.isalpha():
    print("Error - Key duhet te permbaje vetem shrkonja dhe te mos jete bosh!")
else:
    print("Encrypted text: ", encrypt())






text = input("Enter text to decrypt: ")
key =input("Enter key: ") 

key_len = len(key)

def decrypt():

    result= ""
    key_index = 0

    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                c=ord(text[i]) - ord('a')
                k=ord(key[key_index % key_len].lower()) - ord('a')
                p=(c - k + 26) % 26
                result +=chr(p+ ord('a'))
            else:
                c=ord(text[i]) - ord('A')
                k=ord(key[key_index % key_len].upper()) - ord('A')
                p=(c - k + 26) % 26
                result +=chr(p+ ord('A'))

            key_index += 1
        else:
            result += text[i]

    return result

if not key.isalpha():
    print("Error - Key duhet te permbaje vetem shrkonja dhe te mos jete bosh!")
else:
    print("Decrypted text: ", decrypt())




