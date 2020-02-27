import tkinter as tk

# added only to define required global variable "txt"
class Txt(object):
    def SetValue(data): pass
    def GetValue(): pass
txt = Txt()
####

def load():
    with open(textField.get()) as file:
        txt.SetValue(file.read())

def save():
    with open(textField.get(), 'w') as file:
        file.write(txt.GetValue())

win = tk.Tk()
win.title('Text Editor')
win.geometry('500x500')

# create text field
textField = tk.Entry(win, width=50)
textField.pack(fill=tk.NONE, side=tk.TOP)

# create button to open file
openBtn = tk.Button(win, text='Open', command=load)
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

# create button to save file
saveBtn = tk.Button(win, text='Save', command=save)
saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

win.mainloop()