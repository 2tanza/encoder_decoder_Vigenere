phrase = input("Enter a phrase; ")
key = input("Enter a key; ")
phrase = phrase.lower()
key = key.lower()

code_decode = input("Encode?(y/n) ")

phrase_list = list(phrase.replace(" ", ""))
key_list = list(key.replace(" ", ""))

phrase_list = [ord(char) - ord('a') + 1 for char in phrase_list]
key_list = [ord(char) - ord('a') + 1 for char in key_list]

if code_decode == "y":
    result = [(a + b - 1) % 26 + 1 for a, b in zip(phrase_list, key_list)]
    phrase_list = [chr(num + ord('a') - 1) for num in result]

elif code_decode == "n":
    result = [(a - b - 1) % 26 + 1 for a, b in zip(phrase_list, key_list)]
    phrase_list = [chr(num + ord('a') - 1) for num in result]

print(''.join(phrase_list))