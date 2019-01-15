#Класс, конвертирующий классический формат координат в десятичный

class Convertation:
	def __init__(self, degrees, minutes, seconds):
		self.degrees = degrees
		self.minutes = minutes
		self.seconds = seconds
		
	def dtd(self):
		if self.degrees >= 0:
			self.digit = (self.seconds/3600) + (self.minutes/60) + self.degrees
		else:
			self.digit = self.degrees - (self.seconds/3600) - (self.minutes/60) 	
		#Возврат результата в десятичном формате
		
		return self.digit
	
	def show(self):
		print (self.digit)
		
class EditFile:
	def file(self):
		self.filename = input("Enter filename: ")
				
	def write(self):
		self.textfile = open(self.filename, 'a')
		self.textfile.write('123')
		self.textfile.close()
		
	def trunc(self):
		self.textfile = open(self.filename, 'w')
		self.textfile.close
		
	def show(self):
		return self.filename

#conv = Convertation(52, 32, 56.135)
#conv.dtd()
#conv.show()		

		
		
	
