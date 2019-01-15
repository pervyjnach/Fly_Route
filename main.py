import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI import Test
from conv import Convertation
from great_circles import distance
import json


class Qwerty(QMainWindow):
	def __init__(self, parent=None):
		
		QWidget.__init__(self, parent)
		self.wpt_edit_value = 2
		self.qwerty()
		

	def qwerty(self):
		
		self.ui = Test()
		self.load_data()
		self.ui.wpt = self.wpt_edit_value
		self.ui.initUI()
		#self.ui.setWindowIcon(QIcon('map1.ico'))
		self.ui.btn_exit.clicked.connect(app.quit)
		self.ui.btn_processed.clicked.connect(self.getting_data)
		self.ui.btn_clear.clicked.connect(self.clear_data)
		self.ui.btn_set.clicked.connect(self.change_value)
		self.get_data = [[0 for i in range (0,6)] for j in range (self.ui.wpt)]
		self.get_data_text = [[str('') for i in range (0,6)] for j in range (self.ui.wpt)]
		self.home = [0 for i in range (6)]
		self.home_text = [str('') for i in range (6)]
		self.load_data_2()
		self.ui.show()
		
	def change_value(self):
		
		self.wpt_edit_value = int(self.ui.wpt_edit.text())
		self.getting_data()
		self.qwerty()
			
	def save_data(self): #Сохранение данных при выходе
		
		save_points = {'one' : self.get_data_text,
						'two' : self.home_text,
						'tree' : self.wpt_edit_value}
		
		savedata = open('wpt_data.txt', 'w')
		json.dump(save_points, savedata)

			

	def load_data(self):  #Загрузка данных из предыдущей сессии
		
		try: 
			loaddata = open('wpt_data.txt', 'r')

		except FileNotFoundError:
			pass

		else:
			self.load_points = json.load(loaddata)
			loaddata.close()
			self.load_data_route = self.load_points['one']
			self.load_data_home = self.load_points['two']
			self.wpt_edit_value = self.load_points['tree']
					
			

	def load_data_2(self):
		
		try: 
				loaddata = open('wpt_data.txt', 'r')
		except Exception:
			pass

		else:		
			for load_x_route in range (0,6):
				for load_y_route in range (self.ui.wpt):
					try:
						self.ui.line_data[load_x_route][load_y_route]\
						.setText(str(self.load_data_route[load_y_route][load_x_route]))

					except Exception:
						pass	

			for load_home in range (6):
				self.ui.main_point[load_home].setText(str(self.load_data_home[load_home]))		

	#=======================================================================================================================================================================	
	def load_data_alternative(self):  #Загрузка данных из предыдущей сессии
		
		
		try: 
			loaddata = open('wpt_data.txt', 'r')
		except FileNotFoundError:
			pass

		else:
			self.load_points = json.load(loaddata)
			loaddata.close()
			self.load_data_route = self.load_points[0]
			self.load_data_home = self.load_points[1]
			self.wpt_edit_value = self.load_points[2]
		print(self.load_data_route)
		print(self.load_data_home)
		print(self.wpt_edit_value)
		
	
		print('='*50)
		print('load_data_2()')
		print('заносим из памяти значения в таблицу')
		
		try: 
				loaddata = open('wpt_data.txt', 'r')
		except Exception:
			pass

		else:		
			for load_x_route in range (0,6):
				for load_y_route in range (self.ui.wpt):
					try:
						self.ui.line_data[load_x_route][load_y_route]\
						.setText(str(self.load_data_route[load_y_route][load_x_route]))

					except Exception:
						pass	

			for load_home in range (6):
				self.ui.main_point[load_home].setText(str(self.load_data_home[load_home]))					
	#=======================================================================================================================================================================

	def clear_data(self): #Очистка полей ввода от данных
		for clear_x in range (6):
			for clear_y in range(self.ui.wpt):
				self.ui.line_data[clear_x][clear_y].setText('')
		for clear_home in range (6):
			self.ui.main_point[clear_home].setText('')

	def getting_data(self):   #Перенос значений из полей ввода в переменные
		
		for get_x in range (0,6):
		 	for get_y in range(self.ui.wpt):
		 		if self.ui.line_data[get_x][get_y].text() == '':
		 			self.get_data_text[get_y][get_x] = str('')
		 			self.get_data[get_y][get_x] = str(0)
		 		else:
		 			self.get_data_text[get_y][get_x] = self.ui.line_data[get_x][get_y].text()
		 			self.get_data[get_y][get_x] = self.ui.line_data[get_x][get_y].text()

			
		for home_i in range (6):
			if self.ui.main_point[home_i].text() == '':
				self.home[home_i] = str(0)
				self.home_text[home_i] = str('')
			else:
				self.home_text[home_i] = self.ui.main_point[home_i].text()
				self.home[home_i] = self.ui.main_point[home_i].text()
		
		
		self.data_to_decimal_list()
	
	
			

	def deg_to_dec(self, gradus0, minuta0, secunda0, gradus1, minuta1, secunda1):   
		# Перевод градусов в десятичную форму
		secunda0 = str(secunda0.replace(',' ,'.'))
		secunda1 = str(secunda1.replace(',' ,'.'))
		d = [int(gradus0), int(minuta0), float(secunda0), int(gradus1), int(minuta1), float(secunda1)]
			
		self.convertat0 = Convertation(d[0], d[1], d[2])
		self.convertat1 = Convertation(d[3], d[4], d[5])
		return(self.convertat0.dtd(), self.convertat1.dtd())

	def data_to_decimal_list(self):  # Создаем массив хранения координат точек в десятичном формате 
									 # и заполняем десятичными данными							
		self.decimal = [[0 for dec_i in range(2)] for dec_j in range (self.ui.wpt)] 
															
		self.home_decimal = [0 for h_d in range(2)]  # Десятичный формат опорной точки
		self.home_decimal = self.deg_to_dec(self.home[0], self.home[1], self.home[2], self.home[3],\
			self.home[4], self.home[5])
		
		
		for dec_x in range(self.ui.wpt): # Заполнение массива self.decimal точками десятичного формата
			self.decimal[dec_x] = self.deg_to_dec(self.get_data[dec_x][0], self.get_data[dec_x][1],\
			 self.get_data[dec_x][2], self.get_data[dec_x][3], self.get_data[dec_x][4], self.get_data[dec_x][5])	
		
		self.calculate()
	
	def calculate(self):
		#дистанция, градусы
		
		#==== HOME ==============================

		self.home_to_11, self.home_to_12 =\
		 distance(self.home_decimal[0], self.home_decimal[1], self.decimal[0][0], self.decimal[0][1])
		
		self.one_to_home_11, self.one_to_home_12 =\
		 distance(self.decimal[0][0], self.decimal[0][1], self.home_decimal[0], self.home_decimal[1])
		
		self.ui.home_label[0].setText(str(self.home_to_12))
		self.ui.home_label[1].setText(str(self.one_to_home_12))
		self.ui.home_label[2].setText(str(self.one_to_home_11))
		self.ui.home_label[3].setText(str(self.home_to_11))
		
		#==== HOME ===============================

		#==== ROUTE ==============================
		for wpt_new in range(self.ui.wpt-1):
			x_end, y_end = distance(self.decimal[wpt_new][0], self.decimal[wpt_new][1], self.decimal[wpt_new+1][0], self.decimal[wpt_new+1][1])
			j_end, g_end = distance(self.decimal[wpt_new+1][0], self.decimal[wpt_new+1][1], self.home_decimal[0], self.home_decimal[1])
			self.ui.result_label[wpt_new][0].setText(str(y_end))
			self.ui.result_label[wpt_new][1].setText(str(g_end))
			self.ui.result_label[wpt_new][2].setText(str(j_end))
			self.ui.result_label[wpt_new][3].setText(str(x_end))

		
		#==== ROUTE ===
		#===========================
		self.save_data()


	
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	exr = Qwerty()
	sys.exit(app.exec_())

	

