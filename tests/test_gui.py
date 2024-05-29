import unittest
from tkinter import Tk
from app.gui import CalculatorGUI
from app.mongodb import MongoDB

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.mongo = MongoDB()
        self.calculator = CalculatorGUI(self.root, self.mongo)
        # Limpiar colecciones antes de cada prueba
        self.mongo.collection_sum.delete_many({})
        self.mongo.collection_rest.delete_many({})
        self.mongo.collection_multipli.delete_many({})
        self.mongo.collection_div.delete_many({})

    def tearDown(self):
        # Limpiar colecciones después de cada prueba
        self.mongo.collection_sum.delete_many({})
        self.mongo.collection_rest.delete_many({})
        self.mongo.collection_multipli.delete_many({})
        self.mongo.collection_div.delete_many({})
        self.mongo.cerrar_conexion()
        self.root.destroy()

    def test_calculate_sum(self):
        self.calculator.entry.config(state='normal')
        self.calculator.entry.insert(0, "3+2")
        self.calculator.entry.config(state='readonly')
        self.calculator.evaluate_expression()
        self.assertEqual(self.calculator.entry.get(), "5")
        # Verificar que la operación se haya guardado en la colección correcta
        result = self.mongo.collection_sum.find_one({'expresion': '3+2'})
        self.assertIsNotNone(result)
        self.assertEqual(result['resultado'], 5)

    # Los demás métodos de prueba siguen el mismo patrón de corrección

if __name__ == "__main__":
    unittest.main()
