import os
import tkinter as tk
from tkinter import ttk


class Producto:
    def __init__(self, referencia, nombre, pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre: {self.nombre}, Precio: {self.pvp}"


class alimento(Producto):
    def __init__(self, referencia, nombre, pvp, alimento):
        super().__init__(referencia, nombre, pvp)
        self.tipo = alimento

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre: {self.nombre}, Precio: {self.pvp}, Tipo: {self.tipo}"


class electrodomestico(Producto):
    def __init__(self, referencia, nombre, pvp, electrodomestico):
        super().__init__(referencia, nombre, pvp)
        self.tipo = electrodomestico

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre: {self.nombre}, Precio: {self.pvp}, Tipo: {self.tipo}"


class moda(Producto):
    def __init__(self, referencia, nombre, pvp, moda):
        super().__init__(referencia, nombre, pvp)
        self.tipo = moda

    def __str__(self):
        return f"Producto: {self.referencia}, Nombre: {self.nombre}, Precio: {self.pvp}, Tipo: {self.tipo}"


manzana = alimento(1, "Manzana", 1.5, "alimento")
pera = alimento(2, "Peras", 2, "alimento")

lavadora = electrodomestico(3, "Lavadora", 100, "Electrodomestico")
nevera = electrodomestico(4, "Nevera", 100, "Electrodomestico")

camiseta = moda(5, "Camiseta", 10, "Moda")
pantalon = moda(6, "Pantalon", 10, "Moda")

alimentos = [manzana, pera]
electrodomesticos = [lavadora, nevera]
modas = [camiseta, pantalon]

# La sección que se está viendo ahora. Al abrir, son los alimentos.
seccion_actual = electrodomesticos


def texto_producto(producto):
    return (
        f"Referencia: {producto.referencia} | "
        f"Nombre: {producto.nombre} | "
        f"Precio: {producto.pvp} | "
        f"Tipo: {producto.tipo}"
    )


def mostrar_seccion(productos):
    global seccion_actual
    seccion_actual = productos

    lista.delete(0, tk.END)
    for producto in productos:
        lista.insert(tk.END, texto_producto(producto))

    if productos:
        mensaje.config(text="Elige una referencia y pulsa Vender.")
    else:
        mensaje.config(text="Esta sección ya no tiene productos.")


def vender():
    escrito = referencia.get().strip()

    if escrito == "":
        mensaje.config(text="Escribe la referencia del producto.")
        return

    if not escrito.isdigit():
        mensaje.config(text="La referencia tiene que ser un número.")
        return

    teclado = int(escrito)

    for producto in seccion_actual:
        if producto.referencia == teclado:
            seccion_actual.remove(producto)
            referencia.delete(0, tk.END)
            mostrar_seccion(seccion_actual)
            mensaje.config(text=f"Producto vendido: {producto.nombre}")
            return

    mensaje.config(text="Producto no encontrado")


# Colores de la ventana. Cada valor es un color en formato hexadecimal.
FONDO = "#F3EDE3"
TEXTO = "#3A2E24"
LISTA = "#FFF9F2"
VERDE = "#2F7D4A"
AZUL = "#1E6B86"
ROSA = "#A34768"
AMBAR = "#C47B2B"
GRIS = "#7A7068"


def estilo_boton(style, nombre, fondo, activo):
    style.configure(
        nombre,
        background=fondo,
        foreground="white",
        font=("Helvetica", 13),
        padding=(14, 8),
        borderwidth=0,
    )
    style.map(
        nombre,
        background=[("active", activo), ("pressed", activo)],
        foreground=[("disabled", "white"), ("active", "white")],
    )


ventana = tk.Tk()
ventana.title("Centro Comercial")
ventana.geometry("680x460")
ventana.configure(bg=FONDO)

style = ttk.Style()
style.theme_use("clam")
estilo_boton(style, "Alimentos.TButton", VERDE, "#276840")
estilo_boton(style, "Electro.TButton", AZUL, "#18586E")
estilo_boton(style, "Moda.TButton", ROSA, "#8A3B58")
estilo_boton(style, "Vender.TButton", AMBAR, "#A66722")
estilo_boton(style, "Salir.TButton", GRIS, "#645C55")

tk.Label(
    ventana,
    text="Centro Comercial",
    font=("Helvetica", 22, "bold"),
    bg=FONDO,
    fg=TEXTO,
).pack(pady=12)

botones = tk.Frame(ventana, bg=FONDO)
botones.pack(pady=5)

ttk.Button(botones, text="Alimentos", style="Alimentos.TButton", command=lambda: mostrar_seccion(alimentos)).pack(side=tk.LEFT, padx=6)
ttk.Button(botones, text="Electrodomésticos", style="Electro.TButton", command=lambda: mostrar_seccion(electrodomesticos)).pack(side=tk.LEFT, padx=6)
ttk.Button(botones, text="Moda", style="Moda.TButton", command=lambda: mostrar_seccion(modas)).pack(side=tk.LEFT, padx=6)

lista = tk.Listbox(
    ventana,
    width=72,
    height=10,
    bg=LISTA,
    fg=TEXTO,
    font=("Helvetica", 13),
    selectbackground=AZUL,
    selectforeground="white",
    relief="flat",
    highlightthickness=0,
)
lista.pack(pady=14)

venta = tk.Frame(ventana, bg=FONDO)
venta.pack(pady=5)

tk.Label(venta, text="Referencia:", bg=FONDO, fg=TEXTO, font=("Helvetica", 13)).pack(side=tk.LEFT, padx=5)
referencia = tk.Entry(
    venta,
    width=10,
    bg=LISTA,
    fg=TEXTO,
    font=("Helvetica", 13),
    relief="flat",
    highlightthickness=1,
    highlightbackground="#D9CBB8",
    highlightcolor=AZUL,
)
referencia.pack(side=tk.LEFT, padx=5, ipady=4)
ttk.Button(venta, text="Vender", style="Vender.TButton", command=vender).pack(side=tk.LEFT, padx=6)

mensaje = tk.Label(ventana, text="", bg=FONDO, fg=TEXTO, font=("Helvetica", 13))
mensaje.pack(pady=12)

ttk.Button(ventana, text="Salir", style="Salir.TButton", command=ventana.destroy).pack(pady=5)

def traer_al_frente():
    ventana.lift()
    ventana.attributes("-topmost", True)
    ventana.focus_force()
    ventana.after(500, lambda: ventana.attributes("-topmost", False))
    os.system(
        f"/usr/bin/osascript -e 'tell application \"System Events\" "
        f"to set frontmost of the first process whose unix id is {os.getpid()} to true'"
    )


mostrar_seccion(electrodomesticos)
ventana.after(200, traer_al_frente)
ventana.mainloop()
