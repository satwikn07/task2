from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import simpledialog
import mysql.connector as mysql

phy_m = 0
chem_m = 0
math_m = 0
flag1 = False
flag2 = False
flag3 = False


def cgpa(regd):
    global phy_m, chem_m, math_m
    cgpa_ = 0
    sum = phy_m + chem_m + math_m
    cgpa_ = (sum/300)*10
    MessageBox.showinfo('CGPA', f'CGPA: {cgpa_}')

def grade(regd):
    global phy_m,chem_m,math_m
    grade_ = ''
    sum = phy_m + chem_m + math_m
    per = (sum/300)*100
    if per >= 0.91:
        grade_ = 'O'
    elif per >= 0.81:
        grade_ = 'E'
    elif per >= 0.71:
        grade_ = 'A'
    elif per >= 0.61:
        grade_ = 'B'
    elif per >= 0.51:
        grade_ = 'C'
    elif per >= 0.41:
        grade_ = 'D'
    else:
        grade_ = 'F'
    MessageBox.showinfo('Grade',f'Grade: {grade_}')






def new_ip(window):
    window.destroy()
    flag3 = False
    flag2 = False
    flag1 = False
    phy_m = 0
    chem_m = 0
    math_m = 0
    mainpage()


def close(window):
    flag3 = False
    flag2 = False
    flag1 = False
    phy_m = 0
    chem_m = 0
    math_m = 0
    window.quit()


def calculation(regd):
    cal = Tk()
    cal.geometry("800x500")
    cal.title('Result')

    result_l = Label(cal, text=f'Result', font=('bold', 15))
    result_l.place(x=30, y=5)

    cgpa_b = Button(cal, text="CGPA", font=('italic', 10, 'bold'), bg='blue',
                    command=lambda: cgpa(regd))
    cgpa_b.place(x=150, y=80)

    grade_b = Button(cal, text="Grade", font=('italic', 10, 'bold'), bg='orange',
                    command=lambda: grade(regd))
    grade_b.place(x=150, y=140)

    new_b = Button(cal, text="NEW INPUT", font=('italic', 10, 'bold'), bg='yellow',
                     command=lambda: new_ip(cal))
    new_b.place(x=150, y=200)

    quit_b = Button(cal, text="QUIT", font=('italic', 10, 'bold'), bg='red',
                     command=lambda: close(cal))
    quit_b.place(x=150, y=260)


    cal.mainloop()

def sub_entry(window,regd):
    global flag1,flag2,flag3,phy_m,chem_m,math_m
    flag = False
    if (flag1==True and flag2 == True and flag3 == True):

        try:
            con = mysql.connect(host='localhost', user='root', password='', database='cgpa')
            cursor = con.cursor()
            cursor.execute(f"UPDATE marks SET physics = {phy_m},chemistry={chem_m},math = {math_m} WHERE regd = '{regd}'")
            cursor.execute('commit')

            con.close()

            MessageBox.showinfo('Insertion Status','Inserted Successfully')
            window.destroy()
            calculation(regd)


        except:
            MessageBox.showinfo('Insert Status','Insertion Failed')


def phy():
    global phy_m,flag1
    phy_m = simpledialog.askinteger('input','please enter physics marks')
    flag1 = True
    # print(phy_m)
def chem():
    global chem_m,flag2
    chem_m = simpledialog.askinteger('input','please enter chemistry marks')
    flag2 = True
    # print(chem_m)
def math():
    global math_m,flag3
    math_m = simpledialog.askinteger('input','please enter maths marks')
    flag3 = True
    # print(math_m)



def marks_entry(regd,name,branch):
    m_e = Tk()
    m_e.geometry("800x500")
    m_e.title(f'{name} Marks Entry')

    user_ = Label(m_e, text=f'Enter {name} marks', font=('bold', 15))
    user_.place(x=30, y=5)

    phy_l = Label(m_e, text=f'Physics', font=('bold', 10))
    phy_l.place(x=30, y=80)

    chem_l = Label(m_e, text=f'Chemistry', font=('bold', 10))
    chem_l.place(x=30, y=140)

    math_l = Label(m_e, text=f'Math', font=('bold', 10))
    math_l.place(x=30, y=200)

    phy_b = Button(m_e, text="Enter", font=('italic', 10, 'bold'), bg='red',
                   command=phy)
    phy_b.place(x=150, y=80)

    chem_b = Button(m_e, text="Enter", font=('italic', 10, 'bold'), bg='orange',
                   command=chem)
    chem_b.place(x=150, y=140)

    math_b = Button(m_e, text="Enter", font=('italic', 10, 'bold'), bg='white',
                   command=math)
    math_b.place(x=150, y=200)

    Submit = Button(m_e, text="Submit", font=('italic', 10, 'bold'), bg='green',
                    command=lambda : sub_entry(m_e,regd))
    Submit.place(x=150, y=260)




    m_e.mainloop()



def student(window,e_regd,e_name,e_branch):
    regd = e_regd.get()
    name = e_name.get()
    branch = e_branch.get()
    flag = False

    if(regd == "" or name == "" or branch == ""):
        MessageBox.showinfo('Insertion Status','All fields are required')

    if len(regd) != 10:
        MessageBox.showinfo('Insertion Status', 'Enter Valid registration Number')

    else:
        try:
            con = mysql.connect(host='localhost', user='root', password='', database='cgpa')
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO marks(regd,name,branch) values ('{regd}','{name}','{branch}')")
            cursor.execute('commit')
            con.close()
            flag = True
            if flag == True:
                window.destroy()
                marks_entry(regd,name,branch)

        except:
            MessageBox.showinfo('Insert Status','Insertion Failed')


def mainpage():
    main_ = Tk()
    main_.geometry("700x500")
    main_.title('Student Details')

    user_ = Label(main_, text = f'Welcome ',font=('bold',15))
    user_.place(x = 30,y = 5)

    user_ = Label(main_, text='Enter Student Details', font=('bold', 12))
    user_.place(x=30, y=40)

    Regd = Label(main_, text='Registration No. : ', font=('bold', 12))
    Regd.place(x=120, y=80)

    name = Label(main_, text='Name : ', font=('bold', 12))
    name.place(x=120, y=140)

    branch = Label(main_, text='Branch : ', font=('bold', 12))
    branch.place(x=120, y=200)

    e_Regd = Entry(master=main_)
    e_Regd.place(x=250, y=80)
    e_name = Entry(master=main_)
    e_name.place(x=250, y=140)
    e_branch = Entry(master=main_)
    e_branch.place(x=250, y=200)

    login = Button(main_, text="Submit", font=('italic', 10, 'bold'), bg='green',
                   command= lambda: student(main_,e_Regd,e_name,e_branch))
    login.place(x=250, y=260)




    main_.mainloop()



def signin(window):
    window.destroy()
    s_win = Tk()
    s_win.geometry("600x300")
    s_win.title('Login')
    login_label = Label(s_win, text='LOGIN', font=('bold', 15))
    login_label.place(x = 20)

    username = Label(s_win, text='Enter Username', font=('bold', 10))
    username.place(x=20, y=70)

    password = Label(s_win, text='Enter Password', font=('bold', 10))
    password.place(x=20, y=100)

    e_username1 = Entry(master=s_win)
    e_username1.place(x = 150,y = 70)
    e_password1 = Entry(master=s_win)
    e_password1.place(x = 150,y = 100)


    login = Button(s_win, text="Login", font=('italic', 10, 'bold'), bg='green', command=lambda :login_(s_win,e_username1,e_password1))
    login.place(x=310, y=180)

    s_win.mainloop()

def login_(window,e_username1,e_password1):

    e_user = e_username1.get()
    e_pass_ = e_password1.get()
    try:
        con = mysql.connect(host='localhost', user='root', password='', database='cgpa')
        cursor = con.cursor()
        cursor.execute("SELECT username,password FROM pass")
        login = False
        for (user, password) in cursor:
            if e_user == user and e_pass_ == password:
                login = True
                break
        con.close()
        if not login:
            MessageBox.showinfo('login status','Login Failed\nInavlid Username or Password')
            window.destroy()

        else:
            window.destroy()
            mainpage()

    except :
        pass



def signup_():
    username = e_username.get()
    password = e_password.get()
    email = e_email.get()
    year = e_year.get()
    print(username)

    if(username == "" or password == "" or email == "" or year == ""):
        MessageBox.showinfo('SignUp Status','All fields are required')

    try:

        flag = False
        con = mysql.connect(host='localhost', user='root', password='', database='cgpa')
        cursor = con.cursor()
        cursor.execute("SELECT username FROM pass")

        for user in cursor:
            if user == (username,):
                flag = True
                break
        if flag:
            MessageBox.showinfo('SignUp Status','Username Exists\n Try new one')

        con.close()
    except :
        pass

    if int(year) > 4:
        MessageBox.showinfo('SignUp Status', 'Enter year less than 4')

    if '@' not in email:
        MessageBox.showinfo('SignUp Status', 'Enter Valid Email')

    if len(password) < 8:
        MessageBox.showinfo('SignUp Status', 'Enter password of length grater than 7')

    else:
        try:
            con = mysql.connect(host='localhost',user='root',password='',database = 'cgpa')
            cursor = con.cursor()
            cursor.execute(f"insert into pass values('{username}','{password}','{email}','{year}')")
            cursor.execute('commit')

            e_username.delete(0,'end')
            e_password.delete(0,'end')
            e_email.delete(0,'end')
            e_year.delete(0,'end')
            MessageBox.showinfo('SignUp Status','SignUp Sucessfully')
            con.close()
        except :

            MessageBox.showinfo('SignUp Status','Error Occured while Signing Up')

root = Tk()
root.geometry('600x300')
root.title('Signup')

s_label = Label(root,text = 'SIGN UP',font = ('bold', 15))
s_label.place(x = 20,y=0)

username = Label(root,text = 'Enter Username',font = ('bold', 10))
username.place(x = 20, y = 30)

password = Label(root,text = 'Enter Password',font = ('bold', 10))
password.place(x = 20, y = 60)

email = Label(root,text = 'Enter email',font = ('bold', 10))
email.place(x = 20, y = 90)

year = Label(root,text = 'Enter Year',font = ('bold', 10))
year.place(x = 20, y = 120)

e_username = Entry()
e_username.place(x = 150,y = 30)

e_password = Entry()
e_password.place(x = 150,y = 60)

e_email = Entry()
e_email.place(x = 150,y = 90)

e_year = Entry()
e_year.place(x = 150,y = 120)

signup_ = Button(root, text = "Signup", font = ('italic',10,'bold'),bg = 'green',command = signup_)
signup_.place(x = 180,y = 180)

signin_ = Button(root, text = "Sign In", font = ('italic',10,'bold'),bg = 'green',command = lambda :signin(root))
signin_.place(x = 310,y = 180)



root.mainloop()