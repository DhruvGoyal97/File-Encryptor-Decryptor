from Cryptodome.Cipher import DES3

import base64
import os


class DESEncrypt:
    def encrypt_file(self, key, in_filname, out_filename=None, chunksize=16*1024):
        if not out_filename:
            out_filename = in_filname + ".enc"
            iv = os.urandom(8)
            encryptor = DES3.new(key, DES3.MODE_CBC, iv)
        with open(in_filname, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16-len(chunk) % 16)
                    outfile.write(encryptor.encrypt(chunk))
                    chunkd = encryptor.encrypt(chunk)
                    chunkd = base64.b64encode(chunkd).decode()

    def decrypt_file(self, key, in_filname, out_filename, chunksize=16*1024):
        with open(in_filname, 'rb') as infile:
            iv = infile.read(8)
            decryptor = DES3.new(key, DES3.MODE_CBC, iv)
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

    def a(self, key):
        if os.path.isfile('data.txt.enc'):
            while True:
                password = str(input("Enter password: "))
                self.decrypt_file(key, "data.txt.enc",
                                  "g.txt", chunksize=16*1024)
                p = ''
                with open("data.txt", "r") as f:
                    p = f.readlines()
                if p[0] == password:
                    self.encrypt_file(key, "data.txt", chunksize=16*1024)
                    break
            while True:
                choice = int(input(
                    "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to exit.\n"))
                if choice == 1:
                    self.encrypt_file(
                        key, str(input("Enter name of file to encrypt: ")), chunksize=16*1024)
                elif choice == 2:
                    self.decrypt_file(
                        key, str(input("Enter name of file to decrypt: ")), "w.txt", chunksize=16*1024)
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
            self.encrypt_file(key, "data.txt", chunksize=16*1024)
            print("Please restart the program to complete the setup")


enc = DESEncrypt()
