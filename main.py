import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

#labels
label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
label.pack()

label.config(text="This is a new label")

#Button
def button_clicked():
    username = input.get()
    label.config(text=username)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#Entry/input

input = tkinter.Entry(width=10)
input.pack()



window.mainloop()