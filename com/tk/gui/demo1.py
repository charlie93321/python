#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk
import random
import tkFont

from com.tk.gui.Button import Button, Label, Font


def hit_me(target):
    print target.value('underline')
    varStr.set(varStr.get()+str(random.randint(1,100)))


app = tk.Tk()

app.title('窗口')

app.geometry('500x300')

btn2 = Button(parent=app, command=hit_me, text='hit me')
btn2.features(bg='red', width=500, underline=-1, font=Font(family='楷体',size=32,weight=tkFont.BOLD,slant=tkFont.ITALIC).font, fg='green')

varStr = tk.StringVar()
varStr.set("Hit me !!!")




lb1 = Label(parent=app, textvariable=varStr)

lb1.features(bg='green',font=('宋体',12),fg='black',width=150)

lb1.label.pack()
btn2.btn.pack()

app.mainloop()
