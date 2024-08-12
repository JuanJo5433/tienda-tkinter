from tkinter import * 
from PIL import ImageTk, Image
from subprocess import call
from tkinter import messagebox
import sqlite3
import sys

class Login:
	db_name = 'bd_proyecto_2560119.db'

	def __init__(self, ventana_login):

		'''---------------Window attributes----------------'''

		# The window is created.
		self.window = ventana_login 
		# The title is added.
		self.window.title("Ingreso al Sistema") 
		# The size is determined.
		self.window.geometry("330x370") 
		# Insert icon image.
		self.window.iconbitmap("logo.ico") 
		self.window.resizable(0,0) #Manipular eltamaño de la ventana.

		'''----------------Titulo de la ventana---------------------'''

		titulo = Label(ventana_login, text="INICIAR SESION", fg="black", font=("Comic Sans", 14, "bold"),pady=10).pack()# pack: empaquetar

		'''----------------Logo del Login---------------------------'''

		imagen_login = Image.open("login.png") 
		nueva_imagen = imagen_login.resize((40,40))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(ventana_login, image=render)
		label_imagen.image = render
		label_imagen.pack(pady=5)

		'''----------------Marco del Login---------------------------'''

		#Se pide el usuario y la contraseña del cliente.
		marco = LabelFrame(ventana_login, text="Ingrese sus datos", font=("Comic Sans", 10, "bold"))
		marco.pack()


		'''----------------Label del Login---------------------------'''

		label_usuario = Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=10) # La grid
		self.usuario = Entry(marco, width=25) # Permite ingresar informacion y posteriormente procesarla.
		self.usuario.focus() 
		self.usuario.grid(row=0, column=1, padx=5, pady=10)


		label_password = Label(marco, text="password: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=10) # La grid
		self.password = Entry(marco, width=25, show="*") # Permite ingresar informacion y posteriormente procesarla.
		self.password.grid(row=1, column=1, padx=5, pady=10)

		'''---------------Frame Botones del Login--------------------'''
		frame_botones = Frame(ventana_login)
		frame_botones.pack()

		'''------------- Botonoes del Login --------------'''
		boton_ingresar = Button(frame_botones, text="INGRESAR", command=self.login, height=2, width=12, bg="green", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, padx=10, pady=15)
		boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.llamar_registro, height=2, width=12, bg="#04AFCD", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=1, padx=10, pady=15)

		label_olvidar_password = Label(frame_botones, text="Recuperar Password", font=("Comic Sans",10, "bold")).grid(row=1,  column=0, columnspan=2, sticky='s')
		boton_olvidar_password = Button(frame_botones, text="RECUPERAR", command=self.recuperar_password,  height=2, width=12, bg="#9B0303", fg="white", font=("Comic Sans", 10, "bold")).grid(row=2,  column=0, columnspan=2, padx=10, pady=15)
		
	''' ------------ Metodos del Login ---------- '''
	def llamar_registro(self):
		# Se destruye la ventana login
		ventana_login.destroy()
		# Llamar la ventana registro
		call([sys.executable, 'registro.py'])

	def login(self):
		if (self.validar_formulario_completo()):
			usuario = self.usuario.get()
			password = self.password.get()
			dato = self.validar_login(usuario, password)
			if dato != []:
				messagebox.showinfo("Bienvenid@", "Datos ingresados correctamente.")
				self.productos()
			else:
				messagebox.showerror("Error de ingreso", "Usuario o password incorrecto")

	def validar_login(self, usuario, password):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND password = '{password}'"
			cursor.execute(sql)
			validacion = cursor.fetchall()
			cursor.close()
		return validacion

	def validar_formulario_completo(self):
		if len(self.usuario.get())!=0 and len(self.password.get())!=0:
			return True
		else:
			messagebox.showerror("Error de ingreso", "Ingrese el usuario y el password")

	def recuperar_password(self):
		ventana_login.destroy()
		call([sys.executable, 'recuperar.py'])




if __name__ == '__main__':
	ventana_login = Tk()
	application = Login(ventana_login)
	ventana_login.mainloop()

