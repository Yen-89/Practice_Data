import turtle

def dibujar_feliz_cumpleanios():
    ventana = turtle.Screen()
    ventana.bgcolor("lightblue")

    # Configuración de la tortuga con forma de panda
    turtle.shape("panda")
    turtle.color("black")
    turtle.pensize(2)

    # Dibuja "Feliz Cumpleaños"
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.write("¡Feliz Cumpleaños!", font=("Arial", 16, "bold"))

    # Dibuja globos
    for color in ["red", "green", "yellow", "purple"]:
        turtle.color(color)
        turtle.penup()
        turtle.goto(-40, -40)
        turtle.pendown()
        turtle.circle(40)
        turtle.penup()
        turtle.forward(40)

    # Finaliza
    ventana.exitonclick()

# Llama a la función para dibujar el mensaje
dibujar_feliz_cumpleanios()
