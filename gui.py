from PIL import ImageTk
from tkinter import *
import PIL
import tkinter as tk
import os
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import lgin


#创建应用程序窗口
root = tkinter.Tk()
root.geometry('700x350')
varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')

#创建标签
labelName = tkinter.Label(root, text='QQ账号:',justify=tkinter.RIGHT, width=80)

#将标签放到窗口上
labelName.place(x=70, y=260, width=120, height=30)

#创建文本框，同时设置关联的变量
entryName = tkinter.Entry(root, width=80,textvariable=varName)
entryName.place(x=170, y=260, width=120, height=30)
labelPwd = tkinter.Label(root, text='QQ密码:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=370, y=260, width=120, height=30)

#创建密码文本框
entryPwd = tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
entryPwd.place(x=470, y=260, width=120, height=30)

#登录按钮事件处理函数
def login():
    name= entryName.get()
    pwd = entryPwd.get()
    lgin.loginn(name,pwd)

#创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root, text='登录',bg='cornflowerblue', command=login)
buttonOk.place(x=100, y=320, width=500, height=30)

#插入背景图片
im=Image.open("background.jpg")
img=ImageTk.PhotoImage(im)
imLabel=tk.Label(root,image=img).pack()

im2=Image.open("qie.png")
img2=ImageTk.PhotoImage(im2)
imLabel2=tk.Label(root,image=img2).pack()
    
root.mainloop()
