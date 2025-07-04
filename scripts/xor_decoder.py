text = input("Enter XORed text (comma-separated bytes): ").split(',')
key = int(input("Enter XOR key: "))
result = ''.join([chr(int(b) ^ key) for b in text])
print("Decoded:", result)
