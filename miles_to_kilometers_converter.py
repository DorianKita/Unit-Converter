from tkinter import *

def calculate():
    converted = round((int(inp.get()) * 1.609344),2)
    result.config(text=converted)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(pady=100, padx=100)

inp = Entry()
inp.config(width=10)
inp.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

result = Label(text=0)
result.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()