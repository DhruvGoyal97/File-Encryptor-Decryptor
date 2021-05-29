import os


class CCEncrypt:
    def encrypt_file(self, infile, s):
        with open(infile, "r") as data:
            with open(infile + ".enc", "w") as data1:
                text = data.readline()
                result = ""

                # traverse text
                for i in range(len(text)):
                    char = text[i]
                    if(ord(char) == 32):
                        result += ' '
                    # Encrypt uppercase characters
                    elif (char.isupper()):
                        result += chr((ord(char) + s-65) % 26 + 65)

                    # Encrypt lowercase characters
                    else:
                        result += chr((ord(char) + s - 97) % 26 + 97)
                data1.write(result)
                data1.close()

    def decrypt_file(self, infile, s):
        with open(infile, "r") as data:
            with open("a.txt", "w") as data1:
                text = data.readline()
                result = ""

                # traverse text
                for i in range(len(text)):
                    char = text[i]
                    if(ord(char) == 32):
                        result += ' '
                    # Encrypt uppercase characters
                    elif (char.isupper()):
                        result += chr((ord(char) - s-65) % 26 + 65)

                    # Encrypt lowercase characters
                    else:
                        result += chr((ord(char) - s - 97) % 26 + 97)
                data1.write(result)
                data1.close()

    def a(self):
        if os.path.isfile('data.txt.enc'):
            while True:
                password = str(input("Enter password: "))
                self.decrypt_file("data.txt.enc", 5)
                p = ''
                with open("data.txt", "r") as f:
                    p = f.readlines()
                if p[0] == password:
                    self.encrypt_file("data.txt", 5)
                    break

            while True:
                choice = int(input(
                    "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to exit.\n"))
                if choice == 1:
                    self.encrypt_file(
                        input("Enter name of file to encrypt: "), int(password))
                elif choice == 2:
                    self.decrypt_file(
                        str(input("Enter name of file to decrypt: ")), int(password))
                elif choice == 3:
                    exit()
                else:
                    print("Please select a valid option!")

        else:
            while True:
                password = str(
                    input("Setting up stuff. Enter a password that will be used for decryption: "))
                repassword = str(input("Confirm password: "))
                if password == repassword:
                    break
                else:
                    print("Passwords Mismatched!")
            f = open("data.txt", "w+")
            f.write(password)
            f.close()
            self.encrypt_file("data.txt", 5)
            print("Please restart the program to complete the setup")


enc = CCEncrypt()
