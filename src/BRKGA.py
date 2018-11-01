#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy      as     np
from   Cromossomo import Cromossomo
from   copy       import deepcopy

class BRKGA(object):
	def __init__(self,NPop,nAlelos,alpha):
		self.__NPop           = NPop;    #Quantidade de individuos na população
		self.__nAlelos        = nAlelos; #Quantidade de chaves por individuo
		self.__alpha          = alpha;   #Fator determinante crossover
		self.__Populacao      = []		 #Populacao total
		self.__Populacao_mut  = set();   #População Mutante
		self.__Populacao_elit = set();   #População elite

	def InicializaPopulacao(self):
		"""Gera a população inicial"""
		c = Cromossomo(self.__nAlelos);
		for i in xrange(self.__NPop):
			aux      = deepcopy(c);
			aux.Gene = np.array([np.random.uniform(0,1) for i in xrange(self.__nAlelos)]) #Gera uma lista aleatoria uniforme com a quantidade de alelos de um cromossomo
			self.__Populacao.append(aux)

	@property
	def Populacao(self):
		"""Get Populacao"""
		return self.__Populacao;

	@property	
	def Populacao_elit(self):
		"""Get Populacao elite"""
		return self.__Populacao_elit

	@property
	def Populacao_mut(self):
		"""Get Populacao mutante"""
		return self.__Populacao_mut

	@property
	def alpha(self):
		"""Get fator determinante de crossover"""
		return self.__alpha

	@property
	def NPop(self):
		"""Get numero da populacao"""
		return self.__NPop

	@property
	def nAlelos(self):
		"""Get numero de alelos de um cromossomo"""
		return self.__nAlelos

	def ImprimePopulacao(self):
		for i in xrange(self.__NPop):
			print(self.__Populacao[i].Gene)
			
	def ScrambleMutation(self,prob=0.2):
		"""Sorteia um valor aleatorio e compara com um fator de probabilidade que informa se determinado alelo do cromossomo sofrerá ou não mutacao"""
		for cromossomo in self.__Populacao_mut:
			for i in xrange(self.__nAlelos):
				pMut = np.random.uniform(0,1); 
				if prob > pMut: #Verifica se o fator de probabilidade é maior que o valor sorteado
					cromossomo.Gene[i] = np.random.uniform(0,1) # se for sorteia um novo valor para chave

	def CategorizaPopulacao(self,fatorPop=1/4.):
		"""Categoriza a populacao entre elite e mutacao de acordo com o valor do fitness do individuo"""
		self.Populacao.sort() #ordena pelo fitness
		self.Populacao.reverse() #coloca a lista em ordem decrescente para obter o maiores fitness
		for i in xrange(int(fatorPop * self.__NPop)): #Seleciona 1/4 dos melhores individos para serem a populacao elite
			self.__Populacao_elit.add(self.__Populacao[i])

		for i in xrange(self.__NPop-1,int(fatorPop * self.__NPop),-1): #Seleciona 1/4 dos piores individos para sofrerem mutacao
			self.__Populacao_mut.add(self.__Populacao[i])

	def Crossover(self):
		"""Gera um novo individuo pegando um cromossomo da populacao elite e outro da populacao nao-elite
		   sorteia um valor aleatorio para determinar se o alelo será herdado do elite ou do não elite"""
		list_Elite   = list(self.__Populacao_elit)
		list_Plebeus = list(self.__Populacao_elit.symmetric_difference(self.Populacao))
		#Seleciona um cromossomo da populacao elite e um da populaçao nao-elite
		crom_E = list_Elite[np.random.randint(len(list_Elite))]
		crom_P = list_Plebeus[np.random.randint(len(list_Plebeus))]
		#pra cada chave, sortear um valor aleatorio se for menor q o fator de crossover a chave sera herdada da elite senao da nao-elite
		novo_crom = []
		for chave in xrange(self.nAlelos):
			if(np.random.uniform(0,1) < self.alpha):
				novo_crom.append(crom_E.Gene[chave])
			else:
				novo_crom.append(crom_P.Gene[chave])

		Cromossomo_Gerado = Cromossomo(self.nAlelos) #retorna o cromossomo
		Cromossomo_Gerado.Gene = novo_crom
		return Cromossomo_Gerado 			 

def main():
	ag = BRKGA(300,64,0.5);
	ag.InicializaPopulacao();
	ag.ImprimePopulacao();
	ag.ScrambleMutation();

if __name__ == '__main__':
	main()		
