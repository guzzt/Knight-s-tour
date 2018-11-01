import numpy as np

class Cromossomo():
	def __init__(self,nAlelos,fitness=1):
		self._nAlelos = nAlelos;
		self._Fitness = fitness;
		self.Gene     = np.array([]);

	@property
	def Fitness(self):
		"""Get fitness"""
		return self.Fitness;

	@property
	def nAlelos(self):
		"""Get numero de alelos do cromossomo"""
		return self.nAlelos;

	@Fitness.setter
	def Fitness(self, valor):
		"""Set fitness"""
		self._Fitness = valor; 

	def __eq__(self,outro):
		return self.Fitness == outro.Fitness

	def __lt__(self,outro):
		return self.Fitness < outro.Fitness
		
	def __hash__(self):
		return id(self) 