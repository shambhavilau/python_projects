'''
    input text = substitution_text.txt
    output cipher text = cipher_text.txt
'''


import string
dict1 = {}
data = ""
file = open("cipher_text.txt", "w")
for i in range(len(string.ascii_letters)):
    dict1[string.ascii_letters[i]] = string.ascii_letters[i-1]
print(dict1)

with open("substitution_text.txt") as f:
    while True:
        ch = f.read(1)
        if not ch:
            print("Reached End of File")
            break
        if ch in dict1:
            data = dict1[ch]
        else:
            data = ch
        file.write(data)
        # print(data)
file.close()
