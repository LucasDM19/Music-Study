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

   def testNotaCromaticaAcidentesNotaB(self):
      nc = NotaCromatica("B")
      self.assertEqual( nc.soma(1), "C" ) #Dó
      self.assertEqual( nc.subtrai(1), "A#" ) #Lá Sustenido
      
   def testNotaCromaticaAcidentesNotaG(self):
      nc = NotaCromatica("G")
      self.assertEqual( nc.soma(1), "G#" ) #Sol Sustenido
      self.assertEqual( nc.subtrai(1), "F#" ) #Fá Sustenido

class TestGuitarra(unittest.TestCase):
   def testCordasSoltas(self):
      g = Guitar("Guitarra")
      self.assertEqual( g.toca([0, 0, 0, 0, 0, 0]), ["E", "B", "G", "D", "A", "E"] )
      self.assertEqual( g.toca([1, 1, 1, 1, 1, 1]), ["F", "C", "G#", "D#", "A#", "F"] )

class TestAcordeMaior(unittest.TestCase):
   def __init__(self, *args, **kwargs):
      super(TestAcordeMaior, self).__init__(*args, **kwargs)
      self.guita = Guitar("Guitarra")
      
   def testAcordeMaiorA(self):
      acordeA = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("A"), tipoAcorde="M") 
      self.assertEqual( acordeA, [0, 2, 2, 2, 0, -1] ) #-1 indica que não é para tocar a Mizona
      
   def testAcordeMaiorC(self):
      acordeC = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("C"), tipoAcorde="M") 
      self.assertEqual( acordeC, [0, 1, 0, 2, 3, -1] ) #-1 indica que não é para tocar a Mizona
      
   def testAcordeMaiorD(self):
      acordeD = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("D"), tipoAcorde="M") 
      self.assertEqual( acordeD, [2, 3, 2, 0, -1, -1] ) #-1 indica que não é para tocar
      
   def testAcordeMaiorE(self):
      acordeE = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("E"), tipoAcorde="M") 
      self.assertEqual( acordeE, [0, 0, 1, 2, 2, 0] ) #-1 indica que não é para tocar
      
   def testAcordeMaiorG(self):
      acordeG = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("G"), tipoAcorde="M") 
      self.assertEqual( acordeG, [3, 0, 0, 0, 2, 3] ) #-1 indica que não é para tocar
      
   def testAcordeMaiorF(self):
      acordeF = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("F"), tipoAcorde="M", capo=1) 
      self.assertEqual( acordeF, [1, 1, 2, 3, 3, 1] ) 
      
   def testAcordeMaiorB(self):
      acordeB = self.guita.ObtemAcorde(notaFundamental=NotaCromatica("B"), tipoAcorde="M", capo=2) 
      self.assertEqual( acordeB, [2, 4, 4, 4, 2, -1] ) 

class TestAcordeMenor(unittest.TestCase):
   def testAcordesMenoresD(self):
      g = Guitar("Guitarra")
      a = g.ObtemAcorde(notaFundamental=NotaCromatica("D"), tipoAcorde="m") 
      self.assertEqual( a, [1, 3, 2, 0, -1, -1] ) 
      
   def testAcordesMenoresF(self):
      g = Guitar("Guitarra")
<<<<<<< HEAD
      a = g.ObtemAcorde(notaFundamental=NotaCromatica("C"), tipoAcorde="dim") #Obtendo acorde de Dó Aumentada
      self.assertEqual( a, [0, 4, 2, 4, 3, -1], capo=1 ) #-1 indica que não é para tocar a Mizona
=======
      a = g.ObtemAcorde(notaFundamental=NotaCromatica("F"), tipoAcorde="m") 
      self.assertEqual( a, [1, 1, 1, 3, 3, 1] )   
      
# class TestAcordeAumentado(unittest.TestCase):
   # def testAcordesAumentadosC(self):
      # g = Guitar("Guitarra")
      # a = g.ObtemAcorde(notaFundamental=NotaCromatica("C"), tipoAcorde="aum") #Obtendo acorde de Dó Aumentada
      # self.assertEqual( a, [0, 1, 1, 2, 3, -1] ) #-1 indica que não é para tocar a Mizona
      
# class TestAcordeDiminuto(unittest.TestCase):
   # def testAcordesDiminutosC(self):
      # g = Guitar("Guitarra")
      # a = g.ObtemAcorde(notaFundamental=NotaCromatica("C"), tipoAcorde="dim", capo=2) #Obtendo acorde de Dó Aumentado
      # self.assertEqual( a, [-1, 3, 4, 5, 4, -1] ) #-1 indica que não é para tocar a Mizona
      
   # def testAcordesDiminutosD(self):
      # g = Guitar("Guitarra")
      # a = g.ObtemAcorde(notaFundamental=NotaCromatica("D"), tipoAcorde="dim", capo=4) #Obtendo acorde de Ré Aumentado
      # self.assertEqual( a, [-1, 5, 6, 7, 6, -1] ) #-1 indica que não é para tocar a Mizona
>>>>>>> 18e82ab014f8e47285a400202937f83049f5929a
      
if __name__ == '__main__':
    main()