from tkinter import *

ventana = Tk()

ventana.title('MENU')
ventana.geometry ('500x600')
ventana.resizable (width=False, height=False)

img_menu=PhotoImage(file='comida_128.png')
Label(ventana, image=img_menu).place(x=190, y=5)

label1=Label(ventana, text='Elije tu combo',font=(16)).place(x=190, y=180)

hamburguesa=IntVar()
papas=IntVar()
nuggets=IntVar()
soda=IntVar()
helado=IntVar()

def combo():
    opciones = ''
    if hamburguesa.get()==1:
        opciones +='Hamburguesa\n'
    if papas.get()==1:
        opciones +='Papas\n'
    if nuggets.get()==1:
        opciones +='Nuggets\n'
    if soda.get()==1:
        opciones += 'Soda\n'
    if helado.get()==1:
        opciones +='Helado\n'
    
    label2.config(text='Su orden es:\n'+opciones,font=('Verdana,14'))

Checkbutton(ventana, text='HAMBURGUESA',variable=hamburguesa,onvalue=1,command=combo,font=('Consolas',14)).place(x=10, y=210)

Checkbutton(ventana, text='PAPAS',variable=papas,onvalue=1,command=combo,font=('Consolas',14)).place(x=10, y=240)

Checkbutton(ventana, text='NUGGETS',variable=nuggets,onvalue=1,command=combo,font=('Consolas',14)).place(x=10, y=270)

Checkbutton(ventana, text='SODA',variable=soda,onvalue=1,command=combo,font=('Consolas',14)).place(x=10, y=300)

Checkbutton(ventana, text='HELADO',variable=helado,onvalue=1,command=combo,font=('Consolas',14)).place(x=10,y=330)

label2=Label(ventana)
label2.place(x=130,y=390)  






ventana.mainloop()