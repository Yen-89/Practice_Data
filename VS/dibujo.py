import turtle

def mover_tortuga_con_mensaje():
    ventana = turtle.Screen()
    ventana.bgcolor("white")

    # Configuración de la tortuga
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")  # Color de la tortuga
    t.pensize(2)

    # Dibuja "Feliz Cumpleaños"
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.write("¡Feliz Cumpleaños, Ricky!", font=("century gothic", 32, "bold"), align="left", move=False)
    
    # Cambiar de color para la tortuga
    t.color("green")

    # Mueve la tortuga de adelante hacia atrás
    t.penup()
    t.goto(-300, -50)
    t.pendown()

    for _ in range(2):
        t.forward(600)
        t.backward(600)

    # Finaliza
    ventana.exitonclick()

# Llama a la función para mover la tortuga con el mensaje
mover_tortuga_con_mensaje()




