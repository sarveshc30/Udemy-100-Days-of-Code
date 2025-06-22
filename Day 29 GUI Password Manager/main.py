# ---------------------------- PASSWORD GENERATOR ------------------------------- #

from PasswordGenerator import generate_password
def add_password():
    password_ip.insert(-1, generate_password())
# ---------------------------- SAVE PASSWORD ------------------------------- #

with open("passwords.txt", 'a'):
    pass

# ---------------------------- UI SETUP ------------------------------- #

import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(350, 300)

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text='Website')
website_ip = tkinter.Entry(width=35)
website_ip.focus()
website_label.grid(row=1, column=0)
website_ip.grid(row=1, column=1, columnspan=2)

email_uid_label = tkinter.Label(text='Email/Username')
user_ip = tkinter.Entry(width=35)
user_ip.insert(-1, string='sarvesh@gmail.com')
email_uid_label.grid(row=2, column=0)
user_ip.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text='Password')
password_ip = tkinter.Entry(width=21)
password_label.grid(row=3, column=0)
password_ip.grid(row=3, column=1)

generate = tkinter.Button(text='Generate', command=add_password, width=10)
generate.grid(row=3, column=2)

add = tkinter.Button(text='Add', command=) # FileWrite Passwords and Uid
generate.grid(row=3, column=1, columnspan=3)


window.mainloop()
