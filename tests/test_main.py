import unittest
from main import funcion_a_probar  # Ajusta según el contenido de main.py

class TestMain(unittest.TestCase):
    def test_funcion(self):
        self.assertEqual(funcion_a_probar(2, 3), 5)  # Ajusta según tu función

if __name__ == '__main__':
    unittest.main()

