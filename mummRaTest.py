# -*- coding: utf-8 -*-
#Pruebas unitarias para mummRa
#Eduardo Daniel Campos Loera
import unittest

from mummRa import MummRa

class MummRaTest(unittest.TestCase):

    def setUp(self):
        self.mumm = MummRa()

    def test_no_existes(self):
        self.mumm.edad(0)
        self.assertEquals(self.mumm.obtener_resultado(), 1)

    def test_nino(self):
        self.mumm.edad(12)
        self.assertEquals(self.mumm.obtener_resultado(), 2)

    def test_adolescente(self):
        self.mumm.edad(16)
        self.assertEquals(self.mumm.obtener_resultado(), 3)

    def test_adulto(self):
        self.mumm.edad(27)
        self.assertEquals(self.mumm.obtener_resultado(), 4)

    def test_adulto_mayor(self):
        self.mumm.edad(110)
        self.assertEquals(self.mumm.obtener_resultado(), 5)

    def test_mumm_ra(self):
        self.mumm.edad(111000)
        self.assertEquals(self.mumm.obtener_resultado(), 6)

    def test_letra(self):
        self.mumm.edad('a')
        self.assertEquals(self.mumm.obtener_resultado(), 0)

if __name__=='__main__':
    unittest.main()
