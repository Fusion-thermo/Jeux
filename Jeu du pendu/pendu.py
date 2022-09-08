from donnees import *
from fonctions import *
from random import choice
import os
import pickle

nom=input("Nom du joueur : ")

if os.path.exists("dico_scores"):
	fichier=open('dico_scores','rb')
	mon_pickler = pickle.Unpickler(fichier)
	scores = mon_pickler.load()
	fichier.close()
else:
	scores={}

if nom not in scores:
	scores[nom]=0
print("Votre score actuel : {0}.".format(scores[nom]))


mot_final=choice(liste_mots)
mot_en_cours=initmotencours(mot_final)
liste_lettres=[]

print("Il vous reste {0} chances. Lettres utilisées : {1}".format(nbchances, liste_lettres))
while mot_final!=mot_en_cours and nbchances>0: 
	lettre=input("Lettre : ")
	if lettre in liste_lettres:
		print("Déjà dit !")
		lettre="#"
	while lettre not in alphabet:
		lettre=input("Lettre : ")
		if lettre in liste_lettres:
			print("Déjà dit !")
			lettre="#"
	liste_lettres.append(lettre)
	if mot_final.count(lettre)>0:
		mot_en_cours=devoiler(lettre,mot_final,mot_en_cours)
		print("Bien joué ! Vous en êtes à : {0}. Lettres utilisées : {1}\n".format(mot_en_cours,liste_lettres))
	else:
		nbchances-=1
		print("Dommage :/\n")
		print("Il vous reste {0} chances. Lettres utilisées : {1}".format(nbchances, liste_lettres))

scores[nom]=scores[nom]+nbchances
if nbchances==0:
	print("C'est perdu... La réponse était {}".format(mot_final))
else:
	print("Félicitations ! Vous avez gagné {0} points, votre nouveau score est {1}".format(nbchances, scores[nom]))


with open('dico_scores', 'wb') as fichier:
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(scores)



os.system("pause")

