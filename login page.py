"""
PYTHON TUTORIALS
LOGIN PAGE CREAATION
TKINTER SERIES - IX
"""

from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

mycon = sql.connect(host= 'localhost', user = 'root', passwd = 'root',database = 'test')
cur = mycon.cursor()

def f2():
    global frame2
    frame1.destroy()
    frame2 = Frame(root,height = 500, width = 700,bg = '#D3D3D3')
    frame2.place(x= 0, y = 0)
    l0 = Label(frame2,text = 'LOGIN SUCCESSFUL',font = ('normal',25,'bold'),bg = '#D3D3D3')
    l0.place(x = 230 , y = 90)

    b1 = Button(frame2,text = 'LOG OUT',font = ('normal', 15),command = f1)
    b1.place(x = 330, y = 300)
    
def submit():
    cur.execute('select username,password from register')
    total = cur.fetchall()
    username = t1.get()
    password = t2.get()
    for i in total:
        if username == i[0] and password == i[1]:
            return f2()
        elif username == i[0] and password != i[1]:
            messagebox.showinfo('ALERT!','ENTER CORRECT PASSWORD')
            e2.delete(0,END)
            break
    else:
        messagebox.showinfo('ALERT!','ACCOUNT IS NOT REGISTERED')
        e1.delete(0,END)
        e2.delete(0,END)
        
        
    
def f1():
    global t1,t2,frame1,e1,e2
    try:
        frame2.destroy()
    except:
        pass
    frame1 = Frame(root,height = 500, width = 700,bg = '#D3D3D3')
    frame1.place(x= 0, y = 0)
    l0 = Label(frame1,text = 'LOGIN PAGE',font = ('normal',25,'bold'),bg = '#D3D3D3')
    l0.place(x = 230 , y = 90)

    l1 = Label(frame1, text = 'USERNAME',font = ('arial',15,'normal'),bg = '#D3D3D3')
    l1.place(x = 150, y= 195)

    l2 = Label(frame1, text = 'PASSWORD',font = ('arial',15,'normal'),bg = '#D3D3D3')
    l2.place(x= 150 , y = 230)

    t1 = StringVar()
    t2 = StringVar()

    e1 = Entry(frame1,width = 20 , font = ('normal',15),bd = 3,textvariable = t1)
    e1.place(x = 300, y = 195)

    e2 = Entry(frame1,width = 20 , font = ('normal',15),bd = 3,textvariable = t2,show = '*')
    e2.place(x = 300, y = 230)

    b1 = Button(frame1,text = 'SUBMIT',font = ('normal', 15),command = submit)
    b1.place(x = 330, y = 300)

    

root = Tk()
root.title('LOGIN PAGE')
root.geometry('700x500')
f1()
root.mainloop()
