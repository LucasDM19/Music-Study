#coding=utf-8
import unittest
from GuitarClass import * #Classe a ser testada - Chama TUDO

def main():
    unittest.main()  
    
# Here's our "unit tests".
class TestNota(unittest.TestCase):
   def testNotaSimples(self):
      n = Nota("G")
      self.assertEqual( n.soma(1), "A" )
      self.assertEqual( n.subtrai(1), "F" )
      
class TestNotaCromatica(unittest.TestCase):
   def testNotaCromaticaSustenida(self):
      nc = NotaCromatica("C#")
      self.assertEqual( nc.nota, "C#" ) #Dó Sustenido
      
   def testNotaCromaticaAcidentes(self):
      nc = NotaCromatica("G")
      self.assertEqual( nc.soma(1), "G#" ) #Sol Sustenido
      self.assertEqual( nc.subtrai(1), "F#" ) #Fá Sustenido

class TestGuitarra(unittest.TestCase):
   def testCordasSoltas(self):
      g = Guitar("Guitarra")
      self.assertEqual( g.toca([0, 0, 0, 0, 0, 0]), ["E", "B", "G", "D", "A", "E"] )
      self.assertEqual( g.toca([1, 1, 1, 1, 1, 1]), ["F", "C", "G#", "D#", "A#", "F"] )
      
if __name__ == '__main__':
    main()