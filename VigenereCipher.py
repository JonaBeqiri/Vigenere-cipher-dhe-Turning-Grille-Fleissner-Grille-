
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

print(encrypt())