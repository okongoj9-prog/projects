import zipfile

def crack_zip(zip_path, wordlist_path) :
    with open(wordlist_path, 'r', encoding= "latin-1") as wordlist:
        with zipfile.ZipFile(zip_path) as zf :
            for line in wordlist:
                password = line.strip()
                try:
                    zf.extractall(pwd=bytes(password, "utf"))
                    