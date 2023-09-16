from zipfile import ZipFile

zippath = input("Enter the path to zip file: ")
wordlist = input("Enter the path to wordlist: ")
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile(zippath) as zf:
        with open(wordlist, 'rb') as f:
            passwords = f.read().decode('utf-8').splitlines()

            for password in passwords:
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    break
            else:
                print("[+] Password not found in list")

if __name__ == "__main__":
    main()
