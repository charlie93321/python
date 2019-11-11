#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk

from com.tk.gui.Button import Button


def hit_me():
    print "hello"






app = tk.Tk()

app.title('窗口')

app.geometry('500x300')

btn = tk.Button(app, text="hit me", command=hit_me)
btn2= Button(parent=app,command=hit_me,text='hit')
btn2.features(bg='red',width=500,underline=1,font=('consolas',22))


btn2.btn.pack()

app.mainloop()
