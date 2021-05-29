from AES1 import AESEncrypt
from DES1 import DESEncrypt
from CC import CCEncrypt
from MD51 import MD5Encrypt
from tkinter import *
from tkinter.ttk import *

ae = AESEncrypt()
de = DESEncrypt()
md = MD5Encrypt()
cc = CCEncrypt()

master = Tk()
master.geometry("500x500")

choi = IntVar()
radio1 = Radiobutton(master, text="AES Encryption", variable=choi,
                     value=1).pack(side=TOP, ipady=5)
radio2 = Radiobutton(master, text="DES Encryption", variable=choi,
                     value=2).pack(side=TOP, ipady=5)
radio3 = Radiobutton(master, text="MD5 Encryption", variable=choi,
                     value=3).pack(side=TOP, ipady=5)
radio4 = Radiobutton(master, text="CC Encryption", variable=choi,
                     value=4).pack(side=TOP, ipady=5)


def choice():
    choice = choi.get()
    print(" ")
    if(choice == 1):
        ae.a()
    elif(choice == 2):
        key = b'0123456789abcdef'
        de.a(key)
    elif(choice == 3):
        md.gui()
    elif(choice == 4):
        cc.a()


Button(text="Click", command=choice).pack()
master.mainloop()
