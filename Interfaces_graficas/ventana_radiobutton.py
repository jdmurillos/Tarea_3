from tkinter import *

ventana = Tk()

ventana.geometry('500x400')
label_1=Label(ventana, text='Indique su lenguaje favorito de programación', font=(14))
label_1.place(x=10, y=20)

label2 = Label(ventana, font=(16))
label2.place(x=10, y=150)


def lenguajes():
    if seleccion.get()==1:
        label2.config(text='Seleccionaste Python')
    if seleccion.get()==2:
        label2.config(text='Seleccionaste JavaScript')
    if seleccion.get()==3:
        label2.config(text='Seleccionaste Java')

seleccion=IntVar()
seleccion.set(3)

img=PhotoImage(file=r'A:\Documentos\Universidad\UNAD\4°Semestre\Programacion Avanzada\Unidad 2\Tarea 3\tarea_3\Interfaces_graficas\python.png')
img2=PhotoImage(file=r'A:\Documentos\Universidad\UNAD\4°Semestre\Programacion Avanzada\Unidad 2\Tarea 3\tarea_3\Interfaces_graficas\js.png')
img3=PhotoImage(file=r'A:\Documentos\Universidad\UNAD\4°Semestre\Programacion Avanzada\Unidad 2\Tarea 3\tarea_3\Interfaces_graficas\java.png')


radio1=Radiobutton(ventana, text='Python', variable=seleccion, value=1, command=lenguajes, image=img)
radio1.place(x=10, y=60)

radio2=Radiobutton(ventana, text='JavaScript', variable=seleccion, value=2, command=lenguajes, image=img2)
radio2.place(x=10, y=90)

radio3=Radiobutton(ventana, text='Java', variable=seleccion, value=3, command=lenguajes,image=img3)
radio3.place(x=10, y=120)








ventana.mainloop()