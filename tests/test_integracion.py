import unittest
from app.calculator import add, subtract
from app.mongodb import MongoDB

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Conectar a la base de datos de prueba
        self.mongo = MongoDB()
    
    def tearDown(self):
        # Cerrar la conexión después de las pruebas
        self.mongo.cerrar_conexion()

    def test_operaciones_calculadora(self):
        resultado_suma = add(2, 3)
        resultado_resta = subtract(5, 2)
        self.assertEqual(resultado_suma, 5)
        self.assertEqual(resultado_resta, 3)

if __name__ == "__main__":
    unittest.main()
