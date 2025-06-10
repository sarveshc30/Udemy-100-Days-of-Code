import tkinter
window = tkinter.Tk()
window.title('GUI Program')
window.wm_minsize(400,300)
window.config(padx=20, pady=20)
label = tkinter.Label(text="Sample text inside app", font=("Times New Roman", 20))
label.grid(row=1, column=1)

form = tkinter.Entry()
form.insert('end', string='Enter Your Name')
form.grid(row=2, column=2)

def button_click():
    label.config(text=f"Hello {form.get()}")

button = tkinter.Button(text="Button", command=button_click)
button.grid(row=1, column=3)
window.mainloop()
