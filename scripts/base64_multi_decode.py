import base64
text = input("Base64 encoded text: ")
for _ in range(5):
    try:
        text = base64.b64decode(text).decode()
    except:
        break
print("Decoded:", text)

