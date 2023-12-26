import matplotlib.pyplot as plt

def plot_feliz_cumpleanios():
    # Configuración del gráfico
    plt.figure(figsize=(8, 4))
    plt.axis('off')  # Desactivar ejes

    # Agregar el texto
    texto = "¡Feliz Cumpleaños, Ricky!"
    plt.text(0.5, 0.5, texto, ha='center', va='center', fontsize=20, color='green')

    # Mostrar el gráfico
    plt.show()

# Llamar a la función para generar el gráfico
plot_feliz_cumpleanios()

