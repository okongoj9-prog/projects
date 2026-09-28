import zipfile

zipfile = "protected.zip"
wordlist_path = "passwords.txt"

with zipfile.ZipFile(zipfile) as zf :
    with open(wordlist_path, 'r', encoding='utf-8') as f:
        for line in f:
            pwd = line.strip()
            try :
                zf.extractall(pwd=pwd.encode('utf-8'))
                print(f"Password found: {pwd}")
                break
            except (RuntimeError, zipfile.BadZipFile):
                continue