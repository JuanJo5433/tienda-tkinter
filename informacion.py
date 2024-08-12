from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 
from subprocess import call
from tkinter import messagebox
import sqlite3
import sys

class Informacion:
	def __init__(self, ventana_informacion):
		''' ------- Atributos de la ventana ------------- '''
		menubar = Menu(ventana_informacion)
		ventana_informacion.title("informacion")
		ventana_informacion.geometry("800x670")
		ventana_informacion.iconbitmap("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/logo.ico")
		ventana_informacion.resizable(0,0)
		ventana_informacion.configure(menu=menubar)

		''' ------- Menu de la ventana -------------'''
		Productos = Menu(menubar, tearoff=0)
		Clientes = Menu(menubar, tearoff=0)
		Ventas = Menu(menubar, tearoff=0)
		Informacion = Menu(menubar, tearoff=0)

		# Agregamos los elementos del menu(opciones) en cascada
		menubar.add_cascade(label="Productos", menu=Productos)
		menubar.add_cascade(label="Clientes", menu=Clientes)
		menubar.add_cascade(label="Ventas", menu=Ventas)
		menubar.add_cascade(label="Ayuda", menu=Informacion)

		# Iconos del menu
		self.img_informacion = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/info.png")
		self.img_registrar = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/registro.png")

		# Acciones del menu

		self.boton_productos = Productos.add_command(label="Acceder", command=self.abrir_productos, image=self.img_registrar, compound=LEFT)
		self.boton_clientes = Clientes.add_command(label="Acceder",command=self.abrir_clientes, image=self.img_registrar, compound=LEFT)

		self.label_informacion = LabelFrame(ventana_informacion)
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0, column=0)
		'''------------ Titulo ----------------'''
		self.label_titulo = Label(self.label_informacion, text="APLICACION DE ESCRITORIO", fg="white", bg="black", font=("Comic Sans", 25, "bold"), padx=137, pady=20)
		self.label_titulo.grid(row=0, column=0)

		''' --------- Logo Imagenes ----------- '''
		# Logo
		imagen_soporte = Image.open("soporte.png")
		nueva_imagen = imagen_soporte.resize((170,170))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.label_informacion, image = render)
		label_imagen.image = render
		label_imagen.grid(row=1, column=0, padx=10, pady=15)

		''' --------- Opciones ---------------'''
		self.label_titulo = Label(self.label_informacion, text="> Codigo de Tienda de VideoJuegos",fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=2, column=0, sticky=W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="> En esta Tienda Encuentras VideoJuegos" ,fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=3, column=0, sticky= W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="> Aprendiz Juan Jose Giraldo Calle" ,fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=4, column=0, sticky= W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="> Creado por Juan Jose Giraldo Calle - Ficha 2560119 Tgo. Adso - 2023" ,fg="black", font=("Comic Sans", 10, "bold"))
		self.label_titulo.grid(row=6, column=0,padx=60)

	def abrir_clientes(self):
		# Se destruye la ventana Informacion
		ventana_informacion.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'clientes.py'])

	def abrir_productos(self):
		# Se destruye la ventana Informacion
		ventana_informacion.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'productos.py'])
	

		

if __name__ == "__main__":
	ventana_informacion = Tk()
	application = Informacion(ventana_informacion)
	ventana_informacion.mainloop()