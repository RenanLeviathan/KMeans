import metadata.config as conf
from utils.arff_handler import parser
from utils.math_utils import euclidiana
from random import randrange
import math

def exec(K=1, M=1, arq=""):
	parser(arq) #interpreta o arquivo arff
	matriz = []
	iniciais = []
	for k in range(K): #definição dos centros iniciais
		novo = randrange(0, len(conf.data))
		iniciais.append(novo)
		conf.clusters[k] = {novo}
	#calcula cada ponto da base
	o = 1
	# forma a matriz de distância
	m = len(conf.data)  # numero de instâncias
	for i in range(m+K): #inicializa a matriz incluindo o espaço dos centroides
		matriz.append([0 for j in range(m+K)])

	for i in range(m):
		for j in range(m):
			if i != j:
				matriz[i][j] = euclidiana(conf.data[i], conf.data[j])
	#atualiza a distância com os centros
	for i in range(K):
		for j in range(m):
			if i != j:
				matriz[m+i][j] = euclidiana(conf.data[iniciais[i]], conf.data[j])

	#primeira iteração do kmeans considera os k centros iniciais
	for j in range(m):
		minima = math.inf
		min_idx = 0
		for i in range(K):
			if matriz[m+i][j] < minima:
				minima = matriz[m+i][j]
				min_idx = i #atualiza o cluster mais próximo da instância
		conf.clusters[min_idx].add(j) #coloca a instância no cluster

	while o <= M:
		#reposicionamento de centroide
		for c in range(K):
			t = [] #inicia lista temporária com todos os elementos do cluster
			for x in conf.clusters[c]:
				t.append(conf.data[x])
			centro = [0 for i in range(len(conf.data[0]))]
			for j in range(len(t[0])):
				s = 0
				for i in range(len(t)):
					s += t[i][j]
				centro[j] = s/len(t) # atualiza a média
			#atualiza a matriz de distância com o centro
			for j in range(m):
				matriz[m+c][j] = euclidiana(centro, conf.data[j])
			print("Iteração {}".format(o))
			print("Média do cluster {} -> {}".format(c, centro))
			print("Instâncias clusterizadas em {}: {}".format(c, len(conf.clusters[c])))

		# renova os clusters
		for k in range(K):
				conf.clusters[k] = set()

		#atualização de clusters
		for j in range(m):
			minima = math.inf
			min_idx = 0
			for k in range(K):
				if matriz[m+k][j] < minima:
					minima = matriz[m+k][j]
					min_idx = k
				conf.clusters[min_idx].add(j)

		o = o + 1