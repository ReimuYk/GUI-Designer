from tkinter import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('GUI-Design')
        self.root.geometry('1250x820')
        self.c = canvas(self.root)
        self.sizeframe(1080,10)
        self.pointframe(1020,70)
        self.show()
    def sizeframe(self,x,y):
        self.edge = self.c.c.create_rectangle(10,10,510,410,outline='red')
        self.ww = IntVar()
        self.ww.set(500)
        self.hh = IntVar()
        self.hh.set(400)
        f = Frame(self.root,width=50,height=200,borderwidth=2,bg='gray')
        Label(f,text=' width=').grid(column=0,row=0)
        e1 = Entry(f,textvariable=self.ww,width=9)
        e1.grid(column=1,row=0)
        Label(f,text='height=').grid(column=0,row=1)
        e2 = Entry(f,textvariable=self.hh,width=9)
        e2.grid(column=1,row=1)
        e1.bind("<Return>",self.changeSize)
        e2.bind("<Return>",self.changeSize)
        f.place(x=x,y=y)
    def changeSize(self,event):
        self.c.c.coords(self.edge,(10,10,10+self.ww.get(),10+self.hh.get()))
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

class point:
    def __init__(self,x,y,p):
        self.x=x
        self.y=y
        self.p=p
        self.recs=[]

pointlist=[]
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
        self.c.bind("<Button-1>",self.click)
        self.f.place(x=1020,y=10)
        self.select = None
    def reset(self):
        self.c.place_forget()
        self.c = Canvas(root,width=1000,height=800,bg='white')
        self.c.place(x=10,y=10)
    def point(self,x,y):
        global pointlist
        p = self.c.create_oval(x+6,y+6,x+14,y+14,fill='blue')
        item = point(x,y,p)
        pointlist.append(item)
    def rec(self,p,w,h):
        r = self.c.create_rectangle(p.x+10,p.y+10,p.x+w+10,p.y+h+10)
        p.recs.append(r)
    def click(self,event):
        p = self.searchPoint(event.x-10,event.y-10)
        if p:
            if self.select:
                self.c.itemconfig(self.select.p,fill='blue')
                if self.select==p:
                    self.select=None
                    return
            self.c.itemconfig(p.p,fill='red')
            self.select=p
    def motion(self,event):
        self.xx.set(event.x-10)
        self.yy.set(event.y-10)
    def searchPoint(self,x,y):
        for p in  pointlist:
            dx = p.x-x
            dy = p.y-y
            if dx*dx+dy*dy<=18:
                return p
        return None

g = GUI()

