class Domino:
	def __init__(self, face_a, face_b):
		white, double = self.white(face_a, face_b),self.double(face_a, face_b)
		self.state(white, double, face_a, face_b)
	def white(self, face_a, face_b):
		if face_a == 0 or face_b == 0:
			return True
	def double(self, face_a, face_b):
		if face_a == face_b:
			return True
	def state(self, white, double, face_a, face_b):
		if white and double:
			print("""Votre Domino : 
╔═════╗
║  {}  ║
║  -  ║
║  {}  ║
╚═════╝""".format(face_a, face_b),"""
est un double blanc""")
		elif white:
			print("""Votre Domino : 
╔═══════╗
║ {} - {} ║
╚═══════╝""".format(face_a, face_b),"""
possède un côté blanc""")
		elif double:
			print("""Votre Domino : 
╔═════╗
║  {}  ║
║  -  ║
║  {}  ║
╚═════╝""".format(face_a, face_b),"""
est un double""")
		else:
			print("""Votre Domino : 
╔═══════╗
║ {} - {} ║
╚═══════╝""".format(face_a, face_b),"""
n'est ni double et ne possède pas de blanc""")
		print("Sa valeur est de",str(face_a+face_b))
Domino(int(input("1re face du Domino : ")), int(input("2e face du Domino : ")))