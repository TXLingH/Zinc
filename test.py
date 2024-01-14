import tkinter

win = tkinter.Tk()
win.config(background="white")

win.wm_attributes("-transparentcolor", "white")
tkinter.Button(win, text = "Fuck you tkinter", bd=0, bg="#1f1e33").place(
    relx=0.5, rely=0.5, width=100, height=20
    )
win.mainloop()