def devoiler(lettre,mot_final,mot_en_cours):
	mot=""
	for i in range(len(mot_final)):
		if mot_final[i]==lettre:
			mot=mot+lettre
		else:
			mot=mot+mot_en_cours[i]
	#print(mot)
	return mot
#devoiler("a","alphabet","********")

def initmotencours(mot_final):
	mot_en_cours=""
	for i in range(len(mot_final)):
		mot_en_cours=mot_en_cours+"*"
	return mot_en_cours

