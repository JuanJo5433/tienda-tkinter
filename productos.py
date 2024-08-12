from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 
from tkinter import messagebox
from subprocess import call
import sqlite3
import sys

class Productos:
	db_name = 'bd_proyecto_2560119.db'

	def __init__(self, ventana_productos):

		''' ------- Atributos de la ventana ------------- '''
		menubar = Menu(ventana_productos)
		ventana_productos.title("Productos")
		ventana_productos.geometry("800x670")
		ventana_productos.iconbitmap("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/logo.ico")
		ventana_productos.resizable(0,0)
		ventana_productos.configure(menu=menubar)

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
		self.img_registrar = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/registro.png")
		self.img_buscar = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/buscar.png")
		self.img_informacion = PhotoImage(file="C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/info.png")

		# Acciones del menu
		self.boton_clientes = Clientes.add_command(label="Acceder", command=self.abrir_clientes, image=self.img_registrar, compound=LEFT)
		self.boton_registrar = Productos.add_command(label="Registrar", command=self.widgets_crud, image=self.img_registrar, compound=LEFT)
		self.boton_buscar = Productos.add_command(label="Buscar", command=self.widgets_buscador, image=self.img_buscar, compound=LEFT)
		self.boton_informacion = Informacion.add_command(label="Informacion del sistema", command=self.abrir_informacion, image=self.img_informacion, compound=LEFT)
		''' --------- Widgets del Menu -------------------'''
		# Widget crud
		self.label_titulo_crud = LabelFrame(ventana_productos)
		self.frame_logos_productos = LabelFrame(ventana_productos)
		self.frame_registro = LabelFrame(ventana_productos, text="Informacion del sistema", font=("Comic Sans", 10, "bold"),pady=5)
		self.frame_botones_registro = LabelFrame(ventana_productos)
		self.frame_tabla_crud = LabelFrame(ventana_productos)
		# Widget buscador
		self.label_titulo_buscador = LabelFrame(ventana_productos)
		self.frame_buscar_producto = LabelFrame(ventana_productos, text="Buscar producto", font=("Comic Sans", 10, "bold"),pady=10)
		self.frame_boton_buscar = LabelFrame(ventana_productos)
		# Widget informacion
		self.label_informacion = LabelFrame(ventana_productos)

		# Pantalla inicial
		self.widgets_crud()

	def abrir_informacion(self):
	
		# Se destruye la ventana informacion
		ventana_productos.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'informacion.py'])

	def abrir_clientes(self):
	
		# Se destruye la ventana Productos
		ventana_productos.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'clientes.py'])

	def widgets_crud(self):
		# Cada que se inicie el sistema se carga el crud
		self.label_titulo_crud.config(bd=0)
		self.label_titulo_crud.grid(row=0, column=0, padx=5,pady=5)

		'''------------- Titulo de la ventana ---------- '''
		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE PRODUCTOS", fg="black", font=("Comic Sans MS", 13, "bold"),pady=10)
		self.titulo_crud.grid(row=0,column=0)

		'''------------- Frame de los productos --------- '''
		self.frame_logos_productos.grid(row=1,column=0,padx=5,pady=5)

		'''-------------- Logos de la ventana ------------'''
		gta5 = Image.open("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/gta.png")
		nueva_imagen = gta5.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=0, padx=15, pady=5)
		
		gow = Image.open("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/gow.png")
		nueva_imagen = gow.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=1, padx=15, pady=5)

		cod = Image.open("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/cod.png")
		nueva_imagen = cod.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=2, padx=15, pady=5)

		mk = Image.open("C:/Users/juanj/OneDrive/Escritorio/tkinter/Tienda2/mk.png")
		nueva_imagen = mk.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=3, padx=15, pady=5)

		'''--------- Marco de la ventana -----------'''
		self.frame_registro.grid(row=2, column=0, padx=50, pady=5)


		'''--------- Formulario de la venetana ----------'''
		label_codigo = Label(self.frame_registro, text="Codigo del producto", font=("Comic Sans MS", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5, pady=8)
		self.codigo = Entry(self.frame_registro, width=25)
		self.codigo.focus()
		self.codigo.grid(row=0,column=1,padx=5, pady=10)

		label_nombre = Label(self.frame_registro, text="Nombre del producto", font=("Comic Sans MS", 10, "bold")).grid(row=1,column=0,sticky='s',padx=5, pady=8)
		self.nombre = Entry(self.frame_registro, width=25)
		self.nombre.focus()
		self.nombre.grid(row=1,column=1,padx=5, pady=10)

		label_categoria = Label(self.frame_registro, text="Categoria del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2,column=0,sticky='s',padx=5, pady=8)
		self.combo_categoria = ttk.Combobox(self.frame_registro, values=["PlayStation", "Xbox", "Nintendo", "Pc"], width=22, state="readonly")
		self.combo_categoria.current(0)
		self.combo_categoria.grid(row=2,column=1,padx=5, pady=10)

		label_descripcion = Label(self.frame_registro, text="Descripcion del producto", font=("Comic Sans MS", 10, "bold")).grid(row=0,column=2,sticky='s',padx=5, pady=8)
		self.descripcion = Entry(self.frame_registro, width=25)
		self.descripcion.focus()
		self.descripcion.grid(row=0,column=3,padx=5, pady=10)

		label_precio = Label(self.frame_registro, text="Precio del producto", font=("Comic Sans MS", 10, "bold")).grid(row=1,column=2,sticky='s',padx=5, pady=8)
		self.precio = Entry(self.frame_registro, width=25)
		self.precio.focus()
		self.precio.grid(row=1,column=3,padx=5, pady=10)

		label_cantidad = Label(self.frame_registro, text="Cantidad del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2,column=2,sticky='s',padx=5, pady=8)
		self.cantidad = Entry(self.frame_registro, width=25)
		self.cantidad.focus()
		self.cantidad.grid(row=2,column=3,padx=5, pady=10)

		'''-------------Frame de los botonos ---------------------'''
		self.frame_botones_registro.grid(row=3,column=0,padx=5, pady=8)
	 

		'''------------- Botones de la ventana ------------------ '''
		boton_registrar = Button(self.frame_botones_registro, text="REGISTRAR", command=self.agregar_productos, height=2, width=10, bg="#006CFA", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=0, padx=10)
		boton_editar = Button(self.frame_botones_registro, text="EDITAR",command=self.editar_producto, height=2, width=10, bg="#00BF76", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=1, padx=10)
		boton_eliminar = Button(self.frame_botones_registro, text="ELIMINAR", command=self.eliminar_producto, height=2, width=10, bg="#C42103", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0,column=2, padx=10)
		boton_salir = Button(self.frame_botones_registro, text="SALIR", height=2, width=10, bg="black", fg="white",   font=("Comic Sans MS", 9, "bold")).grid(row=0,column=3, padx=10)

		'''------------- Tabla con la lista de productos ------------------'''
		self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud, height=13,columns=("columna1", "columna2", "columna3", "columna4", "columna5"))

		self.tree.heading("#0", text="Codigo", anchor=CENTER)
		self.tree.column("#0", width=90, minwidth=75, stretch=False)

		self.tree.heading("columna1", text="Nombre", anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna2", text="Categoria", anchor=CENTER)
		self.tree.column("columna2", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna3", text="Cantidad", anchor=CENTER)
		self.tree.column("columna3", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna4", text="Precio", anchor=CENTER)
		self.tree.column("columna4", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna5", text="Descripcion", anchor=CENTER)
		self.tree.column("columna5", width=150, minwidth=75, stretch=False)

		self.tree.grid(row=0, column=0, sticky=E)
		self.listar_productos()
		self.widgets_buscador_remove()
		self.label_informacion.grid_remove()


	def widgets_buscador(self):
		# Se carga el buscador
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)


		''' ------------ Titulo ------------- '''
		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCADOR DE PRODUCTOS", fg="black", font=("Comic Sans", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		''' ---------- Frame buscar --------- '''
		self.frame_buscar_producto.config(bd=2)
		self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

		''' --------- Formulario Buscar -------- '''
		self.label_buscar = Label(self.frame_buscar_producto, text="Buscar Por: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.combo_buscar = ttk.Combobox(self.frame_buscar_producto, values=["Codigo", "Nombre"], width=22, state="readonly")
		self.combo_buscar.current(0)
		self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

		label_codigo_codigo = Label(self.frame_buscar_producto, text="Codigo / Nombre del Producto", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=5)
		self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
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
		self.frame_buscar_producto.grid_remove()
		self.frame_boton_buscar.grid_remove()



	def agregar_productos(self):
		if self.validar_formulario_completo():
			query = 'INSERT INTO productos VALUES(NULL, ?, ?, ?, ?, ?, ?)'
			parameters = (self.codigo.get(), self.nombre.get(), self.combo_categoria.get(), self.cantidad.get(), self.precio.get(), self.descripcion.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("REGISTRO EXITOSO", f'Producto Registrado: {self.nombre.get()}')
		self.limpiar_formulario()
		self.listar_productos()

	def validar_formulario_completo(self):
		if len(self.codigo.get()) != 0 and len(self.nombre.get()) != 0 and len(self.combo_categoria.get()) != 0 and len(self.cantidad.get()) != 0 and len(self.precio.get()) !=0 and len(self.descripcion.get()) !=0:
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
		self.cantidad.delete(0, END)
		self.precio.delete(0, END)
		self.descripcion.delete(0, END)

	def listar_productos(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = 'SELECT * FROM productos ORDER BY nombre DESC'
		db_rows = self.ejecutar_consulta(query)
		for row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))
	
	def eliminar_producto(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un producto de la tabla")
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM productos WHERE codigo = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Estas seguro que deseas eliminar el producto: {nombre}?")
		if respuesta == 'yes':
			self.ejecutar_consulta(query, (dato,))
			self.label_productos()
			messagebox.showinfo('EXITO', f'Producto Eliminado: {nombre}')
		else:
			messagebox.showerror('ERROR', f'Error al eliminar eliminar el producto: {nombre}')


	def editar_producto(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un producto de la tabla")
		codigo = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		categoria = self.tree.item(self.tree.selection())['values'][1]
		cantidad = self.tree.item(self.tree.selection())['values'][2]
		precio = self.tree.item(self.tree.selection())['values'][3]
		descripcion = self.tree.item(self.tree.selection())['values'][4]

		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR PRODUCTO")
		# Incluir un icono a la ventana
		self.ventana_editar.iconbitmap("editar.ico")
		self.ventana_editar.resizable(0,0)

		label_codigo = Label(self.ventana_editar, text="Codigo del producto:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s',padx=5, pady=8)
		nuevo_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo),width=25)
		nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)

		label_categoria = Label(self.ventana_editar, text="Categoria:", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_combo_categoria = ttk.Combobox(self.ventana_editar, values=["PlayStation", "Xbox", "Nintendo", "Pc"], width=22, state="readonly")
		nuevo_combo_categoria.set(categoria)
		nuevo_combo_categoria.grid(row=0, column=3, padx=5, pady=0)

		label_nombre = Label(self.ventana_editar, text="Nombre del producto:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_nombre = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre), width=25)
		nuevo_nombre.grid(row=1, column=1, padx=5, pady=0)

		label_descripcion = Label(self.ventana_editar,text="Descripcion:", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nueva_descripcion = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=descripcion), width=25)
		nueva_descripcion.grid(row=1, column=3, padx=5, pady=0)

		label_cantidad = Label(self.ventana_editar, text="Cantidad:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nueva_cantidad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=cantidad), width=25)
		nueva_cantidad.grid(row=2, column=1, padx=5, pady=0)

		label_precio = Label(self.ventana_editar, text="Precio:", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_precio = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=precio), width=25)
		nuevo_precio.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar= Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo.get(), nuevo_nombre.get(), nuevo_combo_categoria.get(), nueva_cantidad.get(), nuevo_precio.get(), nueva_descripcion.get(), codigo), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop()

	def actualizar(self, nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, nueva_descripcion, codigo):
		query = 'UPDATE productos SET codigo = ?, nombre = ?, categoria = ?, cantidad = ?, precio = ?, descripcion = ? WHERE codigo = ?'
		parameters = (nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, nueva_descripcion, codigo)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO', f'Producto Actualizado: {nuevo_nombre}')
		self.ventana_editar.destroy()
		self.listar_productos()

	def buscar_productos(self):
		if(self.validar_busqueda()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			if (self.combo_buscar.get() == 'Codigo'):
				#sentencia SQL LIKE-> inicie por una letra o varias o completas
				query = ("SELECT * FROM productos WHERE codigo LIKE ? ") 
				#% permite realizar la busqueda sin tener completa del codigo a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = (self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))
				
				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				
				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Producto no encontrado")
			else:
				#sentencia SQL LIKE-> inicie por
				query = ("SELECT * FROM productos WHERE nombre LIKE ? ")
				#% permite realizar la busqueda sin tener completa del nombre a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = ("%"+self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))
				
				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				
				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Producto no encontrado")

	def validar_busqueda(self):
		if len(self.codigo_nombre.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR", "Complete todos los campos para la busqueda")


if __name__ == "__main__":
	ventana_productos = Tk()
	application = Productos(ventana_productos)
	ventana_productos.mainloop()