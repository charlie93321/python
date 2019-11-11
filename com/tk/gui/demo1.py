#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk

from com.tk.gui.Button import Button


def hit_me(target):

    print target.value('underline')






app = tk.Tk()

app.title('窗口')

app.geometry('500x300')


btn2= Button(parent=app,command=hit_me,text='hit me')
btn2.features(bg='red',width=500,underline=1,font=('Consolas',16),fg='green')


btn2.btn.pack()

app.mainloop()
