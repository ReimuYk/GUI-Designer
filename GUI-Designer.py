from tkinter import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('GUI-Design')
        self.root.geometry('1250x820')
        self.c = canvas(self.root)
        self.c.rec(0,0,500,400)
        self.pointframe(1020,70)
        self.show()
    def pointframe(self,x,y):
        f = Frame(self.root,width=190,height=200,borderwidth=2,bg='gray')
        xx = IntVar()
        yy = IntVar()
        Label(f,text='x=').grid(column=0,row=0)
        e1 = Entry(f,textvariable=xx)
        e1.grid(column=1,row=0)
        Label(f,text='y=').grid(column=0,row=1)
        e2 = Entry(f,textvariable=yy)
        e2.grid(column=1,row=1)
        Button(f,text='clear').grid(row=2,column=0)
        Button(f,text='point',command=lambda:self.c.point(xx.get(),yy.get())).grid(row=2,column=1)
        f.place(x=x,y=y)
    def show(self):
        self.root.mainloop()

class canvas:
    def __init__(self,root):
        self.c = Canvas(root,width=1000,height=800,bg='white')
        self.c.place(x=10,y=10)
        self.f = Frame(root,width=190,height=200,borderwidth=2,bg='gray')
        Label(self.f,text='x=').grid(row=0,column=0)
        self.xx = IntVar()
        Label(self.f,textvariable=self.xx).grid(row=0,column=1)
        Label(self.f,text='y=').grid(row=1,column=0)
        self.yy = IntVar()
        Label(self.f,textvariable=self.yy).grid(row=1,column=1)
        self.c.bind("<Motion>",self.motion)
        self.f.place(x=1020,y=10)
    def reset(self):
        self.c.place_forget()
        self.c = Canvas(root,width=1000,height=800,bg='white')
        self.c.place(x=10,y=10)
    def point(self,x,y):
        self.c.create_oval(x+6,y+6,x+14,y+14,fill='blue')
    def rec(self,x,y,w,h):
        self.c.create_rectangle(x+10,y+10,x+w+10,y+h+10)
    def motion(self,event):
        self.xx.set(event.x-10)
        self.yy.set(event.y-10)

g = GUI()

