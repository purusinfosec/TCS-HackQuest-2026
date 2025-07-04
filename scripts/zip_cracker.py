import zipfile
wordlist = input("Wordlist file: ")
zip_file = input("ZIP file path: ")
with zipfile.ZipFile(zip_file) as zf:
    for word in open(wordlist):
        try:
            zf.extractall(pwd=word.strip().encode())
            print("[+] Password:", word)
            break
        except:
            continue
