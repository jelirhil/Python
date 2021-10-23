from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #background
        self.bg = PhotoImage(file="criacoes python\j1.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #login frame
        Frame_login= Frame(self.root, bg= "white")
        Frame_login.place(x=330, y=150, width=500, height=400)

        #title and subtitle
        title= Label(Frame_login, text="Login Aqui", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle= Label(Frame_login, text="Membros log area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

        #Username
        lbl_user= Label(Frame_login, text="Usuario", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=140)
        self.username= Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90 ,y=170, width=320, height=35)

        #SENHA
        lbl_user= Label(Frame_login, text="Senha", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=210)
        self.password= Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90 ,y=240, width=320, height=35)

        #button
        forget=Button(Frame_login, text="Esqueceu senha?", cursor="hand2", bd=0, font=("Goudy old style", 10, "bold"), fg="#6162FF", bg="white").place(x=340, y=280)
        register=Button(Frame_login, text="Registrar", cursor="hand2", bd=0, font=("Goudy old style", 10, "bold"), fg="#6162FF", bg="white").place(x=90, y=280)
        submit=Button(Frame_login, command=self.check_function, text="Login", cursor="hand2",bd=0, font=("Goudy old style", 15, "bold"), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)
    
    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("ERRO", "Preencha todos campos", parent= self.root)
            elif self.username.get()!="jonathan" or self.password.get()!="1234":
                messagebox.showerror("ERRO", "Nome ou senha invalidos", parent= self.root)
            else:
                messagebox.showinfo("Bem_Vindo", f"Bem_Vindo {self.username.get()}")   

        
root = Tk() 
obj=Login(root)
root.mainloop()      