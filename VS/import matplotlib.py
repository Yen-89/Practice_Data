import matplotlib.pyplot as plt

def plot_happy_birthday():
    # Configuración del gráfico
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_facecolor('skyblue')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Dibuja las letras de "Feliz Cumpleaños"
    ax.text(1, 5, 'Feliz', fontsize=20, color='white', ha='center', va='center')
    ax.text(5, 5, 'Cumpleaños', fontsize=20, color='white', ha='center', va='center')

    # Dibuja un pastel
    circle = plt.Circle((8, 2), 1, color='orange', fill=True)
    ax.add_patch(circle)

    # Muestra el gráfico
    plt.show(block=True)

# Llama a la función para crear el gráfico
plot_happy_birthday()
