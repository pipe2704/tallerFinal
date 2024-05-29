import sys
sys.path.append('C:/Users/franc/OneDrive/Escritorio/calculadora_Final')

from tkinter import Tk
from app.gui import CalculatorGUI
from app.mongodb import MongoDB

def main():
    # Crea una instancia de MongoDB
    mongo = MongoDB()

    # Crea la interfaz gráfica de la calculadora
    root = Tk()
    app = CalculatorGUI(root, mongo=mongo)
    root.mainloop()

if __name__ == "__main__":
    main()




