import socket
import threading
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Función para calcular los niveles de soporte y resistencia
def calcular_soporte_resistencia(datos, ventana=5):
    soporte = pd.Series(index=datos.index)
    resistencia = pd.Series(index=datos.index)

    for i in range(ventana, len(datos) - ventana):
        ventana_datos = datos[i - ventana:i + ventana + 1]
        minimo = ventana_datos.min()
        maximo = ventana_datos.max()
        media = ventana_datos.mean()
        rango = maximo - minimo

        if datos[i] <= minimo + 0.05 * rango:
            soporte[i] = datos[i]
        elif datos[i] >= maximo - 0.05 * rango:
            resistencia[i] = datos[i]

    return soporte, resistencia


# Función para actualizar el gráfico en tiempo real
def actualizar_grafico(event=None,entrada_d=''):
    # Obtener datos del campo de entrada
    if entrada_d!='':
        entrada = entrada_d
    else:
        entrada=entrada_datos.get()

    # Añadir nuevo dato a la serie de datos
    datos.append(int(entrada))

    # Calcular soporte y resistencia
    soporte, resistencia = calcular_soporte_resistencia(pd.Series(datos))
    print("soporte:"+soporte)
    print("resistencia:" + resistencia)
    # Actualizar el gráfico
    ax.clear()
    ax.plot(datos, label='Datos', color='blue')
    ax.axhline(y=soporte.mean(), color='green', linestyle='--', label='Soporte')
    ax.axhline(y=resistencia.mean(), color='red', linestyle='--', label='Resistencia')
    ax.set_title('Niveles de Soporte y Resistencia')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)
    canvas.draw()

    # Actualizar el historial de datos
    historial_lista.insert(tk.END, entrada)


# Función para resetear los datos y el gráfico
def resetear_datos():
    global datos
    datos = []
    ax.clear()
    ax.set_title('Niveles de Soporte y Resistencia')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Valor')
    canvas.draw()
    historial_lista.delete(0, tk.END)


# Función para iniciar el servidor socket
# Función para iniciar el servidor socket
def iniciar_servidor():
    HOST = 'localhost'  # Dirección IP del servidor
    PORT = 65432  # Puerto utilizado por el servidor

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"El servidor está escuchando en {HOST}:{PORT}")
        conn, addr = s.accept()
        print(f"Conexión establecida desde {addr}")
        delimiter="|"
        with conn:
            print('Conectado con', addr)
            while True:
                try:
                    data = b''  # Inicializamos un byte array vacío
                    chunk = conn.recv(2048)
                    valor=chunk.decode()
                    if delimiter in valor:
                        print("valor1"+str(valor))
                        valor=valor.split("|")
                        for i in valor:
                            if i !='':
                                print("i"+str(i))
                                actualizar_grafico(None, i)
                    else:
                        valor=valor.replace("|","")
                        print("str:"+valor)
                except:
                    print("Falle")



# Crear y configurar la ventana principal
root = tk.Tk()
root.title("Análisis de Soporte y Resistencia en Tiempo Real")

# Crear lienzo para el gráfico
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear campo de entrada
entrada_datos = tk.Entry(root)
entrada_datos.pack(side=tk.LEFT, padx=10, pady=10)

# Asociar el evento <Return> a la función actualizar_grafico
entrada_datos.bind('<Return>', actualizar_grafico)

# Botón para ingresar el dato
boton_ingresar = tk.Button(root, text="Ingresar Dato", command=actualizar_grafico)
boton_ingresar.pack(side=tk.LEFT, padx=10, pady=10)

# Botón para resetear los datos
boton_resetear = tk.Button(root, text="Resetear Datos", command=resetear_datos)
boton_resetear.pack(side=tk.LEFT, padx=10, pady=10)

# Historial de datos ingresados
historial_lista = tk.Listbox(root, width=30)
historial_lista.pack(side=tk.LEFT, padx=10, pady=10)

# Lista para almacenar los datos
datos = []

# Iniciar el servidor en un hilo aparte
threading.Thread(target=iniciar_servidor, daemon=True).start()

# Ejecutar la aplicación
tk.mainloop()
