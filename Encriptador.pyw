from tkinter import filedialog, ttk
import funcs
import tkinter as tk

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

def base(func):
    """
    Un decorador para tener la interfaz de las ventanas emergentes.
    """
    def wrapper(*args, **kwargs):
        def destroy():
            pwd = entry.get()
            func(pwd)
            root.destroy()

        
        # Ventana
        root = tk.Tk()
        root.title("Encriptar / Desencriptar")
        root.resizable(False, False)

        # Texto
        texto = tk.Label(root, text="Por favor introduzca una contraseña.\nEsta deberá conservarla a fin de encriptar\no desencriptar los diferentes\narchivos y conservarlos ;).\n\n")
        texto.pack(side=tk.TOP)

        # Entrada
        entry = ttk.Entry(root)
        entry.insert(0, "Contraseña123")
        entry.pack(side=tk.TOP)

        # Un puto espacio
        espacio = tk.Label(root, text="\n\n")
        espacio.pack(side=tk.TOP)

        # Botón de salida
        button = tk.Button(root, text="Aceptar", command=destroy)
        button.pack(side=tk.TOP)

        # Otro puto espacio
        espacio.pack(side=tk.BOTTOM)

        root.mainloop()

    return wrapper

# ENCRIPTAR =====================================================================
@base
def encrypt_all(pwd):
    for file in files:
        funcs.encrypt(file.name, pwd)

@base
def dencrypt_all(pwd):
    for file in files:
        funcs.dencrypt(file.name, pwd)

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
                         pady=5, fg="white", bg="#30336b", command=encrypt_all)
encrypt_file.pack(side=tk.LEFT)


# DesEncriptar
dencrypt_file = tk.Button(root, text="Desencriptar Archivos", padx=10,
                          pady=5, fg="white", bg="#30336b", command=dencrypt_all)
dencrypt_file.pack(side=tk.LEFT)


root.mainloop() # Mainloop
