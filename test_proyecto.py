# coding=utf-8
import unittest

from proyecto import Calendario,Cita

class TestProyecto(unittest.TestCase):
    def setUp(self):
        self.calendario=Calendario()
        self.day=1
        self.month=2
        self.year=2000
        self.cita=Cita(01,02,2000)
    def testCreacionCalendario(self):
        self.assertIsInstance(self.calendario,Calendario,"Objeto calendario creado correctamente")
    def testCreacionCita(self):
        self.assertIsInstance(self.cita,Cita,"Objeto cita creado correctamente")
    def testContenidoCalendario(self):
        self.assertIsInstance(self.calendario.dOcuped,list,"Lista de dias ocupados creado correctamente")
    

if __name__ == "__main__":
    unittest.main()
