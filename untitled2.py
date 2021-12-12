class Domino:
	def __init__(self, face_a, face_b): #On récupère deux valeurs (celles des deux faces du domino)
		white, double = self.white(face_a, face_b),self.double(face_a, face_b) #On appelle deux fonctions de la classe avec les valeurs des faces, puis on donne les valeurs retournées à deux variables
		self.state(white, double, face_a, face_b) #Avec ces deux variables on appelle une derniere fonction qui donnera l'état du domino, y compris celui donné par les deux fonctions précédents grâce aux deux variables
	def white(self, face_a, face_b): #La première fonction cherche si l'une des deux faces (a ou b) est égale à , si c'est le cas elle retourne True
		if face_a == 0 or face_b == 0:
			return True
	def double(self, face_a, face_b):#La seconde fonction cherche si les deux faces (a et b) sont égales l'une à l'autre, si c'est le cas elle retourne True
		if face_a == face_b:
			return True
	def state(self, white, double, face_a, face_b): #4 états différents sont recherchés avec les valeurs retournées des deux fonctions précédentes :
		if white and double: # Si le domino comporte au moins une face égale à 0 et que les deux faces sont égales (donc égales à 0)
			print("""Votre Domino : 
╔═════╗
║  {}  ║
║  -  ║
║  {}  ║
╚═════╝""".format(face_a, face_b),"""
est un double blanc""")
		elif white:# Si le domino comporte seulement au moins une face égale à 0 et que les deux faces ne sont égales
			print("""Votre Domino : 
╔═══════╗
║ {} - {} ║
╚═══════╝""".format(face_a, face_b),"""
possède un côté blanc""")
		elif double:# Si le domino ne comporte pas de face égale à 0 mais que les deux faces sont égales
			print("""Votre Domino : 
╔═════╗
║  {}  ║
║  -  ║
║  {}  ║
╚═════╝""".format(face_a, face_b),"""
est un double""")
		else: #Enfin le dernier cas possible (donc juste else) s'il n'a ni coté égal à 0 et n'a pas de valeurs égales.  
			print("""Votre Domino : 
╔═══════╗
║ {} - {} ║
╚═══════╝""".format(face_a, face_b),""" 
n'est ni double et ne possède pas de blanc""") #Pour l'affichage, on utilise les """ pour afficher plusieurs lignes, le .format permet de remplacer des {} par des variables. 
		print("Sa valeur est de",str(face_a+face_b)) #Enfin on affiche la valeur du domino (la somme des deux faces).
Domino(int(input("1re face du Domino : ")), int(input("2e face du Domino : "))) #On appelle la classe (qui appelle elle-ême ses fonctions) avec les valeurs de deux imputs mise au format d'entier.