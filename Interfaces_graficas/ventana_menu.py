from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry('500x500+500+200')

def acercade():
    messagebox.showinfo('Software de tarea')

def actualiza():
    messagebox.showwarning('Actualización en camino','''Actualización disponible''')

def salir():
    seleccion = messagebox.askokcancel('Salir','Desea salir de la aplicación?')
    if seleccion==True:
        ventana.destroy()

def cierradoc():
    seleccion=messagebox.askretrycancel('Reintentar','Error en cierre de archivo')
    if seleccion==False:
        ventana.destroy()

barramenu = Menu(ventana)
ventana.config(menu=barramenu,width=600,height=400)
menuarchivo=Menu(barramenu, tearoff=0)
menuarchivo.add_command(label='Nuevo')
menuarchivo.add_command(label='Abrir')
menuarchivo.add_command(label='Guardar')
menuarchivo.add_command(label='Guardar como')
menuarchivo.add_separator()
menuarchivo.add_command(label='Cerrar', command=cierradoc)
menuarchivo.add_command(label='Salir', command=salir)
barramenu.add_cascade(label='Archivo',menu=menuarchivo)
#-----------------------------------

menu_inicio=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label='Inicio',menu=menu_inicio)
menu_inicio.add_command(label='Portapapeles')
menu_inicio.add_command(label='Fuente')
menu_inicio.add_command(label='Párrafo')
menu_inicio.add_command(label='Estilos')
menu_inicio.add_command(label='Edición')
#-----------------------------------

menu_edit = Menu(barramenu, tearoff=0)
menu_edit.add_command(label='Cortar')
menu_edit.add_command(label='Pegar')
menu_edit.add_command(label='Imprimir')
barramenu.add_cascade(label='Edición', menu=menu_edit)
#-----------------------------------


menu_ayuda=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label='Ayuda',menu=menu_ayuda)
menu_ayuda.add_command(label='Soporte')
menu_ayuda.add_command(label='Actualizaciones', command=actualiza)
menu_ayuda.add_command(label='Acerca de',command=acercade)









ventana.mainloop()