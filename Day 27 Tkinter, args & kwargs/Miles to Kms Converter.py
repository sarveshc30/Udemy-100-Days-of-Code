import tkinter

window = tkinter.Tk()
window.title('Miles To Kilometers')
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text='Miles')
label.grid(row=1, column=0)

label1 = tkinter.Label(text='Kilometers')
label1.grid(row=1, column=2)

label2 = tkinter.Label(text='          ')
label2.grid(row=2, column=2)

enter = tkinter.Entry(width=17)
enter.insert('end', string='Enter no of Miles')
enter.grid(row=2, column=0)

def convert():
    label2.config(text=f'{int(enter.get())*1.6} Kilometers')

button = tkinter.Button(text='Convert', command=convert)
button.grid(row=2, column=1)

window.mainloop()