#https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python

from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
linea_g=10

filelbl = Label(window, text="Archivo")
filelbl.grid(column=0, row=0)	
textField = Entry(window, width=50)
textField.grid(column=1, row=0)
#textField.pack(fill=NONE, side=TOP)

lbl = Label(window, text="Largo")
lbl.grid(column=0, row=1)
largoField = Entry(window, width=50)
largoField.insert(0, "100.")
largoField.grid(column=1, row=1)
#largoField.pack(fill=NONE, side=TOP)

#********** ARCHIVO *************

# added only to define required global variable "txt"
class Txt(object):
    def SetValue(data): pass
    def GetValue(): pass
txt = Txt()
####

def load():
    with open(textField.get()) as file:
        f= open(file.read(),"w+")
		
def lin2str(l):
    ret=""
    if (l < 100):
        ret="N000"+str(l)
    if (l < 100):
        ret="N00"+str(l)
    if (l < 1000):
        ret="N0"+str(l)
    else:
        ret="N"+str(l)
    l=l+5
    return ret

# Muy bueno para devolver variables
# https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
def save(lin):
    lin=10
    largo=float(largoField.get())
    paso=4.0
    ancho=12.0
    npasadas=10
    npasos=int(largo/paso)
    print("Pasos: %d" %npasos)
    #with open(textField.get(), 'w') as file:
	#with open(textField.get(), 'w') as file:
    f= open("test.txt","w+")
	#file.write(txt.GetValue())
    f.write(lin2str(lin)+" G21\n")
    lin=lin+10
    #lin=linea() #No puedo meter la funcion 
    f.write(lin2str(lin)+" G40 G90\n")
    lin=lin+10
    f.write(lin2str(lin)+" T02 M06 G43 H2\n")
    x=0.
    for p in range(npasadas):
        f.write(lin2str(lin)+" M11P13 \n")
        for i in range(npasos):
            y=-ancho/2.
            f.write(lin2str(lin)+" Y%.2f \n" % (y))
            lin=lin+10
            x=x+paso/2.
            f.write(lin2str(lin)+" X%.2f \n" % (x))
            lin=lin+10
            y=ancho/2.
            f.write(lin2str(lin)+" Y%.2f \n" % (y))
            lin=lin+10
            x=x+paso/2.
            f.write(lin2str(lin)+" X%.2f \n" % (x))	
            lin=lin+10
			# create text field
        f.write(lin2str(lin)+"( ******************* FIN DE PASADA ***********************)\n")
        lin=lin+10
        f.write(lin2str(lin)+" M10P13 \n")
        lin=lin+10
        f.write(lin2str(lin)+" G4 P60000\n")
        lin=lin+10
    f.close()

		
#Generar!
#Ver si el archivo esta abierto

# v0=IntVar()
# v0.set(1)
# r1=Radiobutton(window, text="male", variable=v0,value=1)
# r2=Radiobutton(window, text="female", variable=v0,value=2)
# r1.place(x=100,y=50)
# r2.place(x=180, y=50)


                
# v1 = IntVar()
# v2 = IntVar()
# C1 = Checkbutton(window, text = "Cricket", variable = v1)
# C2 = Checkbutton(window, text = "Tennis", variable = v2)
# C1.place(x=100, y=100)
# C2.place(x=180, y=100)

b = Button(window, text="Generar", width=10, command=save(linea_g))
b.grid(column=1, row=10)
#b.pack()

window.title('Generador Codigo G')
window.geometry("400x300+10+10")
window.mainloop()