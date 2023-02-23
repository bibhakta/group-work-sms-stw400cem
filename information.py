#import modules
import sqlite3
from tkinter import *
from tkinter import messagebox

#create a window
window=Tk()
window.geometry("1280x720")
window.title("Student Details")
window.configure(bg='white')






std=PhotoImage(file='img/information.png') 
Label(window,image=std,bg='white').place(x=202,y=10) 

photo2=PhotoImage(file='img/dashh.png')
background = Label(window, image=photo2).place(x=0, y=0) #since tkinter doesn't support background image, we place it as a label
def home():
    ho=messagebox.askyesno('message','Insert student data?')
    if (ho):
        window.destroy()
        import sms
image5=PhotoImage(file='img/ho.png') #adding img
Label(window,image=image5,bg='#5e17eb').place(x=10,y=150) #placing img
Label.image= image5 #Image was not showing so internal image varialble to object
Button(window,width=10,pady=7,text='Dashboard',bg='#5e17eb',fg='white',font=('roboto',12),border=0,command=home).place(x=50,y=155) 


def exits():
    q=messagebox.askyesno('Exit','Do you really want to exit ?')
    if (q):
        window.destroy()
image7=PhotoImage(file='img/exit1.png') #adding img
Label(window,image=image7,bg='#5e17eb').place(x=10,y=290) #placing img
Label.image= image7 #Image was not showing so internal image varialble to object
Button(window,width=5,pady=7,text='Exit',bg='#5e17eb',fg='white',font=('roboto',12),border=0,command=exits).place(x=47,y=292) 





def student():
    ab=messagebox.showinfo('Message','You are already in app')
image6=PhotoImage(file='img/students.png') #adding img
Label(window,image=image6,bg='#5e17eb').place(x=10,y=200) #placing img
Label.image= image6 #Image was not showing so internal image varialble to object
Button(window,width=10,pady=7,text='Students',bg='#5e17eb',fg='white',font=('roboto',12),border=0,command=student).place(x=42,y=202) 


def acct():
    abb=messagebox.askyesno('Account','view student data?')
    if (abb):
        import information
image8=PhotoImage(file='img/account.png') #adding img
Label(window,image=image8,bg='#5e17eb').place(x=10,y=245) #placing img
Label.image= image8 #Image was not showing so internal image varialble to object
Button(window,width=6,pady=7,text='Account',bg='#5e17eb',fg='white',font=('roboto',12),border=0,command=acct).place(x=60,y=247) 
#value of y for search function
space=203

#search function
def srch():
    #get data from dropdown menu and entry
    Frame(window,height=600,width=20,bg='white').place(x=202,y=203)
    term=clicked.get()
    detail=search.get()

    #database connection
    conn=sqlite3.connect('students_data.db')
    c=conn.cursor()
    c.execute("SELECT oid,* from students")
    det=c.fetchall()

    #Searching algorithm
    i=len(det)-1
    while i>=0:
        #searching for Student id
        if term=="Student ID":
            try:
                #comparing values
                int(detail)
                if det[i][0]!=int(detail):
                    i=i-1
                    if i==-1:
                        break
                else:
                    Label(window,text="-->",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=200,y=(space+20*i))
                    break
            except:
                messagebox.showerror("Search","Invalid student ID")
                break
        #searching by first name
        elif term=="First Name":
            if det[i][1]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="-->",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=200,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by last name
        elif term=="Last Name":
            if det[i][2]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="-->",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=200,y=(space+20*i))
                i=i-1
                if i==-1:
                    break
        #searching by mobile
        elif term=="Mobile":
            if det[i][5]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="-->",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=200,y=(space+20*i))
                break
        #searching by email
        elif term=="Email":
            if det[i][6]!=detail:
                i=i-1
                if i==-1:
                    break
            else:
                Label(window,text="-->",bg='white',font=('Agency FB',13,'bold'),fg='red').place(x=200,y=(space+20*i))
                break
        else:
            pass
    conn.commit()
    conn.close()    


Frame(window,bg='white',width=1100,height=320).place(x=220,y=190)

#label, dropdown menu for searching
Label(window,text='Search',bg='white',font=('roboto',12)).place(x=210,y=100)
clicked=StringVar()
clicked.set("Student ID")
drop=OptionMenu(window,clicked,"Student ID","First Name","Last Name","Mobile","Email")
drop.place(x=290,y=100)
drop.config(width=15,border=0,background='white')

#entry for searching
search=Entry(window,border=0,highlightthickness=3)
search.place(x=290,y=140,height=28,width=145)
Button(window, text="Search",font=('Arial',8,'bold'),fg='white',bg="purple",width=8,height=1,border=0,cursor='hand2',command=srch).place(x=440,y=100)

#table
def tbl():
    table=Frame(window,height=580,width=950,bg='white',border=0)
    table.place(x=220,y=190)

    try:
        #try fetching data from database
        conn=sqlite3.connect('students_data.db')
        c=conn.cursor()
        c.execute("SELECT oid, firstname, lastname, gender, dob, mob, email, address, course, hobby, ffullname, fmobile, mfullname, mmobile from students")
        lst=c.fetchall()
        conn.commit()
        conn.close()
    except:
        #empty list if list doesn't exist
        lst=[]
    finally:
        #Table headings
        lst.insert(0,('ID','First Name','Last Name','Gender','Dob','Mobile','Email','Address','course','hobby','ffullname','fmobile','mfullname','mmobile'))

    #creating a table
    total_rows =len(lst)
    total_columns=len(lst[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=('roboto',10,'bold')
            jus=CENTER
            bgc ='white'
        else:
            #table data
            fontt=('Arial',10)
            jus=LEFT
            bgc='yellow'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=3
            elif j==1 or j==2:
                wid=10
            elif j==3:
                wid=7
            elif j==4:
                wid=7
            elif j==5:
                wid=10
            elif j==6:
                wid=13
            elif j==7:
                wid=9
            elif j==8:
                wid=10
            elif j==9:
                wid=9
            elif j==10:
                wid=15
            elif j==11:
                wid=11
            elif j==12:
                wid=15
            elif j==13:
                wid=11
            else:
                wid=8
            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
            e.config(state=DISABLED)

#calling table function
tbl()

window.mainloop()