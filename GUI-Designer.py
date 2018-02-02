from tkinter import *

root = Tk()
root.title('GUI-Design')
root.geometry('1200x820')

class canvas:
    def __init__(self):
        self.c = Canvas(root,width=1000,height=800,bg='white')
        self.c.place(x=10,y=10)
    def reset(self):
        self.c.place_forget()
        self.c = Canvas(root,width=1000,height=800,bg='white')
        self.c.place(x=10,y=10)
    def point(self,x,y):
        self.c.create_oval(x-4,y-4,x+4,y+4,fill='blue')

c = canvas()
c.point(100,100)


root.mainloop()
