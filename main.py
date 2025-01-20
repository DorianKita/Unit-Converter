import tkinter

def button_clicked():
    username = input.get()
    label.config(text=username)

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#labels
label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
label.config(text="This is a new label")
label.grid(row= 0, column= 0)

#Button
button = tkinter.Button(text="Click me", command=button_clicked)
new_button = tkinter.Button(text="New Button")
button.grid(row=1, column=1)
new_button.grid(row=0, column=2)

#Entry/input
input = tkinter.Entry(width=10)
input.grid(row=2,column=3)


window.mainloop()