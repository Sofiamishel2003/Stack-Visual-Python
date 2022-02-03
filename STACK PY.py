from tkinter import Tk, Label, Entry, Button, messagebox, END, DISABLED
class app(Tk):
    def __init__(self):
        Tk.__init__(self) #constructor
        self.st=stack(10,self,300)
        self.geometry("450x280")
        self.config(bg="thistle")
        self.title("STACK")
        self.l1=Label(self,text="Ingrese dato:")
        self.l1.place(x=10,y=20)
        self.c1=Entry(widt=20)
        self.c1.place(x=100, y=20)
        self.b1=Button(text="Push", command=self.dopush, width=5)
        self.b1.place(x=10,y=50)
        self.b2=Button(text="Pop", command=self.dopop, width=5)
        self.b2.place(x=60,y=50)
        self.b3=Button(text="Top", command=self.dotop, width=5)
        self.b3.place(x=110,y=50)
        self.b4=Button(text="Empty", command=self.doempty, width=5)
        self.b4.place(x=160,y=50)
        self.b4=Button(text="Make Null", command=self.domaken, width=7)
        self.b4.place(x=210,y=50)
        self.Ls= Label(self,text="*STACK*",bg="lightsteelblue")
        self.Ls.place(x=310,y=0)
    def domaken(self):
        dato=self.st.maken()
        self.c1.delete(0,END)
    def doforma(self):
        f1=app
    def dopush(self):
        try:
            dato=self.c1.get()
            if dato !="":
                self.st.push(dato)
                self.c1.delete(0, END)
            else:
                messagebox.showerror("Error", "Debe ingresar un dato")
        except Exception as msg:
            messagebox.showerror("Error de stack", msg)
    def dopop(self):
        try:
            dato=self.st.pop()
            self.c1.delete(0,END)
            self.c1.insert(0,dato)
        except Exception as msg:
            messagebox.showerror("Error", msg)
    def dotop(self):
        try:
            dato=self.st.top()
            self.c1.delete(0,END)
            self.c1.insert(0,dato)
        except Exception as msg:
            messagebox.showerror("Error", msg)
    def doempty(self):
        self.c1.delete(0,END)
        self.c1.insert(0,str(self.st.empty()))
class stack():
    def __init__(self,t,f,px):
        self.data=[""]*t    #Propiedades del stack
        self.sp=0
        self.tam=t
        self.forma=f
        self.left=px
        for i in range(t):
            self.data[i]=Button(self.forma, width=10,state=DISABLED)
            self.data[i].place(x=px,y=t*25-i*25)
        self.flecha=Label(self.forma,text="←",bg="lightsteelblue")
        self.flecha.place(x=px+85,y=t*25+5)
    def push(self,e):     #Metodos de objeto
        if self.sp<self.tam:
            self.data[self.sp].configure(text=e)
            self.sp+=1
            self.flecha.place(x=self.left+85,y=self.tam*25-self.sp*25+5)
        else:
            raise Exception("Stack overflow")
    def pop(self):
        if self.sp>0:
            self.sp-=1
            self.flecha.place(x=self.left+85,y=self.tam*25-self.sp*25+5)
            temp=self.data[self.sp].configure("text")[-1]
            self.data[self.sp].configure(text="")
            return temp
        else: 
            raise Exception("Stack underflow")
    def top(self):
        if self.sp>0:
            return self.data[self.sp-1].configure("text")[-1]
        else:
            raise Exception("Stack underflow")
    def empty(self):
        return self.sp==0
    def maken(self):
        for i in range(self.tam):
            self.data[i].configure(text="")
        self.sp=0
        self.flecha.configure(text="")
app().mainloop()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Repasar  y experimentar con stacks 
#Lenguaje: python 3.7
#Net Framewor: 4.5
#Recursos: Python, visual studio
#Descripción: Desarrollar un programa que permita ingresar valores a un stacck y realizar las óperaciones de pop, top, empty y push y mostrar el stack visualmente
#Ultima modificación 12/02/2021

