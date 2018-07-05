#Q1
'''from tkinter import *
root = Tk()
root.title('My App')
hwl = Label(root, text='Hello World')
hwl.pack()
exitb = Button(root, text='exit', width=50,command=root.destroy)
exitb.pack()
root.mainloop()'''

#Q2
'''from tkinter import *
root = Tk()
root.title('My App')
hwl = Label(root, text='Hello World')
hwl.pack()
def click():
    hwl.configure(text='welcome')
submitb = Button(root, text='Submit',command=click)
submitb.pack()
exitb = Button(root, text='exit', width=50,command=root.destroy)
exitb.pack()
root.mainloop()'''

#Q3
'''from tkinter import *
root = Tk()
root.title('My App')
root.configure(background='red')
frame1 = Frame(root, bg='black')
frame1.pack(fill=X)
frame2 = Frame(root, bg='brown')
frame2.pack(fill=X, side=BOTTOM)
lbl1 = Label(frame1, text='hello amit', bg='blue')
lbl1.pack()
lbl2 = Label(frame2, text='welcome', bg='yellow')
lbl2.pack()
def click():
    lbl2.configure(text='good bye')
submitb = Button(root, text='Submit', bg='green',activebackground='yellow',command=click)
submitb.pack()
exitb = Button(root, text='exit', width=50,command=root.destroy)
exitb.pack()
root.mainloop()'''

#Q4
'''from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
root = Tk()
root.title('My App')
name = askstring('Name', 'What is your name?')
showinfo('Hello!', 'Hi, {}'.format(name))
root.mainloop()'''