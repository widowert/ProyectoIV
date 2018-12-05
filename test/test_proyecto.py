import unittest,sys,os,json
from flask import jsonify
sys.path.append("./src/")
from classes import Citas

class TestProyecto(unittest.TestCase):
    def setUp(self):
        #Setting up los objetos a usar en el test posteriormente
        self.dates=Citas()
        self.dates.setTestingClass(True)
    def testCreacionCita(self):
        #Comprobando correcta creacion del objeto Citas
        self.assertIsInstance(self.dates,Citas,"Objeto citas creado correctamente")
    def testGetFreeDates(self):
        #Comprobando valor devuelto en modo testing ERROR
        assert self.dates.getFreeDates(10,10,10) == "ERROR"
        assert self.dates.getFreeDates(10,10) == "ERROR"
        assert self.dates.getFreeDates(0,0,0) == "ERROR"
        assert self.dates.getFreeDates(11,11,10) == "ERROR"
        #Comprobando valor devuelto modo testing ENCONTRANDO las citas
        #y que existen los json asociados a las citas
        assert self.dates.getFreeDates(11,11,18) == "FOUND"
        assert self.dates.getFreeDates(11,11) == "FOUND"
    def testGetAllFreeDates(self):
        #Comprobando que exite el json asociado y el metodo funciona
        assert self.dates.getAllFreeDates() == "FOUND"
    def testGetMyDates(self):
        #Comprobando existencia de json de citas registradas y metodo
        #con diferentes usuarios inexistentes
        assert self.dates.getMyDates("username")=="ERROR"
        assert self.dates.getMyDates("")=="ERROR"
        assert self.dates.getMyDates("osca")=="ERROR"
        #Comprobando que con usuarios existentes devuelve correctamente
        assert self.dates.getMyDates("oscar")=="FOUND"
        assert self.dates.getMyDates("marina")=="FOUND"
    def testGetAllOccupiedDates(self):
        #Comprobando existencia de json asociado y funcionamiento del metodo
        assert self.dates.getAllOccupiedDates() == "FOUND"


if __name__ == "__main__":
    unittest.main()
