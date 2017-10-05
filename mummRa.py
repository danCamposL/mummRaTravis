# -*- coding: utf-8 -*-
#Funcionalidad mummRa
#Clasifica una edad dada que se encuentre dentro de determinados parámetros
#Eduardo Daniel Campos Loera
#Pruebas y Mantenimiento
class MummRa():

    resultado = 0

    def obtener_resultado(self):
        if int(self.resultado) == 1:
            print 'No existes'
        elif int(self.resultado) == 2:
            print 'Eres niño'
        elif int(self.resultado) == 3:
            print 'Eres adolescente'
        elif int(self.resultado) == 4:
            print 'Eres adulto'
        elif int(self.resultado) == 5:
            print 'Eres adulto mayor'
        elif int(self.resultado) == 6:
            print 'Eres mummRa'
        return self.resultado

    def edad(self, edad):
        try:
            if int(edad) <= 0:
                self.resultado = 1
            elif int(edad) >= 1 and int(edad) <= 13:
                self.resultado = 2
            elif int(edad) >= 14 and int(edad) <= 18:
                self.resultado = 3
            elif int(edad) >= 19 and int(edad) <= 30:
                self.resultado = 4
            elif int(edad) >= 31 and int(edad) <= 120:
                self.resultado = 5
            elif int(edad) >= 121:
                self.resultado = 6
        except:
            print 'Datos incorrectos'
