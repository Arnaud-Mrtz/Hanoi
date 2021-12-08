class Domino:

	def __init__(self, face_a, face_b):
		print("Votre Domino : [{}-{}]".format(face_a, face_b))
		self.val_a, self.val_b = int(face_a), int(face_b)
	def white(self, val_a, val_b):
		if self.val_a == 0 or self.val_b == 0:
			self.white = True
	def double(self, val_a, val_b):
		if self.val_a == self.val_b:
			self.double = True
	def state(self, white, double):
		print("Votre Domino : [{}-{}]".format(face_a, face_b))
		if white and double:
			print("""	est double blanc""")
		elif white:
			print("""	est blanc""")
		elif double:
			print("""	est double""")
		else:
			print("""	n'est ni double ni blanc""")


face_a = str(input("1re face du Domino : "))
face_b = str(input("2e face du Domino : "))