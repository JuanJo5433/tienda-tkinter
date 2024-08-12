from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 
from subprocess import call
from tkinter import messagebox
import sqlite3
import sys

# Atributos: id, codigo, nombre, apellido, telefono, correo electronico

class Clientes:
	db_name = 'bd_proyecto_2560119.db'
	def __init__ (self, ventana_clientes):
		''' ------- Atributos de la ventana ------------- '''
		menubar = Menu(ventana_clientes)
		ventana_clientes.title("Clientes")
		ventana_clientes.geometry("800x670")
		ventana_clientes.iconbitmap("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/logo.ico")
		ventana_clientes.resizable(0,0)
		ventana_clientes.configure(menu=menubar)

		''' ------- Menu de la ventana -------------'''
		Productos = Menu(menubar, tearoff=0)
		Clientes = Menu(menubar, tearoff=0)
		Ventas = Menu(menubar, tearoff=0)
		Informacion = Menu(menubar, tearoff=0)

		menubar.add_cascade(label="Productos", menu=Productos)
		menubar.add_cascade(label="Clientes", menu=Clientes)
		menubar.add_cascade(label="Ventas", menu=Ventas)
		menubar.add_cascade(label="Ayuda", menu=Informacion)
		# Iconos del menu
		self.img_registrar = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/registro.png")
		self.img_buscar = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/buscar.png")
		self.img_informacion = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/info.png")

		# Acciones del menu

		self.boton_productos = Productos.add_command(label="Acceder", command=self.abrir_productos, image=self.img_registrar, compound=LEFT)
		self.boton_registrar = Clientes.add_command(label="Registrar", command=self.widgets_crud, image=self.img_registrar, compound=LEFT)
		self.boton_buscar = Clientes.add_command(label="Buscar", command=self.widgets_buscador, image=self.img_buscar, compound=LEFT)
		self.boton_informacion = Informacion.add_command(label="Informacion del sistema", command=self.abrir_informacion, image=self.img_informacion, compound=LEFT)

		''' --------- Widgets del Menu -------------------'''
		
		# Widget crud
		self.label_titulo_crud = LabelFrame(ventana_clientes)
		self.frame_logos_clientes = LabelFrame(ventana_clientes)
		self.frame_registro = LabelFrame(ventana_clientes, text="Informacion del sistema", font=("Comic Sans", 10, "bold"),pady=5)
		self.frame_botones_registro = LabelFrame(ventana_clientes)
		self.frame_tabla_crud = LabelFrame(ventana_clientes)
		# Widget buscador
		self.label_titulo_buscador = LabelFrame(ventana_clientes)
		self.frame_buscar_cliente = LabelFrame(ventana_clientes, text="Buscar cliente", font=("Comic Sans", 10, "bold"),pady=10)
		self.frame_boton_buscar = LabelFrame(ventana_clientes)
		# Widget informacion
		self.label_informacion = LabelFrame(ventana_clientes)

		# Pantalla inicial
		self.widgets_crud()

	def abrir_productos(self):
		# Se destruye la ventana clientes
		ventana_clientes.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'productos.py'])

	def abrir_informacion(self):
	
		# Se destruye la ventana informacion
		ventana_clientes.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'informacion.py'])

	def widgets_crud(self):
		# Cada que se inicie el sistema se carga el crud
		self.label_titulo_crud.config(bd=0)
		self.label_titulo_crud.grid(row=0, column=0, padx=5,pady=5)

		'''------------- Titulo de la ventana ---------- '''
		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE CLIENTES", fg="black", font=("Comic Sans MS", 13, "bold"),pady=10)
		self.titulo_crud.grid(row=0,column=0)

		'''------------- Frame de los productos --------- '''
		self.frame_logos_clientes.grid(row=1,column=0,padx=5,pady=5)

		'''-------------- Logos de la ventana ------------'''
		gta5 = Image.open("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/gta.png")
		nueva_imagen = gta5.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_clientes, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=0, padx=15, pady=5)
		
		
		'''--------- Marco de la ventana -----------'''
		self.frame_registro.grid(row=2, column=0, padx=50, pady=5)


		'''--------- Formulario de la venetana ----------'''
		label_codigo = Label(self.frame_registro, text="Codigo del cliente", font=("Comic Sans MS", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5, pady=8)
		self.codigo = Entry(self.frame_registro, width=25)
		self.codigo.focus()
		self.codigo.grid(row=0,column=1,padx=5, pady=10)

		label_nombre = Label(self.frame_registro, text="Nombre del cliente", font=("Comic Sans MS", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5, pady=8)
		self.nombre = Entry(self.frame_registro, width=25)
		self.nombre.focus()
		self.nombre.grid(row=1,column=1,padx=5, pady=10)
		
		label_apellido = Label(self.frame_registro, text="Apellido del cliente", font=("Comic Sans MS", 10, "bold")).grid(row=2,column=0,sticky='s',padx=5, pady=8)
		self.apellido = Entry(self.frame_registro, width=25)
		self.apellido.focus()
		self.apellido.grid(row=2,column=1,padx=5, pady=10)

		label_telefono = Label(self.frame_registro, text="Telefono del cliente", font=("Comic Sans MS", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5, pady=8)
		self.telefono = Entry(self.frame_registro, width=25)
		self.telefono.focus()
		self.telefono.grid(row=0,column=3,padx=5, pady=10)

		label_correo_electronico = Label(self.frame_registro, text="Correo electronico del Cliente", font=("Comic Sans MS", 10, "bold")).grid(row=1,column=2,sticky='s',padx=5, pady=8)
		self.correo_electronico = Entry(self.frame_registro, width=25)
		self.correo_electronico.focus()
		self.correo_electronico.grid(row=1,column=3,padx=5, pady=10)

	
		'''-------------Frame de los botonos ---------------------'''
		self.frame_botones_registro.grid(row=3,column=0,padx=5, pady=8)
	 

		'''------------- Botones de la ventana ------------------ '''
		boton_registrar = Button(self.frame_botones_registro, text="REGISTRAR", command=self.agregar_clientes, height=2, width=10, bg="#006CFA", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=0, padx=10)
		# boton_editar = Button(self.frame_botones_registro, text="EDITAR",command=self.editar_cliente, height=2, width=10, bg="#00BF76", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=1, padx=10)
		# boton_eliminar = Button(self.frame_botones_registro, text="ELIMINAR", command=self.eliminar_cliente, height=2, width=10, bg="#C42103", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=2, padx=10)
		# boton_salir = Button(self.frame_botones_registro, text="SALIR", height=2, width=10, bg="black", fg="white",   font=("Comic Sans MS", 9, "bold")).grid(row=0,column=3, padx=10)
	
		boton_editar = Button(self.frame_botones_registro, text="EDITAR", height=2, width=10, bg="#00BF76", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=1, padx=10)
		boton_eliminar = Button(self.frame_botones_registro, text="ELIMINAR",  height=2, width=10, bg="#C42103", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=2, padx=10)
		boton_salir = Button(self.frame_botones_registro, text="SALIR", height=2, width=10, bg="black", fg="white",   font=("Comic Sans MS", 9, "bold")).grid(row=0,column=3, padx=10)

		'''------------- Tabla con la lista de productos ------------------'''
		self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud, height=13,columns=("columna1", "columna2", "columna3", "columna4"))

		self.tree.heading("#0", text="Codigo", anchor=CENTER)
		self.tree.column("#0", width=90, minwidth=75, stretch=False)

		self.tree.heading("columna1", text="Nombre", anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna2", text="Apellido", anchor=CENTER)
		self.tree.column("columna2", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna3", text="Telefono", anchor=CENTER)
		self.tree.column("columna3", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna4", text="Correo Electronico", anchor=CENTER)
		self.tree.column("columna4", width=200, minwidth=100, stretch=False)



		self.tree.grid(row=0, column=0, sticky=E)
		# self.listar_clientes()
		self.widgets_buscador_remove()
		self.label_informacion.grid_remove()
		self.listar_clientes()


	def widgets_buscador(self):
		# Se carga el buscador
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)


		''' ------------ Titulo ------------- '''
		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCADOR DE CLIENTES", fg="black", font=("Comic Sans", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		''' ---------- Frame buscar --------- '''
		self.frame_buscar_cliente.config(bd=2)
		self.frame_buscar_cliente.grid(row=2, column=0, padx=5, pady=5)

		''' --------- Formulario Buscar -------- '''
		self.label_buscar = Label(self.frame_buscar_cliente, text="Buscar Por: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.combo_buscar = ttk.Combobox(self.frame_buscar_cliente, values=["Codigo", "Nombre"], width=22, state="readonly")
		self.combo_buscar.current(0)
		self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

		label_codigo_codigo = Label(self.frame_buscar_cliente, text="Codigo / Nombre", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=5)
		self.codigo_nombre = Entry(self.frame_buscar_cliente, width=25)
		self.codigo_nombre.focus()
		self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

		''' --------- Frame Marco ---------------'''
		self.frame_boton_buscar.config(bd=0)
		self.frame_boton_buscar.grid(row=3, column=0,padx=5, pady=5)
		''' --------- Boton --------------------'''
		self.boton_buscar = Button(self.frame_boton_buscar, text="BUSCAR", command=self.buscar_productos, height=2, width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
		self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

		# Se Carga la tabla pero sin datos
		self.tree.delete(*self.tree.get_children())

		# Remover otros widgets de otros formularios
		self.widgets_crud_remove()
		self.label_informacion.grid_remove()

	def widgets_crud_remove(self):
		# Remove permite que al cambiar de una ventana a otra se limpie(Cargue la nueva ventana solicitada, pasarse de buscar a registro o viceversa)
		# Se limpia el Label y se carga los nuevos
		self.label_titulo_crud.grid_remove() 
		self.frame_registro.grid_remove() 
		self.frame_botones_registro.grid_remove() 

	def widgets_buscador_remove(self):
		self.label_titulo_buscador.grid_remove()
		self.frame_buscar_cliente.grid_remove()
		self.frame_boton_buscar.grid_remove()
	
	def agregar_clientes(self):
		if self.validar_formulario_completo():
			query = 'INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?, ?)'
			parameters = (self.codigo.get(), self.nombre.get(), self.apellido.get(), self.telefono.get(), self.correo_electronico.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("REGISTRO EXITOSO", f'Cliente Registrado: {self.nombre.get()}')
		self.limpiar_formulario()
		self.listar_clientes()

	def validar_formulario_completo(self):
		if len(self.codigo.get()) != 0 and len(self.nombre.get()) != 0 and len(self.apellido.get()) != 0 and len(self.telefono.get()) != 0 and len(self.correo_electronico.get()) !=0:
			return True
		else:
			messagebox.showerror("ERROR", "Complete Todos los Campos del Formulario")
	
	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit()
		return result

	def limpiar_formulario(self):
		self.codigo.delete(0, END)
		self.nombre.delete(0, END)
		self.apellido.delete(0, END)
		self.telefono.delete(0, END)
		self.correo_electronico.delete(0, END)

	def listar_clientes(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = 'SELECT * FROM clientes ORDER BY codigo ASC'
		db_rows = self.ejecutar_consulta(query)
		for row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2], row[3], row[4], row[5]))

if __name__ == "__main__":
	ventana_clientes = Tk()
	application = Clientes(ventana_clientes)
	ventana_clientes.mainloop()