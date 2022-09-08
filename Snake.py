from tkinter import *
from random import randint

hauteur,largeur=300,300
offset=2

#direction de la tête du serpent
class direc:
	def __init__(self,coox,cooy):
		self.x=coox
		self.y=cooy

def left(event):
	if direction.x!=1:
		direction.x=-1
		direction.y=0

def right(event):
	if direction.x!=-1:
		direction.x=1
		direction.y=0

def up(event):
	if direction.y!=1:
		direction.x=0
		direction.y=-1

def down(event):
	if direction.y!=-1:
		direction.x=0
		direction.y=1

#chaque carré (anneau) du serpent
class anneau:
	
	def __init__(self,coox,cooy):
		self.x=coox
		self.y=cooy
		self.retard=0

	def afficher(self,couleur):
		x=self.x
		y=self.y
		a=x*cote+offset
		b=y*cote+offset
		c=x*cote+cote+offset
		d=y*cote+cote+offset
		Canevas.create_rectangle(a,b,c,d,outline=couleur,fill=couleur)

#le carré rouge que le serpent doit manger
class nourriture:
	def __init__(self,coox,cooy):
		self.x=coox
		self.y=cooy

	def afficher(self):
		x=self.x
		y=self.y
		a=x*cote+offset
		b=y*cote+offset
		c=x*cote+cote+offset
		d=y*cote+cote+offset
		Canevas.create_rectangle(a,b,c,d,outline='black',)


def avancer():
	Canevas.delete(ALL)
	oeuf.afficher()#affiche la nourriture
	for morceau in range(len(serpent)): #affiche chaque anneau du serpent
		if morceau==0:
			serpent[0].afficher('red')
		else:
			if serpent[morceau].retard==0:
				serpent[morceau].afficher('green')
			else:
				serpent[len(serpent) - serpent[morceau].retard].afficher('black')


def directionvers(event):
	print(event.char)

def main():
	#chaque morceau prend la place du précédent en prenant la même direction
	for morceau in range(len(serpent)-1,0,-1):
		serpent[morceau].x=serpent[morceau-1].x
		serpent[morceau].y=serpent[morceau-1].y
		if serpent[morceau].retard>0:
			serpent[morceau].retard-=1
	#la tête avance selon "direction"
	serpent[0].x+=direction.x
	serpent[0].y+=direction.y
	#print([(i.x,i.y) for i in serpent])

	x=serpent[0].x
	y=serpent[0].y

	#toucher les bords
	if x<0 or x>largeur//cote-1 or y<0 or y>hauteur//cote-1:
		print("Score : "+str(len(serpent)))
		fenetre.destroy()
		return True

	#manger un oeuf
	if x==oeuf.x and y==oeuf.y:
		nouveau=anneau(serpent[-1].x,serpent[-1].y)
		nouveau.retard=len(serpent)
		serpent.append(nouveau)
		oeuf.x=randint(0,largeur//cote-1)
		oeuf.y=randint(0,hauteur//cote-1)

	#quand on touche un de ses anneaux
	for morceau in range(1,len(serpent)):
		if serpent[morceau].retard>0:#pas si c'est l'anneau de fin avec du retard (avant qu'on l'affiche)
			break
		elif x==serpent[morceau].x and y==serpent[morceau].y:
			print("Score : "+str(len(serpent)))
			fenetre.destroy()
			return True

	avancer()
	fenetre.after(70,main)


cote=10
direction=direc(1,0)
oeuf=nourriture(8,1)
serpent=[anneau(3,1),anneau(2,1),anneau(1,1)] #la tête du serpent est serpent[0]



fenetre=Tk()
fenetre.title("")
#fenetre.focus_force()

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack()


fenetre.bind("<Left>",left)
fenetre.bind("<Right>",right)
fenetre.bind("<Up>",up)
fenetre.bind("<Down>",down)

fin=False
fin=main()


# if a==0:
# 	fenetre.stop()
# 	print(a)

fenetre.mainloop()