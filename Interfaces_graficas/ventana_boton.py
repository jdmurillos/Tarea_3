from tkinter import *
import sys

ventana = Tk()

ventana.geometry('500x500')
label_mensaje=Label(ventana, text='¿Desea mostrar saludo?',font=(18))
label_mensaje.place(x=10,y=20)

def saludo():
    label_mensaje.config(text='Hola a Todos')

boton_aceptar=Button(ventana, text='ACEPTAR', bg='green', command=saludo)
boton_aceptar.config(width=10,height=3)
boton_aceptar.place(x=10,y=70)

def cancelar():
    sys.exit()

boton_cancelar = Button(ventana, text='CANCELAR', bg='red',  command=cancelar)
boton_cancelar.config(width=10,height=3)
boton_cancelar.place(x=110,y=70)


ventana.mainloop()