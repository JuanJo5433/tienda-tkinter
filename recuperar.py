from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from subprocess import call
import sqlite3
import sys

class Recuperar:
	db_name = 'bd_proyecto_2560119.db'

	def __init__(self, ventana_recuperar):
		''' -------------- Atributos de la ventana ----------- '''
		self.window = ventana_recuperar
		self.window.title("Recuperar Password")
		self.window.geometry("410x420")
		self.window.iconbitmap("logo.ico")
		self.window.resizable(0,0)

		'''----------Titulo de la ventana ----------'''
		titulo = Label(ventana_recuperar, text="RECUPERAR PASSWORD", fg="black", font=("Comic Sans", 13, "bold"), pady=10).pack()

		'''------------ Logo de Recuperar --------'''
		imagen_login = Image.open("recuperar_password.ico")
		nueva_imagen= imagen_login.resize((60,60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(ventana_recuperar, image=render)
		label_imagen.image = render
		label_imagen.pack(pady=5)


		'''--------- Marco de Recuperar ---------- '''
		marco = LabelFrame(ventana_recuperar, text="Datos de recuperacion del password", font=("Comic Sans", 10, "bold"))
		marco.pack()

		'''--------------------------------- Formulario de recuperar ------------------------------ '''
		label_usuario = Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
		self.usuario = Entry(marco, width=33)
		self.usuario.focus()
		self.usuario.grid(row=0, column=1, padx=5, pady=10)

		#Creamos el label para poner el texto de seleccione una pregunta
		label_nota = Label(marco,text="Seleccione una pregunta y digite la respuesta correcta.", font=("Comic Sans", 9, "bold"),foreground="red").grid(row=1,column=0,columnspan=2,sticky='s',padx=8)

		label_pregunta = Label(marco, text="Pregunta: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s',padx=5,pady=8)
		self.combo_pregunta = ttk.Combobox(marco, values=["Nombre primera mascota", "Nombre colegio", "Ciudad de nacimiento", "Deporte favorito"], width=30, state="readonly")
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=2, column=1, padx=5, pady=8)

		label_respuesta = Label(marco, text="Respuesta: ", font=("Comic Sans", 10, "bold")).grid(row=3,column=0,sticky='s',padx=5,pady=8)
		self.respuesta = Entry(marco,width=33)
		self.respuesta.grid(row=3,column=1,padx=5,pady=8)

		label_password = Label(marco, text="Nuevo Password: ",font=("Comic Sans", 10, "bold")).grid(row=4,column=0,sticky='s',padx=5,pady=8)
		self.nuevo_password=Entry(marco, width=33, show="*")
		self.nuevo_password.grid(row=4, column=1, padx=5, pady=8)
		
		label_password = Label(marco, text="Repetir Password: ",font=("Comic Sans", 10, "bold")).grid(row=5,column=0,sticky='s',padx=10,pady=8)
		self.repetir_password=Entry(marco, width=33, show="*")
		self.repetir_password.grid(row=5, column=1, padx=5, pady=8)


		'''------------------------- Frame de los botones de recuperar password -----------------------'''
		frame_botones = Frame(ventana_recuperar)
		frame_botones.pack()

		'''-------------------------- Botones de Recuperar Password -------------------------------------'''
		boton_recuperar = Button(frame_botones,text="RECUPERAR", command=self.recuperar_password, height=2, width=10, bg="green", fg="white",font=("Comic Sans", 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
		boton_login = Button(frame_botones,text="LOGIN", command=self.llamar_login, height=2,width=10, bg="blue", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, padx=10, pady=10)
		boton_cancelar = Button(frame_botones, text="CANCELAR", command=ventana_recuperar.quit, height=2, width=10, bg="red", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=3, padx=10, pady=10)


	'''--------------------------- Metodos de recuperar -------------------------'''
	def recuperar_password(self):
		#Valida la funciones
		if self.validar_formulario_completo() and self.validar_datos_usuario() and self.validar_password():
			#Permite actualizar la contrasena a partir del usuario
			query = 'UPDATE usuarios SET password = (?) WHERE usuario= (?)'
			parameters = (self.nuevo_password.get(), self.usuario.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("Password Recuperado", f'Password actualizado correctamente')
			self.limpiar_formulario()


	def validar_formulario_completo(self):
		if len(self.usuario.get()) !=0 and len(self.nuevo_password.get()) !=0 and len(self.repetir_password.get()) !=0 and len(self.respuesta.get()) !=0 :
			return True
		else:
			messabox.showerror("Error", "Complete todos los campos del formulario")

	def validar_datos_usuario(self):
		usuario = self.usuario.get()
		respuesta = self.respuesta.get()
		busqueda = self.buscar_usuario(usuario, respuesta)
		if busqueda != []:
			return True
		else:
			messagebox.showerror("Error de recuperacion", "Datos de recuperacion no son correctos")
	
	def validar_password(self):
		if(str(self.nuevo_password.get()) == str(self.repetir_password.get())):
			return True
		else:
			messagebox.showerror("Error de recuperacion", "Password no coinciden")

	def ejecutar_consulta(self, query, parameters=()):
		with  sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query,parameters)
			conexion.commit()
		return result
	
	def limpiar_formulario(self):
		self.usuario.delete(0, END)
		self.respuesta.delete(0, END)
		self.nuevo_password.delete(0, END)
		self.repetir_password.delete(0, END)

	def buscar_usuario(self, usuario, respuesta):
		with  sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql= f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND respuesta = '{respuesta}'"
			cursor.execute(sql)
			busqueda=cursor.fetchall()
			cursor.close()
		return busqueda

	def llamar_login(self):
		ventana_recuperar.destroy()
		call([sys.executable, 'login.py'])

if __name__ == '__main__':
	ventana_recuperar = Tk()
	application = Recuperar(ventana_recuperar)
	ventana_recuperar.mainloop()        