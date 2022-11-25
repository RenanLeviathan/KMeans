#metadata

title = ""
attr = {}
data = []
centroids = {}
def add_to_centroid(c,x):
	if c not in centroids:
		centroids[c] = [x]
	else:
		centroids[c].append(x)