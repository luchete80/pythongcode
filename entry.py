import tkinter as tk
win = tk.Tk()

var = tk.StringVar()
var_entry = tk.Entry(win,text='var',textvariable=var)
var_entry.grid()

def handle_button(event):
    button_arg = event.widget['text']
    var_entry.insert(0,'end')

button1 = tk.Button(win,text = '1')
button1.bind("<Button-1>", handle_button)
button1.grid()
# similarly I defined all the buttons.


windows()
win.mainloop()