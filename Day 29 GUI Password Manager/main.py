# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import tkinter
from tkinter import messagebox
import json
from PasswordGenerator import generate_password
def gen_password():  # Generates and inserts data in tkinter password entry widget
    password_ip.insert(tkinter.END, str(generate_password()))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():  # Grabs data from entry widgets and saves them in json file
    new_data = {
        website_ip.get(): {
            "Username": user_ip.get(),
            "Password": password_ip.get()
        }
    }
    try:
        with open("passwords.json", 'r') as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
        with open('passwords.json', 'w') as outfile:
            outfile.write("{}")

    with open('passwords.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


    website_ip.delete(0, tkinter.END)
    user_ip.delete(0, tkinter.END)
    password_ip.delete(0, tkinter.END)


# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
def search():
    target = website_ip.get()
    with open("passwords.json", 'r') as file:
        data = json.load(file)
    try:
        username = data[target]["Username"]
        password = data[target]["Password"]
        messagebox.showinfo("Credentials", f"Username: {username}\nPassword: {password}")
    except KeyError:
        messagebox.showwarning("Error", f"Credentials for '{target}' not found")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(350, 300)

# Image
canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Website Label and entry
website_label = tkinter.Label(text='Website')
website_ip = tkinter.Entry(width=35)
website_ip.focus()
website_label.grid(row=1, column=0)
website_ip.grid(row=1, column=1, columnspan=2)

# Search Button
search = tkinter.Button(text='Search', command=search, width=9)
search.grid(row=1, column=2)

# Email label and entry
email_uid_label = tkinter.Label(text='Email/Username')
user_ip = tkinter.Entry(width=35)
user_ip.insert(-1, string='sarvesh@gmail.com')
email_uid_label.grid(row=2, column=0)
user_ip.grid(row=2, column=1, columnspan=2)

# Password label and entry
password_label = tkinter.Label(text='Password')
password_ip = tkinter.Entry(width=24)
password_label.grid(row=3, column=0)
password_ip.grid(row=3, column=1)

# Generate button
generate = tkinter.Button(text='Generate', command=gen_password, width=9)
generate.grid(row=3, column=2)

# Add button (FileWrite Passwords and Uid)
add = tkinter.Button(text='Add', command=add_password, width=35)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
