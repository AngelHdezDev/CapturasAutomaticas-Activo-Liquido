import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys
import os

# Agregar la carpeta 'core' al PYTHONPATH usando una ruta relativa
base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener la ruta del archivo actual
core_dir = os.path.join(base_dir, '..', 'core')  # Subir un nivel y agregar 'core'
sys.path.append(core_dir)



# Importar la función desde el módulo 'core.web_interactions'
from core.web_interactions import login_to_platform


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Automatización de Archivos")
        self.geometry("800x600")

        # Crear un frame principal
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Etiqueta de bienvenida
        label = ttk.Label(main_frame, text="Seleccione un archivo Excel", font=("Arial", 16))
        label.pack(pady=10)

        # Botón para buscar archivo
        btn_browse = ttk.Button(main_frame, text="Buscar Archivo", command=self.browse_file)
        btn_browse.pack(pady=5)

        # Mostrar ruta seleccionada
        self.file_label = ttk.Label(main_frame, text="Ningún archivo seleccionado", foreground="red")
        self.file_label.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=(("Archivos Excel", "*.xlsx"), ("Archivos Excel Antiguos", "*.xls"))
        )

        if file_path:
            self.file_label.config(text=f"Archivo seleccionado: {file_path}", foreground="green")
            # Automatizar el login
            login_to_platform()
        else:
            messagebox.showwarning("Advertencia", "No seleccionaste ningún archivo")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
