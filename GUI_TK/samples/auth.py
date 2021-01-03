from tkinter import *


root = Tk()
root.geometry('500x500')
root.title('login/register')



def registration():
    title_reg = Label(text = 'register in system')
    text1_reg = Label(text= 'input login: ')
    login  = Entry()
    text2_reg = Label(text= 'input password: ')
    password  = Entry()
    text3_reg = Label(text = 'try password: ')
    password2 = Entry(show = '*')
    button_register = Button(text = 'Register', command = lambda : save())
    title_reg.pack()
    text1_reg.pack()
    login.pack()
    text2_reg.pack()
    password.pack()
    text3_reg.pack()
    password2.pack()
    button_register.pack()

def authorize():
    title_login = Label(text = 'enter the system')
    text1_login = Label(text= 'enter login: ')
    login  = Entry()
    text2_login = Label(text= 'enter password: ')
    password  = Entry()
    button_login = Button(text = 'Login', command = lambda : save())
    title_login.pack()
    text1_login.pack()
    login.pack()
    text2_login.pack()
    password.pack()
    button_login.pack()

def intro():
    title_intro = Label(text = 'try login to continue ... ', )
    button_register_intro = Button(text = 'Authorization', command = lambda : registration())
    button_login_intro = Button(text = 'Login', command = lambda : authorize())
    title_intro.pack()
    button_login_intro.pack()
    button_register_intro.pack()


def save():
    data = [login.get(), password.get()]
    file = open('database.txt', 'a')
    for line in data:
        file.write(line + '\n')

intro()

root.mainloop()