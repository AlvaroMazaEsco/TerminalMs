import tkinter as tk
import subprocess
import turtle

# Lista de comandos personalizados
comandos_personalizados = ["pintar_mar", "pintar_medusa", "pintar_ojos", "ms_help", "pintar_dino", "fondo_rosa",
                           "fondo_azul", "fondo_verde", "fondo_blanco", "fondo_negro", "fondo_hacker"]


def ejecutar_comando(event=None):
    comando = entrada_comando.get()
    if comando.strip() == "clear":
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.config(state=tk.DISABLED)
        turtle.clear()  # Limpiar el lienzo de Turtle si se ejecuta "clear"
    elif comando.strip() == "pintar_mar":
        pintar_mar()
    elif comando.strip() == "pintar_medusa":
        pintar_medusa()
    elif comando.strip() == "pintar_ojos":
        pintar_ojos()
    elif comando.strip() == "ms_help":
        mostrar_ayuda()
    elif comando.strip() == "pintar_dino":
        pintar_dino()
    elif comando.strip() == "fondo_rosa":
        fondo_rosa()
    elif comando.strip() == "fondo_azul":
        fondo_azul()
    elif comando.strip() == "fondo_verde":
        fondo_verde()
    elif comando.strip() == "fondo_blanco":
        fondo_blanco()
    elif comando.strip() == "fondo_negro":
        fondo_negro()
    elif comando.strip() == "fondo_hacker":
        fondo_hacker()
    else:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.insert(tk.END, f"{resultado.stdout}")
        texto_resultado.config(state=tk.DISABLED)

    # Borrar el contenido del campo de entrada después de ejecutar el comando
    entrada_comando.delete(0, tk.END)


def mostrar_ayuda():
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.insert(tk.END, "Comandos personalizados disponibles:\n")
    for comando in comandos_personalizados:
        texto_resultado.insert(tk.END, f"- {comando}\n")
    texto_resultado.config(state=tk.DISABLED)


def pintar_mar():
    # Inicializar Turtle solo cuando se pinte el mar
    turtle.setup(width=700, height=600)
    turtle.penup()
    turtle.hideturtle()
    turtle.Screen().bgcolor("lightblue")
    turtle.speed(0)

    turtle.penup()
    turtle.goto(-350, -300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("blue")
    for _ in range(2):
        turtle.forward(700)
        turtle.left(90)
        turtle.forward(600)
        turtle.left(90)
    turtle.end_fill()

    # Ejecutar el bucle principal de la ventana
    turtle.mainloop()


def pintar_medusa():
    turtle.speed(0)
    turtle.bgcolor("lightblue")
    turtle.penup()

    # Dibujar el cuerpo de la medusa
    turtle.goto(0, -50)  # Mover un poco hacia arriba
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("purple")
    turtle.circle(150)
    turtle.end_fill()

    # Ajustar el grosor de los tentáculos
    turtle.width(10)

    # Dibujar los tentáculos con más volumen y posición ajustada
    turtle.penup()
    turtle.goto(0, -50)  # Mover un poco hacia arriba
    turtle.pendown()
    turtle.color("purple")
    for _ in range(8):
        turtle.left(45)
        turtle.forward(200)  # Aumentar la longitud de los tentáculos
        turtle.backward(200)  # Retroceder para volver al centro
    turtle.hideturtle()


def pintar_ojos():
    turtle.penup()
    turtle.goto(-60, 80)  # Ajustar la posición del primer ojo
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(60, 80)  # Ajustar la posición del segundo ojo
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-60, 80)  # Ajustar la posición de la pupila del primer ojo
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(8)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(60, 80)  # Ajustar la posición de la pupila del segundo ojo
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()

    # Pintar una boca sonriente
    turtle.penup()
    turtle.goto(0, 40)  # Posición para la boca
    turtle.pendown()
    turtle.width(4)  # Ajustar el grosor de la pluma
    turtle.color("black")
    turtle.right(90)
    turtle.circle(40, 180)  # Dibujar la parte superior de la boca
    turtle.penup()
    turtle.goto(0, 40)
    turtle.pendown()
    turtle.left(180)
    turtle.circle(-40, 180)  # Dibujar la parte inferior de la boca
    turtle.hideturtle()


def pintar_dino():
    t = turtle.Turtle()
    t.pensize(4)
    t.speed(0)
    turtle.bgcolor("black")

    def go(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    t.pencolor("#006400")
    t.fillcolor("#00FF7F")

    go(59, -25)

    t.begin_fill()
    t.seth(139)
    t.circle(119, 124)
    t.seth(273)
    t.circle(-63, 108)
    t.seth(308)
    t.circle(100, 60)
    t.seth(290)
    t.circle(122, 14)
    t.seth(0)
    t.forward(25)
    t.seth(42)
    t.forward(13)
    t.seth(90)
    t.forward(18)
    t.seth(270)
    t.forward(8)
    t.seth(0)
    t.forward(123)
    t.seth(275)
    t.circle(23, 180)
    t.seth(0)
    t.forward(8)
    t.seth(272)
    t.circle(24, 123)
    t.seth(52)
    t.circle(125, 32)
    t.seth(72)
    t.circle(473, 38)
    t.seth(102)
    t.circle(130, 109)
    t.seth(209)
    t.circle(109, 71)
    t.seth(286)
    t.circle(126, 81)
    t.seth(301)
    t.circle(-106, 36)
    t.end_fill()

    go(47, 26)
    t.seth(15)
    t.circle(126, 28)

    go(-130, -165)
    t.seth(270)
    t.circle(122, 18)

    go(47, -198)
    t.seth(270)
    t.forward(16)

    go(-61, -212)
    t.begin_fill()
    t.seth(270)
    t.circle(22, 180)
    t.end_fill()

    go(-55, 63)
    t.seth(337)
    t.circle(62, 90)

    t.fillcolor("#00CC00")

    go(-149, -141)
    t.begin_fill()
    t.seth(127)
    t.circle(19, 180)
    t.end_fill()

    go(-132, -76)
    t.begin_fill()
    t.seth(170)
    t.circle(23, 180)
    t.end_fill()

    go(-89, -20)
    t.begin_fill()
    t.seth(136)
    t.circle(29, 180)
    t.end_fill()

    go(-22, 4)
    t.begin_fill()
    t.seth(104)
    t.circle(27, 180)
    t.end_fill()

    go(59, -25)
    t.seth(139)
    t.circle(119, 124)
    t.seth(273)
    t.circle(-63, 108)

    t.fillcolor("#FFF176")

    go(91, -206)
    t.begin_fill()
    t.seth(4)
    t.circle(87, 66)
    t.seth(72)
    t.circle(473, 11)
    t.seth(186)
    t.circle(50, 58)
    t.seth(266)
    t.circle(-75, 36)
    t.seth(192)
    t.circle(50, 61)
    t.seth(268)
    t.forward(38)
    t.end_fill()

    t.pencolor("#F48FB1")
    t.fillcolor("#F48FB1")

    go(76, 116)
    t.begin_fill()
    t.seth(90)
    t.circle(17)
    t.end_fill()

    t.pencolor("black")
    t.fillcolor("black")

    go(39, 140)
    t.begin_fill()
    t.seth(90)
    t.forward(13)
    t.circle(12, 180)
    t.forward(13)
    t.circle(12, 180)
    t.end_fill()

    t.hideturtle()


def fondo_rosa():
    ventana.configure(bg="pink")
    texto_resultado.config(bg="pink")
    etiqueta.configure(bg="pink")
    entrada_comando.configure(bg="pink")
    boton_ejecutar.configure(bg="pink", fg="black")
    entrada_comando.configure(fg="black")
    texto_resultado.configure(fg="black")
    etiqueta.configure(fg="black")


def fondo_azul():
    ventana.configure(bg="lightblue")
    texto_resultado.config(bg="lightblue")
    etiqueta.configure(bg="lightblue")
    entrada_comando.configure(bg="lightblue")
    boton_ejecutar.configure(bg="lightblue", fg="black")
    entrada_comando.configure(fg="black")
    texto_resultado.configure(fg="black")
    etiqueta.configure(fg="black")


def fondo_verde():
    ventana.configure(bg="lightgreen")
    texto_resultado.config(bg="lightgreen")
    etiqueta.configure(bg="lightgreen")
    entrada_comando.configure(bg="lightgreen")
    boton_ejecutar.configure(bg="lightgreen", fg="black")
    entrada_comando.configure(fg="black")
    texto_resultado.configure(fg="black")
    etiqueta.configure(fg="black")


def fondo_blanco():
    ventana.configure(bg="white")
    texto_resultado.config(bg="white")
    etiqueta.configure(bg="white")
    entrada_comando.configure(bg="white")
    boton_ejecutar.configure(bg="white", fg="black")
    entrada_comando.configure(fg="black")
    texto_resultado.configure(fg="black")
    etiqueta.configure(fg="black")


def fondo_negro():
    ventana.configure(bg="black")
    texto_resultado.config(bg="black")
    etiqueta.configure(bg="black")
    entrada_comando.configure(bg="black")
    boton_ejecutar.configure(bg="black", fg="white")
    entrada_comando.configure(fg="white")
    texto_resultado.configure(fg="white")
    etiqueta.configure(fg="white")


def fondo_hacker():
    ventana.configure(bg="black")
    texto_resultado.config(bg="black")
    etiqueta.configure(bg="black")
    entrada_comando.configure(bg="black")
    boton_ejecutar.configure(bg="black", fg="green")
    entrada_comando.configure(fg="green")
    texto_resultado.configure(fg="green")
    etiqueta.configure(fg="green")


# Configurar tema
ventana = tk.Tk()
ventana.title("Ejecutar comandos de Bash y dibujar")
ventana.configure(bg="black")
ventana.option_add('*TCombobox*Listbox*Background', 'black')
ventana.option_add('*TCombobox*Listbox*Foreground', 'white')

# Etiqueta
etiqueta = tk.Label(ventana, text="Introduce el comando de Bash:", bg="black", fg="white")
etiqueta.pack()

# Entrada de texto para el comando
entrada_comando = tk.Entry(ventana, width=50, bg="black", fg="white")
entrada_comando.pack()

# Vincular el evento de pulsación de tecla "Enter" a la función ejecutar_comando
entrada_comando.bind("<Return>", ejecutar_comando)

# Botón para ejecutar el comando
boton_ejecutar = tk.Button(ventana, text="Ejecutar Comando", command=ejecutar_comando, bg="black", fg="white")
boton_ejecutar.pack()

# Texto para mostrar el resultado
texto_resultado = tk.Text(ventana, height=240, width=150, bg="black", fg="white", spacing2=2)
texto_resultado.pack()
texto_resultado.config(state=tk.DISABLED)  # Hacer el texto de solo lectura

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
