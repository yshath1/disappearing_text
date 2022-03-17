from tkinter import *

window = Tk()
window.title("Disappearing Text App")
window.minsize(500, 500)
window.config(padx=100, pady=100)
time = 0


def delete():
    textbox.delete(1.0, END)
    textbox.insert(END, "")


def disappear_text():
    global time, text
    if text == textbox.get(1.0, END):
        if time == 5:
            window.after(1000, delete)
            time = -1
        window.after(1000, disappear_text)
        time += 1
    else:
        window.after(1000, disappear_text)
        text = textbox.get(1.0, END)
        time = 0


text = ""
textbox = Text(height=50, width=100, yscrollcommand=True)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)

window.after(1000, disappear_text)
window.mainloop()
