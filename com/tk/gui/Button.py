#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk
import tkFont


class Label():
    '''
    text	1. 指定 Label 显示的文本
        2. 文本可以包含换行符
        3. 如果设置了 bitmap 或 image 选项，该选项则被忽略
    bitmap	1. 指定显示到 Label 上的位图
        2. 如果指定了 image 选项，则该选项被忽略
    image	1. 指定 Label 显示的图片
        2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
        3. 该选项优先于 text 和 bitmap 选项

    textvariable	1. Label 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
                2. 如果变量被修改，Label 的文本会自动更新
    '''

    def __init__(self, parent, image=None, bitmap=None, text=None, textvariable=None):
        self.parent = parent
        self.image = image
        self.bitmap = bitmap
        self.text = text
        self.textvariable = textvariable
        if self.image is not None:
            self.label = tk.Label(master=parent, image=self.image)
        elif self.bitmap is not None:
            self.label = tk.Label(master=parent, bitmap=self.bitmap)
        elif textvariable is not None:
            self.label = tk.Label(master=parent, textvariable=self.textvariable)
        else:
            self.label = tk.Label(master=parent, text=self.text)
        self.featureMap = {'parent': parent, 'image': self.image, 'bitmap': self.bitmap, 'text': self.textvariable,
                           'textvariable': self.textvariable}

    '''
    
    anchor	    1. 控制文本（或图像）在 Label 中显示的位置
                2. "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位（ewsn 代表东西南北，上北下南左西右东）
                     默认值是 "center"
    bg	跟 background 一样
     
    bd	1. 指定 Label 的边框宽度
                2. 默认值由系统指定，通常是 1 或 2 像素
    
    
    font	1. 指定 Label 中文本的字体(注：如果同时设置字体和大小，应该用元组包起来，如（"楷体", 20）
            2. 一个 Label 只能设置一种字体
            3. 默认值由系统指定
    fg	1. 设置 Label 的文本和位图的颜色
                2. 默认值由系统指定
    
    height	1. 设置 Label 的高度
            2. 如果 Label 显示的是文本，那么单位是文本单元
            3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
            4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出高度
    
     
    justify	1. 定义如何对齐多行文本
            2. 使用 "left"，"right" 或 "center"
            3. 注意，文本的位置取决于 anchor 选项
            4. 默认值是 "center"
    padx	1. 指定 Label 水平方向上的额外间距（内容和边框间）
            2. 单位是像素
    pady	1. 指定 Label 垂直方向上的额外间距（内容和边框间）
            2. 单位是像素
    relief	1. 指定边框样式
            2. 默认值是 "flat"
            3. 另外你还可以设置 "groove", "raised", "ridge", "solid" 或者 "sunken"
    state	1. 指定 Label 的状态
            2. 这个标签控制 Label 如何显示
            3. 默认值是 "normal
            4. 另外你还可以设置 "active" 或 "disabled"
    
                 
    underline	1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键） 
                2. 默认值是 -1
                3. 例如设置为 1，则说明在 Button 的第 2 个字符处画下划线
    width	1. 设置 Label 的宽度
            2. 如果 Label 显示的是文本，那么单位是文本单元
            3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
            4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出宽度
    wraplength	1. 决定 Label 的文本应该被分成多少行
                2. 该选项指定每行的长度，单位是屏幕单元
                3. 默认值是 0
                
                
                
    takefocus	1. 如果是 True，该 Label 接受输入焦点
    2. 默认值是 False
    
    highlightbackground	1. 指定当 Label 没有获得焦点的时候高亮边框的颜色
            2. 默认值由系统指定，通常是标准背景颜色
    highlightcolor	1. 指定当 Label 获得焦点的时候高亮边框的颜色
        2. 默认值由系统指定
    highlightthickness	1. 指定高亮边框的宽度
            2. 默认值是 0（不带高亮边框）
                        
    compound	1. 控制 Label 中文本和图像的混合模式
                2. 默认情况下，如果有指定位图或图片，则不显示文本
                3. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
                4. 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方）
                5. 默认值是 NONE
    cursor	    1. 指定当鼠标在 Label 上飘过的时候的鼠标样式
                2. 默认值由系统指定
    disabledforeground	1. 指定当 Label 不可用的时候前景色的颜色
                        2. 默认值由系统指定
    '''

    def value(self, name):
        return self.featureMap[name]

    def features(self, width=None, height=None, bd=None, fg=None, bg=None, padx=None, pady=None, font=None, relief=None,
                 underline=None, state=None, justify=None, wraplength=None, anchor=None,
                 takefocus=False, highlightbackground=None, highlightcolor=None, highlightthickness=0, compound=None,
                 cursor=None, disabledforeground=None):
        if width is not None:
            self.label.configure(width=width)
            self.featureMap['width'] = width
        if height is not None:
            self.label.configure(height=height)
            self.featureMap['height'] = height
        if bd is not None:
            self.label.configure(bd=bd)
            self.featureMap['bd'] = bd
        if fg is not None:
            self.label.configure(fg=fg)
            self.featureMap['fg'] = fg
        if bg is not None:
            self.label.configure(bg=bg)
            self.featureMap['bg'] = bg
        if padx is not None:
            self.label.configure(padx=padx)
            self.featureMap['padx'] = padx
        if pady is not None:
            self.label.configure(pady=pady)
            self.featureMap['pady'] = pady
        if font is not None:
            self.label.configure(font=font)
            self.featureMap['font'] = font
        if relief is not None:
            self.label.configure(relief=relief)
            self.featureMap['relief'] = relief
        if underline is not None:
            self.label.configure(underline=underline)
            self.featureMap['underline'] = underline
        if state is not None:
            self.label.configure(state=state)
            self.featureMap['state'] = state
        if justify is not None:
            self.label.configure(justify=justify)
            self.featureMap['justify'] = justify
        if wraplength is not None:
            self.label.configure(wraplength=wraplength)
            self.featureMap['wraplength'] = wraplength
        if anchor is not None:
            self.label.configure(anchor=anchor)
            self.featureMap['anchor'] = anchor

        '''
        takefocus=False,highlightbackground=None,highlightcolor=None,highlightthickness=0,compound=None,cursor=None,disabledforeground=None
        '''
        if takefocus is not None:
            self.label.configure(takefocus=takefocus)
            self.featureMap['takefocus'] = takefocus
        if highlightbackground is not None:
            self.label.configure(highlightbackground=highlightbackground)
            self.featureMap['highlightbackground'] = highlightbackground
        if highlightcolor is not None:
            self.label.configure(highlightcolor=highlightcolor)
            self.featureMap['highlightcolor'] = highlightcolor
        if highlightthickness is not None:
            self.label.configure(highlightthickness=highlightthickness)
            self.featureMap['highlightthickness'] = highlightthickness
        if compound is not None:
            self.label.configure(compound=compound)
            self.featureMap['compound'] = compound
        if cursor is not None:
            self.label.configure(cursor=cursor)
            self.featureMap['cursor'] = cursor
        if disabledforeground is not None:
            self.label.configure(disabledforeground=disabledforeground)
            self.featureMap['disabledforeground'] = disabledforeground

    '''
         activebackground	1. 设置当 Label 处于活动状态（通过 state 选项设置状态）的背景色
                    2. 默认值由系统指定
        activeforeground	1. 设置当 Label 处于活动状态（通过 state 选项设置状态）的前景色
                        2. 默认值由系统指定
    '''

    def activebackground(self, activebackground):
        if activebackground is not None:
            self.label.configure(activebackground=self.activebackground)
            self.featureMap['activebackground'] = activebackground

    def activeforeground(self, activeforeground):
        if activeforeground is not None:
            self.label.configure(activeforeground=self.activeforeground)
            self.featureMap['activeforeground'] = activeforeground


class Button():
    '''
      parent:父容器
      command:按钮关联的函数，当按钮被点击时，执行该函数
      text:按钮的文本内容
    '''

    def event(self):
        self.command(self)

    def __init__(self, parent, command, text):
        self.parent = parent
        self.command = command
        self.text = text
        self.btn = tk.Button(master=self.parent, command=self.event, text=self.text)
        self.featureMap = {'parent': self.parent, 'text': text}

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

    def value(self, name):
        return self.featureMap[name]

    def features(self, width=None, height=None, bd=None, fg=None, bg=None, padx=None, pady=None, font=None, relief=None,
                 underline=None, state=None, image=None, justify=None, wraplength=None, anchor=None):
        if width is not None:
            self.btn.configure(width=width)
            self.featureMap['width'] = width
        if height is not None:
            self.btn.configure(height=height)
            self.featureMap['height'] = height
        if bd is not None:
            self.btn.configure(bd=bd)
            self.featureMap['bd'] = bd
        if fg is not None:
            self.btn.configure(fg=fg)
            self.featureMap['fg'] = fg
        if bg is not None:
            self.btn.configure(bg=bg)
            self.featureMap['bg'] = bg
        if padx is not None:
            self.btn.configure(padx=padx)
            self.featureMap['padx'] = padx
        if pady is not None:
            self.btn.configure(pady=pady)
            self.featureMap['pady'] = pady
        if font is not None:
            self.btn.configure(font=font)
            self.featureMap['font'] = font
        if relief is not None:
            self.btn.configure(relief=relief)
            self.featureMap['relief'] = relief
        if underline is not None:
            self.btn.configure(underline=underline)
            self.featureMap['underline'] = underline
        if state is not None:
            self.btn.configure(state=state)
            self.featureMap['state'] = state
        if image is not None:
            self.btn.configure(image=image)
            self.featureMap['image'] = image
        if justify is not None:
            self.btn.configure(justify=justify)
            self.featureMap['justify'] = justify
        if wraplength is not None:
            self.btn.configure(wraplength=wraplength)
            self.featureMap['wraplength'] = wraplength
        if anchor is not None:
            self.btn.configure(anchor=anchor)
            self.featureMap['anchor'] = anchor

    '''
         activebackground: 当鼠标放上去时，按钮的背景色
         activeforeground:当鼠标放上去时，按钮的前景色
    '''

    def activebackground(self, activebackground):
        if activebackground is not None:
            self.btn.configure(activebackground=self.activebackground)
            self.featureMap['activebackground'] = activebackground

    def activeforeground(self, activeforeground):
        if activeforeground is not None:
            self.btn.configure(activeforeground=self.activeforeground)
            self.featureMap['activeforeground'] = activeforeground

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

        '''
1）family 为字体类型，如family='Times'（新罗马字体）,family=' 微软雅黑'等

2）size 字体大小，字体大小以磅为单位。要以像素为单位给出大小，前面加一个负号

3）weight 是否加粗，默认为NORMAL，如果设置加粗使用weight = tf.BOLD

4）slant 是否斜体，模型为NORAML，如果设置斜体使用slant  = tf.ITALIC  must be roman, or italic

5）underline 是否有下划线，默认为0(false)，如果设置下划线使用underline = 1(true)

6）overstrike 是否有删除线，默认为0（false），如果设置删除线使用overstrike = 1（true）
        '''


class Font():
    def __init__(self, family='Consolas', size=12, weight=tkFont.NORMAL, slant=tkFont.ROMAN, underline=0,
                 overstrike=0):
        self.family = family
        self.size = size
        self.weight = weight
        self.slant = slant
        self.underline = underline
        self.overstrike = overstrike
        self.font = tkFont.Font(family=self.family, size=self.size, weight=self.weight, slant=self.slant,
                                underline=self.underline, overstrike=self.overstrike)
