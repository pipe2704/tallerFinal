from tkinter import *
from app.mongodb import MongoDB

class CalculatorGUI:
    def __init__(self, master=None, mongo=None):
        self.master = master
        self.mongo = mongo  # Objeto MongoDB opcional
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Calculadora")
        self.master.geometry("450x550")  # Ajuste el tamaño de la ventana
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        container = Frame(self.master)
        container.grid(row=0, column=0, sticky="nsew")

        for i in range(5):
            container.grid_rowconfigure(i, weight=1)
        for j in range(4):
            container.grid_columnconfigure(j, weight=1)

        self.entry_var = StringVar()
        self.entry = Entry(container, textvariable=self.entry_var, font=('Arial', 24), state='readonly')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)  # Añadí padding

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            button = Button(container, text=button_text, font=('Arial', 18),
                            command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)  # Añadí padding
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, text):
        if text == '=':
            self.evaluate_expression()
        elif text == 'C':
            self.clear_entry()
        else:
            current_text = self.entry_var.get()
            self.entry_var.set(current_text + text)

    def evaluate_expression(self):
        expression = self.entry_var.get()
        try:
            result = eval(expression)
            self.entry_var.set(str(result))
            if self.mongo:
                operacion = '+' if '+' in expression else '-' if '-' in expression else '*' if '*' in expression else '/'
                self.mongo.guardar_operacion(expression, result, operacion)
        except Exception as e:
            self.entry_var.set("Error al evaluar la expresión: {}. Error: {}".format(expression, str(e)))

    def clear_entry(self):
        self.entry_var.set("")

# Código para probar la interfaz si se ejecuta este script directamente
def main():
    root = Tk()
    mongo = MongoDB()  # Suponiendo que ya has configurado la clase MongoDB correctamente
    app = CalculatorGUI(root, mongo=mongo)
    root.mainloop()

if __name__ == "__main__":
    main()


