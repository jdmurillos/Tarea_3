from tkinter import *

ventana = Tk()
ventana.geometry('300x400')
etiqueta = Label(ventana, text='Línea de texto',fg='blue', font=('Verdana',18))
etiqueta.place(x=100, y=100)
imagen = PhotoImage(file='im2.png')
Label(ventana, image=imagen).place(x=10, y=0)


ventana.mainloop()