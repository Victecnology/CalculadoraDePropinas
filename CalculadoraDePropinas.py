import guizero

# Crear una ventana
app = guizero.App("Calculadora de propinas")

# Crear una función para calcular la propina
def btn_calcular():
    # Obtener los valores de entrada
    importe = int(txt_importe.value)
    propina = int(txt_propina.value) / 100

    # Calcular la propina
    propina_cantidad = importe * propina

    # Calcular el total
    total = importe + propina_cantidad

    # Mostrar el resultado
    lbl_total.value = f"{total:.2f}"

# Crear etiquetas y campos de entrada
lbl_importe = guizero.Text(app, text="Importe de la factura:")
txt_importe = guizero.TextBox(app)
lbl_propina = guizero.Text(app, text="Propina (%):")
txt_propina = guizero.TextBox(app)
lbl_total = guizero.Text(app, text="Total a pagar:")

# Crear un botón
btn_calcular = guizero.PushButton(app, text="Calcular", command=btn_calcular)

# Ejecutar la aplicación
app.display()