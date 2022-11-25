import metadata.config as conf
import re


# estados do automato: a, b

def parser(arq):
    state = 'a'
    with open(arq) as f:
        for l in f:
            l1 = l.strip('\n').split(' ')
            if state == 'a':
                if l1[0] == '@attribute' or l1[0] == '@ATTRIBUTE':
                    conf.attr[l1[1]] = l1[2]
                    if re.match('{([\w, -])*}',l1[2]):
                        conf.attr[l1[1]] = set(l1[2].strip('{}').split(',')) #caso seja um atributo nominal, converte em
                        # conjunto de valores
                elif l1[0] == '@relation' or l1[0] == '@RELATION':
                    conf.title = l1[1]
                elif l1[0] == '@data' or l1[0] == '@DATA':
                    state = 'b'
            elif state == 'b':
                x = l.split(',')  # transforma a linha do arquivo em vetor
                for i in range(0, len(x)):
                    if re.match('(real|integer)',conf.attr.keys()[i]): #se o atributo for um número
                        x[i] = int(x[i])
                conf.data.append(x)
            else:
                raise Exception("Erro na leitura do ARFF")
