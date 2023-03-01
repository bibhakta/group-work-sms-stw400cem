from tkinter import *            #tkinter module import garya
from tkinter import messagebox
import sqlite3
root = Tk()                      #Tk()function lai variable name declare garnu parxa ani window create bhayo 
root.title("Register Page")              #title naya rakhna lai title fuction bydefault chai Tk hunxa
root.iconbitmap('img/students.ico')     #icon  change garna
root.geometry('900x500+200+2')
root.configure(bg='#fff')  #bg color change garne
image=PhotoImage(file='img/loggg.png') #adding img
Label(root,image=image,bg='white').place(x=400,y=40) #placing img


#Registration page
def clear():
    firstname.delete(0,END)
    lastname.delete(0,END)
    add.delete(0,END)
    email.delete(0,END)
    pas.delete(0,END)
    newpas.delete(0,END)

def signup():
    if firstname.get()=='' or lastname.get()== '' or add.get()== ''  or email.get()== ''  or pas.get()== '' or newpas.get()== '':
        messagebox.showerror("Error","one or more fields empty!")
    elif pas.get() != newpas.get():
        messagebox.showerror("Error","Password didnot matches")
    elif "@" and ".com" not in email.get():
        messagebox.showerror("Error","Invalid Email")
    else:
        try:
            connection=sqlite3.connect("register_std.db")
            cur=connection.cursor()
        except:
            messagebox.showerror('error','Database connectivity Issue,Please try again')
            return

        cur.execute("INSERT INTO Account VALUES (:FirstName, :LastName, :Phone, :Email, :Password, :ConfirmPass)",
        {
            'FirstName':firstname.get(), 
            'LastName':lastname.get(), 
            'Phone':add.get(), 
            'Email':email.get(), 
            'Password':pas.get(), 
            'ConfirmPass':newpas.get()
            })
        connection.commit()
        connection.close()
        messagebox.showinfo('Success',"New account created successfully")
        clear()





def sign_up():
    def openlogin():
        root.destroy()
        import login
    global firstname,lastname,add,email,pas,newpas           



    header=Label(root,text='Register Now',fg='#3751FE', bg='white',font=('roboto',23,'bold'))
    header.place(x=50,y=50)


    para=Label(root,text='Please input your information on fields.',fg='black', bg='white',font=('roboto',9))
    para.place(x=50,y=100)


    para1=Label(root,text='First name',fg='black', bg='white',font=('roboto',8))
    para1.place(x=50,y=170)
    firstname=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    firstname.place(x=50,y=190,height=25)

    para2=Label(root,text='Last name',fg='black', bg='white',font=('roboto',8))
    para2.place(x=240,y=170)
    lastname=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    lastname.place(x=240,y=190,height=25)

    para3=Label(root,text='Phone Number',fg='black', bg='white',font=('roboto',8))
    para3.place(x=50,y=230)
    add=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    add.place(x=50,y=250,height=25)

    para4=Label(root,text='Email',fg='black', bg='white',font=('roboto',8))
    para4.place(x=240,y=230)
    email=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    email.place(x=240,y=250,height=25)

    para5=Label(root,text='Create Password',fg='black', bg='white',font=('roboto',8))
    para5.place(x=50,y=290)
    pas=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    pas.place(x=50,y=310,height=25)

    para6=Label(root,text='Confirm Password',fg='black', bg='white',font=('roboto',8))
    para6.place(x=240,y=290)
    newpas=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
    newpas.place(x=240,y=310,height=25)


    Button(root,width=10,pady=7,text='Sign up',bg='#3751FE',fg='white',border=0,command=signup).place(x=50,y=350)


    para3=Label(root,text='Already have an account?',fg='black', bg='white',font=('roboto',8))
    para3.place(x=100,y=430)

    Button(root,width=6,pady=7,text='Login',bg='white',fg='#3751FE',font=('roboto',8),border=0,command=openlogin).place(x=232,y=423)
sign_up()


root.mainloop()                  #ui open grna chai variable name.fun name garnu paryo #mainloop()=endless loop of window
