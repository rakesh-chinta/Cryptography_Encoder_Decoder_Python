from tkinter import *

import random
import time
import datetime

root= TK()
root.geometry("1200x6000")
root.title("Crypography Encoder-Decoder")

Tops = Frame(root, widh = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Tops = Frame(root, widh = 800, height =700, relief = SUNKEN)
f1.pack(side = LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font = ('helvetica', 50, 'bold'),
                text = "SECRET MESSAGING \n Vigenere cipher",
                fg = "Black", bd = 10, anchor = 'w')

lblinfo.grid(row = 0, column = 0)

lblinfo =  Label(Tops, font = ('arial', 20, 'bold'),
                text = localtime, fg ="Stee; Blue",
                 bd = 10, anchor = 'w')

lblinfo.grid(row = 1, column = 0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


def qExit():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

lblReference = Label(f1, font = ('arial', 16, 'bold'),
                     text = "Name:", bd = 16, anchor='w')

lblReference.grid(row = 0, column =0)



txtReference = Entry(f1, font = ('arial', 16, 'bold'),
                     textVariable = rand, bd = 16, insertwidth = 4,
                     bg = "power blue", justify = 'right')

txtReference.grid(row = 0, column =1)


lblMsg = Label(f1, font = ('arial', 16, 'bold'),
                     text = "Message:", bd = 16, anchor='w')

lblMsg.grid(row = 1, column =0)


txtMsg = Entry(f1, font = ('arial', 16, 'bold'),
                     textVariable = Msg, bd = 10, insertwidth = 4,
                     bg = "power blue", justify = 'right')

txtMsg.grid(row = 1, column =1)

lblKey = Label(f1, font = ('arial', 16, 'bold'),
                     text = "Key:", bd = 16, anchor='w')

lblMsg.grid(row = 1, column =0)


txtKey = Entry(f1, font = ('arial', 16, 'bold'),
                     textVariable = key, bd = 10, insertwidth = 4,
                     bg = "power blue", justify = 'right')

txtKey.grid(row = 2, column =1)

lblMode = Label(f1, font = ('arial', 16, 'bold'),
                     text = "MODE(e for encrypt, d for decrypt)", bd = 16, anchor='w')

lblMode.grid(row = 3, column =0)


txtMode = Entry(f1, font = ('arial', 16, 'bold'),
                     textVariable = mode, bd = 10, insertwidth = 4,
                     bg = "power blue", justify = 'right')

txtMode.grid(row = 3, column =1)


lblService = Label(f1, font = ('arial', 16, 'bold'),
                     text = "Result:", bd = 16, anchor='w')

lblService.grid(row = 2, column =2)


txtService = Entry(f1, font = ('arial', 16, 'bold'),
                     textVariable = Result, bd = 10, insertwidth = 4,
                     bg = "power blue", justify = 'right')

txtService.grid(row = 2, column =3)


import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i%len(key)]
        enc_c = chr((ord(clear[i])) +
                    ord(key_c) % 256)

        enc.append(enc_c)

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(clear)):
        key_c = key[i%len(key)]
        dec_c = chr((ord(enc[i])) +                
                    ord(key_c) % 256)

        dec.append(dec_c)

    return "".join(dec)


def Ref():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if(m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

btnTotal = Button(f1, padx = 16, pady =8, bd =16, fg = "black",
                  font('arial', 16, 'bold'), width = 10,
                  text = "Show Message", bg = "powder blue",
                  command = Ref).grid(row = 7, column = 1)

btnReset = Button(f1, padx = 16, pady =8, bd =16, fg = "black",
                  font('arial', 16, 'bold'), width = 10,
                  text = "Reset", bg = "green",
                  command = Result).grid(row = 7, column = 1)

btnExit = Button(f1, padx = 16, pady =8, bd =16, fg = "black",
                  font('arial', 16, 'bold'), width = 10,
                  text = "Exit", bg = "Red",
                  command = qExit).grid(row = 7, column = 3)

root.mainloop()


























