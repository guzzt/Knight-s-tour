class Cavalo():
	def __init__(self,PosAtual=(0,2),NovaPos=(0,2)):
		self.__PosAtual = PosAtual;

	@property
	def PosAtual(self):
		"""Get posicao atual"""
		return self.__PosAtual

	@PosAtual.setter
	def PosAtual(self, valor):
		"""Set posicao atual"""
		self.__PosAtual = valor

	"""Verifica se um movimento pode ser realizado dada a posicao do cavalo, se for retorna o novo movimento"""
	def Mov1(self,dimensaoTabuleiro):
		if((self.PosAtual[0]+1 < dimensaoTabuleiro) and (self.PosAtual[1]-2 >= 0)):
			 return (self.PosAtual[0]+1,self.PosAtual[1]-2)
		return None

	def Mov2(self,dimensaoTabuleiro):
		if((self.PosAtual[0]-1 >= 0) and (self.PosAtual[1]-2 >= 0)):
			return (self.PosAtual[0]-1,self.PosAtual[1]-2)
		return None

	def Mov3(self,dimensaoTabuleiro):
		if((self.PosAtual[0]-2 >= 0) and (self.PosAtual[1]-1 >= 0)):
			return (self.PosAtual[0]-2,self.PosAtual[1]-1)			
		return None

	def Mov4(self,dimensaoTabuleiro):
		if((self.PosAtual[0]-2 >= 0) and (self.PosAtual[1]+1 < dimensaoTabuleiro)):
			return (self.PosAtual[0]-2,self.PosAtual[1]+1)
		return None

	def Mov5(self,dimensaoTabuleiro):
		if((self.PosAtual[0]-1 >= 0) and (self.PosAtual[1]+2 < dimensaoTabuleiro)):
			return (self.PosAtual[0]-1,self.PosAtual[1]+2)
		return None

	def Mov6(self,dimensaoTabuleiro):
		if((self.PosAtual[0]+1 < dimensaoTabuleiro) and (self.PosAtual[1]+2 < dimensaoTabuleiro)):
			return (self.PosAtual[0]+1,self.PosAtual[1]+2)
		return None

	def Mov7(self,dimensaoTabuleiro):
		if((self.PosAtual[0]+2 < dimensaoTabuleiro) and (self.PosAtual[1]-1 >= 0)):
			return (self.PosAtual[0]+2,self.PosAtual[1]-1)
		return None
		
	def Mov8(self,dimensaoTabuleiro):
		if((self.PosAtual[0]+2 < dimensaoTabuleiro) and (self.PosAtual[1]+1 < dimensaoTabuleiro)):
			return (self.PosAtual[0]+2,self.PosAtual[1]+1)
		return None

def main():
	c = Cavalo()
	c.Mov1()
	c.Mov3()
	print c.NovaPos
if __name__ == '__main__':
	main()