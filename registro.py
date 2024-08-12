from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import sys
import sqlite3 

class Registro:

	db_name = 'bd_proyecto_2560119.db'




	def __init__(self, ventana_registro):
		'''-------------Atributos de la ventana-------'''
		self.window = ventana_registro
		self.window.title("FORMULARIO REGISTRO")
		self.window.geometry("460x630")
		self.window.iconbitmap("logo.ico")
		self.window.resizable(0,0)

		'''-----------------Titulo de la ventana---------------'''
		titulo = Label(ventana_registro, text="REGISTRO DE USUARIO", fg="black", font=("Comic Sans", 14, "bold"),pady=10).pack()

		'''----------------Logo del registro---------------------------'''

		imagen_registro = Image.open("login.png") #
		nueva_imagen = imagen_registro.resize((40,40))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(ventana_registro, image=render)
		label_imagen.image = render
		label_imagen.pack(pady=5)

		'''----------- Ventana del regidtro ------'''
		marco =  LabelFrame(ventana_registro, text="formulario de registro", font=("Comic Sans", 10, "bold"),pady=6, padx=10)
		marco.pack()

		''' ----------- Formulario de registro -------- '''
		label_usuario = Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky="s", padx=5, pady=8)
		self.usuario = Entry(marco, width=20)
		self.usuario.focus()
		self.usuario.grid(row=0, column=1, padx=5, pady=8)

		label_nombre = Label(marco, text="Nombre: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky="s", padx=5, pady=8)
		self.nombre = Entry(marco, width=20)
		self.nombre.grid(row=1, column=1, padx=5, pady=8)

		label_apellido = Label(marco, text="Apellido: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky="s", padx=5, pady=8)
		self.apellido = Entry(marco, width=20)
		self.apellido.grid(row=2, column=1, padx=5, pady=8)


		label_genero = Label(marco, text="Genero: ", font=("Comic Sans", 10, "bold")).grid(row=3, column=0, sticky="s", padx=5, pady=8)
		self.combo_genero = ttk.Combobox(marco, values=["Seleccione su Genero", "Masculino", "Femenino", "No binario"], width=22, state="readonly")
		self.combo_genero.current(0)
		self.combo_genero.grid(row=3, column=1, padx=5, pady=8)

		label_edad = Label(marco, text="Edad: ", font=("Comic Sans", 10, "bold")).grid(row=4, column=0, sticky="s", padx=5, pady=8)
		self.edad = Entry(marco, width=20)
		self.edad.grid(row=4, column=1, padx=5, pady=8)

		label_correo = Label(marco, text="Correo: ", font=("Comic Sans", 10, "bold")).grid(row=5, column=0, sticky="s", padx=5, pady=8)
		self.correo = Entry(marco, width=20)
		self.correo.grid(row=5, column=1, padx=5, pady=8)

		label_password = Label(marco, text="Password: ", font=("Comic Sans", 10, "bold")).grid(row=6, column=0, sticky="s", padx=5, pady=8)
		self.password = Entry(marco, width=20)
		self.password.grid(row=6, column=1, padx=5, pady=8)

		label_confirmacion_password = Label(marco, text="Confirmacion de Password: ", font=("Comic Sans", 10, "bold")).grid(row=7, column=0, sticky="s", padx=5, pady=8)
		self.confirmacion_password = Entry(marco, width=20)
		self.confirmacion_password.grid(row=7, column=1, padx=5, pady=8)

		'''---------Marco Pregunta Registro---------'''
		marco_pregunta = LabelFrame(ventana_registro, text="¿Olvido su password?", font=("Comic Sans", 10, "bold"),pady=8)
		marco_pregunta.pack()

		label_pregunta = Label(marco_pregunta, text="preguntas",font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky="s", padx=5, pady=8)
		self.combo_pregunta = ttk.Combobox(marco_pregunta, values=["Nombre primera mascota", "Nombre colegio", "Ciudad de nacimiento", "Deporte favorito"], width=30, state="readonly")
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=0, column=1, padx=10, pady=8)


		label_respuesta = Label(marco_pregunta, text="Respuesta",font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky="s", padx=5, pady=8)
		self.respuesta = Entry(marco_pregunta, width=33)
		self.respuesta.grid(row=1, column=1, padx=10, pady=8)

		'''--------------Frame de los botones del registro ------------'''
		frame_botones = Frame(ventana_registro)
		frame_botones.pack()

		'''---------Botones de registro -------'''

		boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.registrar_usuario, height=2, width=12, bg="#31D64D", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_limpiar = Button(frame_botones, text="LIMPIAR", command=self.limpiar_formulario, height=2, width=12, bg="#C854D6", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=2, padx=10, pady=15)
		boton_login = Button(frame_botones, text="LOGIN", command=self.llamar_login, height=2, width=12, bg="#3CD6B3", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=3, padx=10, pady=15)
		boton_cancelar = Button(frame_botones, text="CANCELAR", command=ventana_registro.quit, height=2, width=12, bg="#D6461C", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=4, padx=10, pady=15)
		

	'''---------Botones de registro -------'''
	def registrar_usuario(self):
		if self.validar_formulario() and self.validar_password() and self.validar_usuario():
			query = 'INSERT INTO usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
			parameters = (self.usuario.get(), self.nombre.get(), self.apellido.get(), self.combo_genero.get(), self.edad.get(), self.correo.get(), self.password.get(), self.respuesta.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("Registro Exitoso", f"Bienvenid@ {self.nombre.get()} {self.apellido.get()}")

			

		# aura.duque@globant.com		
	def validar_formulario(self):
		if len(self.usuario.get())!=0 and len(self.nombre.get())!=0  and len(self.apellido.get())!=0  and len(self.combo_genero.get())!=0  and len(self.edad.get())!=0  and len(self.correo.get())!=0  and len(self.password.get())!=0 and len(self.confirmacion_password.get())!=0  and len(self.respuesta.get())!=0 :
			return True
		else:
			messagebox.showerror("Error en el registro", "Diligencie todos los campos del formulario")

	def validar_password(self):
		if (str(self.password.get())) == (str(self.confirmacion_password.get())):
			return True
		else:
			messagebox.showerror("Error de registro", "Las contraseñas no coinciden")

	def validar_usuario(self):
		usuario = self.usuario.get()
		dato = self.buscar_usuario(usuario)
		# Si  dato se encuntra vacio, el usuario no existe
		if dato == []:
			return True
		else:
			messagebox.showerror("Error de registro", "El usuario ya se encuentra registrado")

	def limpiar_formulario(self):
		self.usuario.delete(0, END)
		self.nombre.delete(0, END)
		self.apellido.delete(0, END)
		self.combo_genero.delete(0, END)
		self.edad.delete(0, END)
		self.correo.delete(0, END)
		self.password.delete(0, END)
		self.confirmacion_password.delete(0, END)
		self.combo_pregunta.delete(0, END)
		self.respuesta.delete(0, END)

	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit()
		return result


	def buscar_usuario(self, usuario):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = "SELECT * FROM usuarios WHERE usuario = '{}'".format(usuario)
			cursor.execute(sql)
			usuario_consulta = cursor.fetchall()
			cursor.close()
		return usuario_consulta

	def llamar_login(self):
		# se destruye la venta de registro
		ventana_registro.destroy()
		# Se invocael archivo login.py
		call([sys.executable, 'login.py'])




if __name__ == '__main__':	
	ventana_registro = Tk()
	application = Registro(ventana_registro)
	ventana_registro.mainloop()


