import main.main as mn
import tkinter as tk
from tkinter import filedialog, Text, ttk

files = []

# Abrir archivos 
def open_file():

    for widget in frame.winfo_children():
        widget.destroy()

    file = filedialog.askopenfile(initialdir="/", title="Abrir Archivo", 
                           filetypes=(("Blocs de Notas", "*.txt"), ("Todos los archivos", "*")))

    if file != None:
        files.append(file)

    for archivo in files:
        label = tk.Label(frame, text=archivo.name, bg="gray")
        label.pack()


# Base
def base(crypt):
    """
    Básicamente sirve a modo de contenedor para no tener
    que repetir el código que usaré para crear las nuevas ventanas.
    
    Y meter un texto útil.
    """

    def destroy():
        global contra
        nonlocal coso

        contra = entry.get()
        coso.destroy()


    # VENTANA
    coso = tk.Tk()
    coso.title("Contraseña")
    coso.resizable(False, False)

    # Texto
    presen = tk.Label(coso, text=f"\n\nPor favor introduzca una contraseña de {crypt}.\nEsta deberá conservarla a fin de poder desencriptar\nlos documentos que desee. También puede compartirla :D.\n\n")
    presen.pack(side=tk.TOP)

    # Entrada
    entry = ttk.Entry(coso)
    entry.insert(0, "Contraseña123")
    entry.pack(side=tk.TOP)

    # Un puto espacio
    espacio = tk.Label(coso, text="\n\n")
    espacio.pack(side=tk.TOP)

    # Botón de salida
    button = tk.Button(coso, text=crypt, command=destroy)
    button.pack(side=tk.BOTTOM)

    # Otro puto espacio (QUE VA ABAJO DE SALIDA)
    espacio2 = tk.Label(coso, text="\n")
    espacio.pack(side=tk.BOTTOM)

    coso.mainloop()


# Encriptar Archivos
def Encrypt_All():
    """
    Esto encripta todo. (con todo y botón)
    """
    base("Encriptar")

    # Bucle para desencriptar todo
    for archivo in files:
        mn.encriptar(archivo.name, archivo.name, contra)


# Desencriptar Archivos
def Dencrypt_All():
    """
    Esto desencripta todo. (con todo y botón)
    """
    base("Desencriptar")

    # Bucle pa desencriptar
    for archivo in files:
        mn.desencriptar(archivo.name, archivo.name, contra)



root = tk.Tk() # Crear Ventana
root.title("Encriptador")
root.resizable(False, False)


# El fondo
canvas = tk.Canvas(root, height=400, width=385, bg="#f9ca24") 
canvas.pack()

# El cuadrito de en medio
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


# Abrir Archivo
open_file = tk.Button(root, text="Seleccionar Archivos", padx=10, 
                      pady=5, fg="white", bg="#22a6b3", command=open_file) 
open_file.pack(side=tk.LEFT)


# Encriptar
encrypt_file = tk.Button(root, text="Encriptar Archivos", padx=10,
                         pady=5, fg="white", bg="#30336b", command=Encrypt_All)
encrypt_file.pack(side=tk.LEFT)


# DesEncriptar
dencrypt_file = tk.Button(root, text="Desencriptar Archivos", padx=10,
                          pady=5, fg="white", bg="#30336b", command=Dencrypt_All)
dencrypt_file.pack(side=tk.LEFT)



root.mainloop() # Mainloop
