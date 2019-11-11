#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk


class Button():
    '''
      parent:父容器
      command:按钮关联的函数，当按钮被点击时，执行该函数
      text:按钮的文本内容
    '''

    def __init__(self, parent, command, text):
        self.parent = parent
        self.command = command
        self.text = text
        self.btn = tk.Button(master=self.parent, command=self.command, text=self.text)

    '''
        bg:按钮的背景色
        fg:按钮的前景色(按钮文本的颜色)
        bd:按钮边框的大小，默认为 2 个像素
        height:按钮的高度
        width:按钮的宽度，如未设置此项，其大小以适应按钮的内容（文本或图片的大小）
        padx:按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离
        pady:按钮在y轴方向上的内边距(padding)
        font:文本字体
        relief:边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
        underline:下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
        state:设置按钮组件状态,可选的有NORMAL、ACTIVE、 DISABLED。默认 NORMAL。
        highlightcolor:要高亮的颜色
        image:按钮上要显示的图片
        justify:显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
        wraplength:限制按钮每行显示的字符的数量
        anchor:锚选项，控制文本的位置，默认为中心
    '''

    def features(self, width=None, height=None, bd=None, fg=None, bg=None, padx=None, pady=None, font=None, relief=None,
                 underline=None, state=None, image=None, justify=None, wraplength=None, anchor=None):
        if width is not None:
            self.btn.configure(width=width)
        if height is not None:
            self.btn.configure(height=height)
        if bd is not None:
            self.btn.configure(bd=bd)
        if fg is not None:
            self.btn.configure(fg=fg)
        if bg is not None:
            self.btn.configure(bg=bg)
        if padx is not None:
            self.btn.configure(padx=padx)
        if pady is not None:
            self.btn.configure(pady=pady)
        if font is not None:
            self.btn.configure(font=font)
        if pady is not None:
            self.btn.configure(pady=pady)
        if relief is not None:
            self.btn.configure(relief=relief)
        if underline is not None:
            self.btn.configure(underline=underline)
        if state is not None:
            self.btn.configure(state=state)
        if image is not None:
            self.btn.configure(image=image)
        if justify is not None:
            self.btn.configure(justify=justify)
        if wraplength is not None:
            self.btn.configure(wraplength=wraplength)
        if anchor is not None:
            self.btn.configure(anchor=anchor)

    '''
         activebackground: 当鼠标放上去时，按钮的背景色
         activeforeground:当鼠标放上去时，按钮的前景色
    '''

    def activebackground(self, activebackground):
        if activebackground is not None:
            self.btn.configure(activebackground=self.activebackground)

    def activeforeground(self, activeforeground):
        if activeforeground is not None:
            self.btn.configure(activeforeground=self.activeforeground)

    '''
        deselect() 	清除单选按钮的状态
        flash() 	在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
        invoke() 	可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
        select() 	设置单选按钮为选中。
    '''

    def deselect(self):
        self.btn.deselect()

    def flash(self):
        self.btn.flash()

    def invoke(self):
        self.btn.invoke()

    def select(self):
        self.btn.select()
