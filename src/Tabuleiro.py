#!/usr/bin/env python
# -*- coding: utf-8 -*-
from   BRKGA  import BRKGA
from   Cavalo import Cavalo
import numpy  as     np 
from   Board  import ChessBoard

class Tabuleiro():
	"""Essa classe servirá como auxiliar para verificar se o cavalo já passou por determinada casa"""
	def __init__(self,posInicial,geracao,Dimensao=8):
		"""Inicializa matriz com 0s"""
		self.Dimensao = Dimensao;
		self.nMov     = 1
		self.matriz   = np.array([0 for i in xrange(self.Dimensao*self.Dimensao)]).reshape(self.Dimensao,self.Dimensao);
		self.screen   = ChessBoard(Dimensao,geracao)
		self.screen.InicializaTabuleiro((0,2))

	def ImprimeTabuleiro(self):
		for i in xrange(self.Dimensao):
			print(self.matriz[i])

	def MovimentaCavalo(self,Movimento):
		"""Adiciona a determinada posicao da matriz o numero de movimentos"""
		self.matriz[Movimento] = self.nMov		
		self.nMov += 1
		#self.ImprimeTabuleiro()
		#print
		self.screen.MovimentoKnight(Movimento) #Interface grafica

def main():
	pass
if __name__ == '__main__':
	main()