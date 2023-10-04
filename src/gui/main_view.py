import tkinter as tk

root = tk.Tk()

my_label = tk.Label(root)
my_label.pack()

# Creamos un textbox
textbox = tk.Text(root)
textbox.pack()

# Creamos un botón
button = tk.Button(root, text="Cambiar texto")
button.pack()


# Definimos la acción del botón
def change_text():
    # Obtenemos el valor del textbox
    value = textbox.get("1.0", "end-1c")

    # Cambiamos el texto del textbox
    textbox.delete("1.0", "end")

    # Modificamos el valor del label.
    my_label.config(text=value)


# Conectamos el botón a la acción
button.config(command=change_text)

root.mainloop()
