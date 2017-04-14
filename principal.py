from tkinter import *
import ll

b = Tk()
b.geometry('300x400+500+100')
bn = Button(b,command= ll.inicia, text ='dale').pack()
b.mainloop()