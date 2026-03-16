import tkinter as tk
from tkinter import messagebox
from datetime import date

# Clase para gestionar empleados
class GestionEmpleados:

    def __init__(self, identificacion, nombre, genero, cargo, dias, valor_dia):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.dias = dias
        self.valor_dia = valor_dia
        self.fecha = date.today()

    def calcular_nomina(self):
        total = self.dias * self.valor_dia
        return total


# Valores por cargo
valores = {
    "Servicios Generales": 40000,
    "Administrativo": 50000,
    "Electricista": 60000,
    "Mecánico": 80000,
    "Soldador": 90000
}

# Función para calcular nómina
def calcular():
    try:
        identificacion = entrada_id.get()
        nombre = entrada_nombre.get()
        genero = genero_var.get()
        cargo = cargo_var.get()
        dias = int(entrada_dias.get())
        valor_dia = valores[cargo]

        empleado = GestionEmpleados(
            identificacion,
            nombre,
            genero,
            cargo,
            dias,
            valor_dia
        )

        total = empleado.calcular_nomina()

        reporte = f"""
        REPORTE DE NÓMINA

        Identificación: {empleado.identificacion}
        Nombre: {empleado.nombre}
        Género: {empleado.genero}
        Cargo: {empleado.cargo}
        Días trabajados: {empleado.dias}
        Valor por día: ${empleado.valor_dia}
        Fecha registro: {empleado.fecha}

        TOTAL A PAGAR: ${total}
        """

        messagebox.showinfo("Reporte de Nómina", reporte)

    except:
        messagebox.showerror("Error", "Por favor ingrese datos válidos")


# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Nómina")
ventana.geometry("400x450")

# Campos del formulario
tk.Label(ventana, text="Identificación").pack()
entrada_id = tk.Entry(ventana)
entrada_id.pack()

tk.Label(ventana, text="Nombre Completo").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Género").pack()
genero_var = tk.StringVar(value="Masculino")

tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino").pack()
tk.Radiobutton(ventana, text="Femenino", variable=genero_var, value="Femenino").pack()

tk.Label(ventana, text="Cargo").pack()
cargo_var = tk.StringVar(value="Servicios Generales")
menu_cargo = tk.OptionMenu(ventana, cargo_var, *valores.keys())
menu_cargo.pack()

tk.Label(ventana, text="Días trabajados").pack()
entrada_dias = tk.Entry(ventana)
entrada_dias.pack()

# Botón calcular
tk.Button(ventana, text="Calcular Nómina", command=calcular).pack(pady=20)

# Ejecutar ventana
ventana.mainloop()

