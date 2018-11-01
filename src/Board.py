#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame as pg 
import numpy  as np 
class ChessBoard():
	def __init__(self,dimensao,title):
		"""Classe responsavel pela interface grafica"""
		self.__bknight       = pg.image.load('../img/bknight.png')
		self.__wknight       = pg.image.load('../img/wknight.png')
		self.__squareCenters = []
		self.__corEscura     = (251, 196, 117)
		self.__corClara      = (139, 69, 0)
		self.__ScreenWidth   = 440
		self.__ScreenHeight  = 440
		self.__screen        = pg.display.set_mode((self.__ScreenWidth, self.__ScreenHeight))
		self.__title         = pg.display.set_caption("Geração "+str(title))
		self.__dimensao      = dimensao
		self.__delay         = 50

	def InicializaTabuleiro(self,posInicial):
		"""Desenha as casas do tabuleiro e adiciona a imagem do cavalo branco na posicao inicial"""
		colors    = [self.__corClara,self.__corEscura]
		increment = self.__ScreenWidth/self.__dimensao
		index     = 1  # mudar de cor (index - 1) * -1
		for column in xrange(self.__dimensao):
			for row in xrange(self.__dimensao):
				Square = pg.Rect(row * increment, column * increment, increment + 1, increment + 1)
				if Square not in self.__squareCenters:
					self.__squareCenters.append(Square)
				pg.draw.rect(self.__screen, colors[index], Square)
				index = (index - 1) * -1
			index = (index - 1) * -1
		self.__screen.blit(self.__wknight, self.__squareCenters[(posInicial[0]*self.__dimensao)+(posInicial[1])])
		pg.display.update()

	def MovimentoKnight(self,movimento):
		"""Adiciona a imagem do cavalo negro a determinada casa"""
		self.__screen.blit(self.__bknight,self.__squareCenters[(movimento[0]*self.__dimensao)+(movimento[1])])
		pg.display.update()
		pg.time.delay(self.__delay)

def main():
	InicializaTabuleiro((0,2))
	while True:
		pass

if __name__ == '__main__':
	main()