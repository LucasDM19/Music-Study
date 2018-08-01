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

class TestAcorde(unittest.TestCase):
   def testAcordesMaiores(self):
      g = Guitar("Guitarra")
      a = g.ObtemAcorde(notaFundamental=NotaCromatica("A"), tipoAcorde="M") #Obtendo acorde de Lá Maior
      self.assertEqual( a, [0, 2, 2, 2, 0, -1] ) #-1 indica que não é para tocar a Mizona
      
   def testAcordesAumentados(self):
      g = Guitar("Guitarra")
      a = g.ObtemAcorde(notaFundamental=NotaCromatica("C"), tipoAcorde="aum") #Obtendo acorde de Dó Aumentada
      self.assertEqual( a, [0, 1, 1, 2, 3, -1] ) #-1 indica que não é para tocar a Mizona
      
if __name__ == '__main__':
    main()