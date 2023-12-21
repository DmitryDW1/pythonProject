text = input("Input text: ")
if text.isdigit():
    print(bin(int(text)))
    print(oct(int(text)))
    print(hex(int(text)))
else:
    print(text.isascii())
