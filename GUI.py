__author__ = 'Anindita'
import tkinter as tk
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


        def Enter_encrypt(enter=1):
            Button_encrypt.configure(bg="lavender")
        def Leave_encrypt(enter=1):
            Button_encrypt.configure(bg="#5BC8AC")


        def Enter_decrypt(enter=1):
            Button_decrypt.configure(bg="lavender")
        def Leave_decrypt(enter=1):
            Button_decrypt.configure(bg="#5BC8AC")

        w=tk.Canvas(self,width=1000,height=500,highlightthickness=0,background="#FFFFFF")
        w.place(x=0,y=0)
        w.create_rectangle(85,130,270,275,width=7)
        w.create_rectangle(315,130,500,275,width=7)
        w.create_rectangle(2,2,597,447,width=10)
        Title_label=tk.Label(self,text="Traditional Ciphers",width=20,font=("HELVETICA",20,"italic bold"),bg="#CCD1D9",fg="Black")
        Title_label.place(x=120,y=50)

        Button_encrypt=tk.Button(self,text="Encrypt",font=("HELVETICA",12,"italic bold"),width=17,height=7,bd=0,relief="flat",background="#5BC8AC",fg="Black",command=lambda:controller.show_frame(Encrypt_Frame))
        Button_encrypt.bind("<Enter>",Enter_encrypt)
        Button_encrypt.bind("<Leave>",Leave_encrypt)
        Button_encrypt.place(x=90,y=135)


        Button_decrypt=tk.Button(self,text="Decrypt",font=("HELVETICA",12,"italic bold"),width=17,height=7,bd=0,relief="flat",background="#5BC8AC",fg="Black",command=lambda:controller.show_frame(Decrypt_Frame))
        Button_decrypt.bind("<Enter>",Enter_decrypt)
        Button_decrypt.bind("<Leave>",Leave_decrypt)
        Button_decrypt.place(x=320,y=135)





class Encrypt_Frame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        w=tk.Canvas(self,width=1000,height=500,highlightthickness=0,background="#FFFFFF")
        w.place(x=0,y=0)
        w.create_line(0,125,1000,125,fill="Black",width=5)
        w.create_line(0,175,1000,175,fill="Black",width=5)
        w.create_rectangle(2,2,597,447,width=10)


        def entercaesar_button(enter=1):
            Button_caesar.configure(bg="lavender")

        def leavecaesar_button(enter=1):
            Button_caesar.configure(bg="#5BC8AC")

        def entervigenere_button(enter=1):
            Button_vigenere.configure(bg="lavender")

        def leavevigenere_button(enter=1):
            Button_vigenere.configure(bg="#5BC8AC")


        def enterotp_button(enter=1):
            Button_otp.configure(bg="lavender")

        def leaveotp_button(enter=1):
            Button_otp.configure(bg="#5BC8AC")

        def backbutton_enter(enter=1):
            back_button.configure(bg="lavender")
        def backbutton_leave(enter=1):
            back_button.configure(bg="#5BC8AC")


        plaintext_label=tk.Label(self,text="Enter your plaintext here",width=35,height=1,font=("HELVETICA",10,"italic "),background="#5BC8AC",fg="Black")
        plaintext_label.place(x=15,y=50)


        plaintext_entry=tk.Entry(self,width=30)
        plaintext_entry.place(x=320,y=50)

        Keye_label=tk.Label(self,text="Enter the key value",width=35,height=1,font=("HELVETICA",10,"italic "),background="#5BC8AC",fg="Black")
        Keye_label.place(x=15,y=90)

        Keye_entry=tk.Entry(self,width=30)
        Keye_entry.place(x=320,y=90)

        def Encipher_Caesar():
            pt=plaintext_entry.get()
            key=Keye_entry.get()
            #print(pt,key)
            value=cipher_func.caesar_encrypt(pt,key)
            print(value)
            encryption_answer.configure(text=value)

        def Encipher_Vigenere():
            pt=plaintext_entry.get()
            key=Keye_entry.get()
            value=cipher_func.vigenere_encrypt(pt,key)
            encryption_answer.configure(text=value)

        def Encipher_OTP():
            pt=plaintext_entry.get()
            key=Keye_entry.get()

            # value=cipher_func.OTP_encrypt(pt,key)
            # encryption_answer.configure(text=value)


        Button_caesar=tk.Button(self,text="Caesar",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Encipher_Caesar)
        Button_caesar.bind("<Enter>",entercaesar_button)
        Button_caesar.bind("<Leave>",leavecaesar_button)
        Button_caesar.place(x=20,y=130)

        Button_vigenere=tk.Button(self,text="Vigenere",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Encipher_Vigenere)
        Button_vigenere.bind("<Enter>",entervigenere_button)
        Button_vigenere.bind("<Leave>",leavevigenere_button)
        Button_vigenere.place(x=190,y=130)


        Button_otp=tk.Button(self,text="One Time Pad",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Encipher_OTP)
        Button_otp.bind("<Enter>",enterotp_button)
        Button_otp.bind("<Leave>",leaveotp_button)
        Button_otp.place(x=370,y=130)

        encryption_answer=tk.Label(self,text=" ",width=55,height=10,font=("HELVETICA",10,"bold"),background="#5BC8AC",fg="Black")
        encryption_answer.place(x=50,y=220)

        back_button=tk.Button(self,text="BACK",relief="flat",background="#5BC8AC",fg="Black",bd=0,width=10,height=2,command=lambda:controller.show_frame(Home))
        back_button.bind("<Enter>",backbutton_enter)
        back_button.bind("<Leave>",backbutton_leave)
        back_button.place(x=490,y=400)

class Decrypt_Frame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        w=tk.Canvas(self,width=1000,height=500,highlightthickness=0,background="#FFFFFF")
        w.place(x=0,y=0)
        w.create_line(0,125,1000,125,fill="Black",width=5)
        w.create_line(0,175,1000,175,fill="Black",width=5)
        w.create_rectangle(2,2,597,447,width=10)

        def enter_caesar(enter=1):
            Button_caesar.configure(bg="lavender")
        def leave_caesar(enter=1):
            Button_caesar.configure(bg="#5BC8AC")

        def enter_vigenere(enter=1):
            Button_vigenere.configure(bg="lavender")
        def leave_vigenere(enter=1):
            Button_vigenere.config(bg="#5BC8AC")
        def enter_otp(enter=1):
            Button_otp.configure(bg="lavender")
        def leave_otp(enter=1):
            Button_otp.configure(bg="#5BC8AC")
        def backbutton_enter(enter=1):
            back_button.configure(bg="lavender")
        def backbutton_leave(enter=1):
            back_button.configure(bg="#5BC8AC")

        ciphertext_label=tk.Label(self,text="Enter your ciphertext here",width=35,height=1,font=("HELVETICA",10,"italic "),background="#5BC8AC",fg="Black")
        ciphertext_label.place(x=15,y=50)


        ciphertext_entry=tk.Entry(self,width=30)
        ciphertext_entry.place(x=320,y=50)

        Key_label=tk.Label(self,text="Enter the cipher key value",width=35,height=1,font=("HELVETICA",10,"italic "),background="#5BC8AC",fg="Black")
        Key_label.place(x=15,y=90)

        Key_entry=tk.Entry(self,width=30)
        Key_entry.place(x=320,y=90)

        def Decipher_Caesar():   #Deciphering caesar_cipher
            pt=ciphertext_entry.get()
            key=Key_entry.get()
            value=cipher_func.caesar_decrypt(pt,key)
            decypher_answer.configure(text=value)

        def Decipher_Vigenere():           #Deciphering Vigenere cipher
            pt=ciphertext_entry.get()
            key=Key_entry.get()
            value=cipher_func.vigenere_decipher(pt,key)
            decypher_answer.configure(text=value)

        def Decipher_OTP():
            pt=ciphertext_entry.get()
            key=Key_entry.get()
            # value=cipher_func.OTP_decrypt(pt,key)
            # decypher_answer.configure(text=value)


        Button_caesar=tk.Button(self,text="Caesar",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Decipher_Caesar)
        Button_caesar.bind("<Enter>",enter_caesar)
        Button_caesar.bind("<Leave>",leave_caesar)
        Button_caesar.place(x=20,y=130)


        Button_vigenere=tk.Button(self,text="Vigenere",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Decipher_Vigenere)
        Button_vigenere.bind("<Enter>",enter_vigenere)
        Button_vigenere.bind("<Leave>",leave_vigenere)
        Button_vigenere.place(x=190,y=130)


        Button_otp=tk.Button(self,text="One Time Pad",width=13,height=2,font=("HELVETICA",10,"italic bold"),bd=0,relief="flat",background="#5BC8AC",fg="Black",command=Decipher_OTP)
        Button_otp.bind("<Enter>",enter_otp)
        Button_otp.bind("<Leave>",leave_otp)
        Button_otp.place(x=370,y=130)

        decypher_answer=tk.Label(self,text=" ",width=55,height=10,font=("HELVETICA",10,"bold"),background="#5BC8AC",fg="Black")
        decypher_answer.place(x=50,y=220)


        back_button=tk.Button(self,text="BACK",relief="flat",background="#5BC8AC",fg="Black",bd=0,width=10,height=2,command=lambda:controller.show_frame(Home))
        back_button.bind("<Enter>",backbutton_enter)
        back_button.bind("<Leave>",backbutton_leave)
        back_button.place(x=490,y=400)



app=main()
app.mainloop()

