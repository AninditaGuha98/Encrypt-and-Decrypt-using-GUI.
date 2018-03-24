__author__ = 'Anindita'
import Tkinter as tk
import cipher_func

class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        def move_window(event):
               self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        tk.Tk.title(self,"File Transfer")
        tk.Tk.wm_overrideredirect(self,True)
        tk.Tk.wm_resizable(self,0,0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        #tk.Tk.iconbitmap(self,default="aa.ico")
        self.bind('<B1-Motion>', move_window)



        def enterb(event):
            btn_close.configure(text="X",background="#C60000")
        def leaveb(event):
            btn_close.configure(text="X",background="#04202C")


        btn_close=tk.Button(self,width=3,text="X",relief="flat",bg="#04202c",fg="White",bd=0,activebackground="#777777",command=self.destroy,font=('Berlin Sans FB',15))
        btn_close.bind("<Enter>",enterb)
        btn_close.bind("<Leave>",leaveb)
        btn_close.place(x=560,y=3)


        self.frames = {}

        for F in (Home,Encrypt_Frame,Decrypt_Frame):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.winfo_toplevel().geometry("600x450")

class Home(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        w=tk.Canvas(self,width=1000,height=500,highlightthickness=0,background="#CCD1D9")
        w.place(x=0,y=0)

        Button_encrypt=tk.Button(self,text="Encrypt",font=("HELVETICA",12,"italic bold"),width=15,height=5,bd=0,relief="flat",background="#5BC8AC",fg="Black",command=lambda:controller.show_frame(Encrypt_Frame))
        Button_encrypt.place(x=100,y=150)


        Button_decrypt=tk.Button(self,text="Decrypt",font=("HELVETICA",12,"italic bold"),width=15,height=5,bd=0,relief="flat",background="#5BC8AC",fg="Black",command=lambda:controller.show_frame(Decrypt_Frame))
        Button_decrypt.place(x=330,y=150)





class Encrypt_Frame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        plaintext_label=tk.Label(self,text="Enter your plaintext here",width=20,height=1,font=("HELVETICA",12,"italic bold"),background="#5BC8AC",fg="Black")
        plaintext_label.place(x=40,y=50)


        plaintext_entry=tk.Entry(self,width=30)
        plaintext_entry.place(x=280,y=50)

        def Encipher_Caesar():
            pt=plaintext_entry.get()
            print(pt)
            value=cipher_func.caesar_encrypt(pt)
            Caesar_encryption_answer.configure(text=value)


        Button_line=tk.Button(self,width=500,height=1,bd=0,relief="flat",state="disabled",background="black")
        Button_line.place(x=0,y=80)


        Button_caesar=tk.Button(self,text="Caesar",width=8,height=2,font=("HELVETICA",12,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Encipher_Caesar)
        Button_caesar.place(x=20,y=120)


        Button_caesar=tk.Button(self,text="Playfair",width=8,height=2,font=("HELVETICA",12,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black")
        Button_caesar.place(x=130,y=120)


        Caesar_encryption_answer=tk.Label(self,text=" ",width=40,height=10,font=("HELVETICA",12,"italic bold"),background="#5BC8AC",fg="Black")
        Caesar_encryption_answer.place(x=110,y=230)



class Decrypt_Frame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


app=main()
app.mainloop()

