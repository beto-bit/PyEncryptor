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
        # Ventana
        root = tk.Tk()
        root.title("Encriptar / Desencriptar")
        root.resizable(False, False)

        # Texto
        texto = tk.Label(root, text="Por favor introduzca una contraseña. \
            Esta deberá conservarla a fin de encriptar o desencriptar los\
                diferentes archivos y conservarlos")
        texto.pack(side=tk.TOP)

        # Entrada
        entry = ttk.Entry(root)
        entry.insert(0, "Contraseña123")
        entry.pack(side=tk.TOP)

        # Un puto espacio
        espacio = tk.Label(root, text="\n\n")
        espacio.pack(side=tk.TOP)

        # Botón de salida
        button = tk.Button(root, text="Aceptar", command=lambda: root.destroy())
        button.pack(side=tk.TOP)

        # Otro puto espacio
        espacio.pack(side=tk.BOTTOM)

        root.mainloop()

        func(*args, **kwargs)
        return entry.get()

    return wrapper

# ENCRIPTAR =====================================================================



# # Encriptar Archivos
# def Encrypt_All():
#     """
#     Esto encripta todo. (con todo y botón)
#     """
#     base("Encriptar")

#     # Bucle para desencriptar todo
#     for archivo in files:
#         mn.encriptar(archivo.name, archivo.name, contra)


# # Desencriptar Archivos
# def Dencrypt_All():
#     """
#     Esto desencripta todo. (con todo y botón)
#     """
#     base("Desencriptar")

#     # Bucle pa desencriptar
#     for archivo in files:
#         mn.desencriptar(archivo.name, archivo.name, contra)



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
