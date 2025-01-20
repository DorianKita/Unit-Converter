import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

#labels
label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
label.pack()


window.mainloop()