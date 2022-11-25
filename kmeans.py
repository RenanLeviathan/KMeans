import metadata.config as conf
from utils.arff_handler import parser
from utils.math_utils import euclidiana
from random import randint
import math

def exec(K=1, M, arq):
	parser(arq) #interpreta o arquivo arff
	for i in range(K): #definição dos centros iniciais
		k = randint(0,len(conf.data))
		conf.centroids.append(conf.data[k])
	#calcula cada ponto da base
	for x in conf.data:
		minima = math.inf
		c_min = []
		for c,v in conf.centroids.items(): #procura o centroide mais próximo de x
			if c != x: #não pode calcular a instância consigo mesma
				if euclidiana(c,x) < minima:
					c_min = c
		conf.add_to_centroid(c_min,x)

	#reposicionamento do centroide
	for c,v in conf.centroids.items():
		t = c + v #concatena os vetores para calcular a média
		n = len(t) # número de instâncias do centroide
		m = len(t[0]) #tamanho de cada instância
		centro = [] #novo centro com as médias de cada xj
		for j=0 in range(0,m):
			s = 0  # usado para calcular a media
			for i=0 in range(0,n):
				s += t[i][j]
			centro[j] = s/n

