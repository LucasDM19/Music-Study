#coding=utf-8
from string import ascii_uppercase

#Classe para o deslocamento entre as notas
class Nota():
   #Para criar as estruturas próprias, com base no total de notas informadas, nos nomes e nos IDs de notas
   def initRegraNotas(self, _TOTAL_NOTAS, _nomes_notas, _notas_validas):
      if((len(_nomes_notas) != len(_notas_validas)) or (_TOTAL_NOTAS != len(_notas_validas)) or (_TOTAL_NOTAS != len(_nomes_notas))): #Passou coisa a mais, ou coisa a menos
         raise Exception("Escala incorreta com relação aos totais", len(_nomes_notas), len(_notas_validas), _TOTAL_NOTAS)
      self.TOTAL_NOTAS = _TOTAL_NOTAS
      self.indices = range(self.TOTAL_NOTAS)
      self.notas_validas = _notas_validas
      self.nomes_notas = _nomes_notas
      self.notas_dict = dict(zip(self.notas_validas, self.indices))
      self.numeros_dic = dict(zip(self.indices, self.notas_validas))
      self.nomes_dict = dict(zip(self.indices, self.nomes_notas))
      
   #Agora, com base nas regras particulares (escala de notas, acidentes, etc), inicia a estrutura
   def initNotas(self, _note):
      if not _note in self.notas_validas:
         raise Exception("Nota inváda", _note)
      self.nota = _note
      self.nota_numero = self.notas_dict[self.nota] #Com base na sigla, acho indice
      self.nota_nome = self.nomes_dict[self.nota_numero] #Com base no indice, acho nome da nota
      #print(self.nota, self.nota_numero, self.nota_nome )
      
   def __init__(self, _note):
      self.initRegraNotas(_TOTAL_NOTAS=7, _nomes_notas=["Dó", "Ré", "Mi", "Fá" , "Sol", "Lá", "Si"], _notas_validas=["C", "D", "E", "F", "G", "A", "B"]) #Preparo tudo
      self.initNotas(_note) #Mutretinha, em nome da facilidade de herança
      
   def soma(self, n):
       if not n in range(self.TOTAL_NOTAS+1):
           raise Exception("Número inválido", n)

       old_number = self.notas_dict[self.nota]
       new_number = (old_number + n) % self.TOTAL_NOTAS
       return self.numeros_dic[new_number]

   def subtrai(self, n):
       if not n in range(self.TOTAL_NOTAS+1):
         raise Exception("Número inválido", n)

       old_number = self.notas_dict[self.nota]
       new_number = (old_number - n) % self.TOTAL_NOTAS
       return self.numeros_dic[new_number]

#Classe que implementa, com tranquilidade, a Nota Cromática. A lógica é a mesma. Só muda a inclusão dos acidentes.
class NotaCromatica(Nota):
   def __init__(self, _nota):
      self.initRegraNotas(_TOTAL_NOTAS=12, _nomes_notas=["Dó", "Dó Sustenido", "Ré", "Ré Sustenido", "Mi", "Fá", "Fá Sustenido", "Sol", "Sol Sustenido", "Lá", "Lá Sustenido", "Si"], 
      _notas_validas=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']) #Preparo tudo
      self.initNotas(_nota) #Mutretinha, em nome da facilidade de herança
      
#Cada corda da guitarra tera, na posição 0, uma nota       
class Corda():
   def __init__(self, _notaCorda=None, _maximoCasas=20):
      if (not isinstance(_notaCorda, NotaCromatica)) and (not isinstance(_notaCorda, Nota)):
         raise Exception("Classe inválida", _notaCorda)
      if( _maximoCasas is None or _maximoCasas<0):
         raise Exception("Valor inválido para casa máxima", _maximoCasas)
      self.notaCorda = _notaCorda
      self.maximoCasas = _maximoCasas
   
   def toca(self, _casa):
      if(_casa <-2 or _casa > self.maximoCasas):
         raise Exception("Casa inválida", _casa)
      return self.notaCorda.soma(_casa) 
           
#Começando por cima. Uma Guitarra tem seis cordas. Cada corda possui uma escala de notas.
class Guitar:
   tipos_guitarras = {"Violão" : ["E", "B", "G", "D", "A", "E"], "Baixo" : ["G", "D", "A", "E"], "Guitarra" : ["E", "B", "G", "D", "A", "E"], "Ukulele" : ["A", "E", "C", "G"],}
   def __init__(self, _tipoGuitarra):
      if _tipoGuitarra not in Guitar.tipos_guitarras:
         raise Exception("Tipo Inválido de Guitarra", _tipoGuitarra)
      self.tipoGuitarra = _tipoGuitarra
      self.cordas = []
      for nota in Guitar.tipos_guitarras[self.tipoGuitarra]:
         self.cordas.append( Corda(NotaCromatica(nota)) )

   def toca(self, itemTab):
      #print("Plein!")
      if( len(itemTab) != len(self.cordas) ): #Se falta informacao
         raise Exception("Item de Tablatura inválido", itemTab)
      return [self.cordas[_idx].toca(itemTab[_idx]) for _idx in range(len(itemTab)) ] 
      
   def ObtemAcorde(self, notaFundamental=NotaCromatica("A"), tipoAcorde="M", capo=0):
      NOTA_FUNDAMENTAL = 0 #Sem deslocamento
      TERCA_MENOR = 3 #1 Tons e um Semi Tom
      TERCA_MAIOR = 4 #2 Tons
      QUINTA_DIMINUTA = 6 #3 Tons
      QUINTA_JUSTA = 7 #3 Tons e um Semi Tom
      QUINTA_AUMENTADA = 8 #4 Tons
      SETIMA_DIMINUTA = 10 #5 Tons
      ACORDE_MAIOR = "M" 
      ACORDE_MENOR = "m"
      ACORDE_AUMENTADO = "aum"
      ACORDE_DIMINUTO = "dim"
      dictAcordes = { 
         ACORDE_MAIOR : [NOTA_FUNDAMENTAL, TERCA_MAIOR, QUINTA_JUSTA] ,
         ACORDE_MENOR : [NOTA_FUNDAMENTAL, TERCA_MENOR, QUINTA_JUSTA] ,
         ACORDE_AUMENTADO : [NOTA_FUNDAMENTAL, TERCA_MAIOR, QUINTA_AUMENTADA] ,
         ACORDE_DIMINUTO : [NOTA_FUNDAMENTAL, TERCA_MENOR, QUINTA_DIMINUTA, SETIMA_DIMINUTA] ,
      }
      acorde = [] #Por padrão, será vazio
      min_casas = capo #Para mudar traste
      max_casas = 4+min_casas #Tem a ver com os dedos
      acordeInc = [notaFundamental.soma(item) for item in dictAcordes[tipoAcorde] ] #Obtenho os deslocamentos possiveis - Nem usei

      #if len([n for n in notas1 if n not in notas2]) == 0: #Aí sim
      for corda in range(len(self.cordas)):
         casasCandidatas = [x for x in range(min_casas,max_casas) for y in dictAcordes[tipoAcorde] if notaFundamental.soma(y)==self.cordas[corda].toca(x)]
         if len(casasCandidatas) == 1:
            acorde.append( casasCandidatas[0] ) #Pego apenas o primeiro
         elif len(casasCandidatas) == 0: #Nao tem nada, então não toca
            acorde.append( -1 )
         else:
<<<<<<< HEAD
            raise Exception("Erro na HARMONIZAÇÃO do acorde=", acorde, ", corda=", corda, ", max_casas=", max_casas, ", notaFundamental=",notaFundamental.soma(0), ", tipoAcorde", tipoAcorde, ", casasCandidatas=", casasCandidatas )
=======
            acorde.append( min(casasCandidatas) ) #Heurística: Se tiver mais de uma opção, pega a menor
            #raise Exception("Erro na HARMONIZAÇÃO do acorde", acorde, corda, max_casas, notaFundamental, tipoAcorde, casasCandidatas )
>>>>>>> 18e82ab014f8e47285a400202937f83049f5929a
      #Definindo nota grave do acorde = fundamental
      ehNotaGrave = False #Por padrão, não tem o grave ainda
      acordeGrave = [] #Vamos ver
      for idx_casa in range(len(acorde)-1,-1,-1):
         #print("i=", idx_casa, ehNotaGrave, acorde[idx_casa], acordeGrave, self.cordas[idx_casa].toca(acorde[idx_casa]), notaFundamental.soma(0) )
         if self.cordas[idx_casa].toca(acorde[idx_casa]) == notaFundamental.soma(0) and ehNotaGrave==False: #Se é a nota fundamental
            ehNotaGrave = True #Ativo apenas uma vez
            acordeGrave.append(acorde[idx_casa])
         elif ehNotaGrave==False : #Nota que não deve ser tocada
            #acorde[idx_casa] == -1 #Deixa ela intocada
            acordeGrave.append(-1)
         else: #Só mantém
            acordeGrave.append(acorde[idx_casa])
      acorde = list(reversed(acordeGrave)) #Inverto
      return acorde #[0, 2, 2, 2, 0, -1]
      
if __name__ == '__main__':
   g = Guitar("Guitarra")
   g.toca([0, 0, 0, 0, 0, 0])
   g.toca([1, 1, 1, 1, 1, 1])
   
   #e = NotaCromatica("E")
   #print(e.subtrai(3))
   
   #c1 = Corda(e)
   #print( c1.toca(40) )
   