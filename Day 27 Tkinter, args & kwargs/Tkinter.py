import tkinter
window = tkinter.Tk()
window.title('GUI Program')
window.wm_minsize(300,200)
label = tkinter.Label(text="Sample text inside app", font=("Times New Roman", 20))
label.pack(side="bottom")


window.mainloop()
