import metadata.config
#estados do automato: a, b

def parser(arq):
	state = 'a'
	with open(arq) as f:
		for l in f:
			l1 = l.split(' ')
			if state == 'a':
				if l1[0] == '@attribute':
					attr[l1[0]] = l1[1]
				elif l1[0] == '@relation':
					title = l1[1]
				elif l1[0] == '@data':
					state = 'b'
			elif state == 'b':
				x = l.split(',') #transforma a linha do arquivo em vetor
				data.append(x)
			else:
				raise Exception("Erro na leitura do ARFF")