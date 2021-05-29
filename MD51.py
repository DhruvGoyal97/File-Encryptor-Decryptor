from hashlib import md5
import hashlib
import os


class MD5Encrypt:
    def encrypt_file(infile):
        with open(infile, "r") as wl:

            with open(infile + ".enc", "w") as wl_md5:

                line = wl.readline().strip()

                while line:

                    digest = md5(line.encode()).hexdigest()

                    wl_md5.write(digest)

                    line = wl.readline().strip()

    def a():
        while True:
            choice = int(input(
                "1. Press '1' to encrypt file.\n2. Press '2'to exit.\n"))
            if choice == 1:
                enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            elif choice == 2:
                exit()
            else:
                print("Please select a valid option!")


enc = MD5Encrypt
