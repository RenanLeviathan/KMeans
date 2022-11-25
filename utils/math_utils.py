from math import sqrt

def euclidiana(X, Y):
	s = 0
	for i in range(len(X)):
		s += (Y[i] - X[i])**2
	return sqrt(s)

