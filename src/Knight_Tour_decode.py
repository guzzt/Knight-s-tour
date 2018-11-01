#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BRKGA     import BRKGA
from Cavalo    import Cavalo
from math      import sqrt
from copy      import deepcopy
from Tabuleiro import Tabuleiro
from optparse  import OptionParser

LEN_BOARD = 64

class Decode(BRKGA):
	def __init__(self,nCasas,nIndividuos,fatorCrossover):
		self.nCasas = nCasas; #Numero de casas do tabuleiro
		super(Decode,self).__init__(nIndividuos,nCasas,fatorCrossover)

	def Imprime(self):
		self.ImprimePopulacao()

	def Inicializa(self):
		"""Incializa BRKGA"""
		self.InicializaPopulacao() 

	def Tour(self,CromTab,knight,geracao):
		"""Verifica se o movimento é possivel, verifica se já passou pela casa e verifica qual a casa que possui a menor chave, 
		movimenta o cavalo pra essa casa, e incrementa o numero de movimentos (fitness)"""
		t         = Tabuleiro(knight.PosAtual,geracao);
		menor     = 1
		nMov      = 0;
		movimento = None;

		while True:
			if((knight.Mov1(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov1(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov1(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov1(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov2(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov2(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov2(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov2(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov3(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov3(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov3(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov3(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov4(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov4(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov4(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov4(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov5(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov5(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov5(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov5(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov6(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov6(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov6(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov6(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov7(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov7(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov7(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov7(int(sqrt(self.nCasas)))
				menor     = CromTab[movimento]

			if((knight.Mov8(int(sqrt(self.nCasas)))) and (t.matriz[knight.Mov8(int(sqrt(self.nCasas)))] == 0) and (CromTab[knight.Mov8(int(sqrt(self.nCasas)))] < menor)):
				movimento = knight.Mov8(int(sqrt(self.nCasas)))
				menor = CromTab[movimento]

			if(not movimento): #se o cavalo não movimentar retorna o fitness da solucao
				print("[*]Numero de movimentos: "+str(nMov))
				t.ImprimeTabuleiro()
				return nMov;
			else:
				nMov += 1;
				menor = 1
				knight.PosAtual = movimento
				t.MovimentaCavalo(knight.PosAtual)
				movimento = None;

	def AvaliaPopulacao(self,geracao):
		"""Calcula o fitness de cada solucao"""
		Populacao = self.Populacao
		for cromossomo in Populacao:
			cromAux      = deepcopy(cromossomo)
			cromAux.Gene = cromAux.Gene.reshape(int(sqrt(self.nCasas)),int(sqrt(self.nCasas)))
			knight       = Cavalo()
			cromossomo.Fitness = self.Tour(cromAux.Gene,knight,geracao)
			
def main():

	parser = OptionParser(usage="Options: --gerations <int> --population <int> --mutation_factor <float> --crossover_factor <float>",conflict_handler="resolve")
#	parser.add_option('--len_board', type='int',dest='len_board', default=64)
	parser.add_option('--gerations', type='int',dest='gerations', default=30)
	parser.add_option('--population',type='int',dest='population',default=5)
	parser.add_option('--mutation_factor', type='float',dest='mutation_factor', default=1/4)
	parser.add_option('--crossover_factor',type='float',dest='crossover_factor',default=0.5)
	(options,args) = parser.parse_args()

	print(parser.usage)

	d = Decode(LEN_BOARD,options.population,options.crossover_factor);
	d.Inicializa()
	nova_Pop = []
	for i in xrange(options.gerations): #Numero de geracoes
		print("[+]GERACAO: "+str(i))
		d.AvaliaPopulacao(i)
		d.CategorizaPopulacao()
		nova_Pop += list(d.Populacao_elit) #Nova populacao recebe os individuos da populacao elite
		for i in xrange(len(d.Populacao) - len(d.Populacao_elit)): #Faz crossover para gerar o restante dos individuos da populacao
			nova_Pop.append(d.Crossover())
		d.ScrambleMutation(); #Faz mutação nos individuos da populacao mutante (os piores individuos)
		d.__Populacao = nova_Pop
		nova_Pop = []

if __name__ == '__main__':
	main()