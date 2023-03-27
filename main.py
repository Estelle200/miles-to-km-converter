from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = Label(text="Miles", font=("Ariel", 18, "bold"))
my_label.grid(row=0, column=2)

my_label = Label(text="is equal to", font=("Ariel", 18, "bold"))
my_label.grid(row=1, column=0)

my_label = Label(text="Km", font=("Ariel", 14, "bold"))
my_label.grid(row=1, column=2)


def calculate():
    new_text = float(input.get())
    km = new_text * 1.609
    ans_label = Label(text=f"{km}", font=("Ariel", 16))
    ans_label.grid(row=1, column=1)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


input = Entry(width=10)
print(input.get())
input.grid(row=0, column=1)

window.mainloop()