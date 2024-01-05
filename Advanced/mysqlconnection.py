from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random

class memberConnect:

    def __init__(self,root):
         self.root = root
         blankSpace=" "
         self.root.title(202 * blankSpace + "Mysql Connector")
         self.root.resizable(width=False, height=False)
         self.root.geometry("1360x700+0+0")

if __name__=='__main__':
    root=Tk()
    application = memberConnect(root)
    root.mainloop()