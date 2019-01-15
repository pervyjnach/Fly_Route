import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Test(QWidget):
	wpt = 54
	def __init__(self):
		super().__init__()
		

		
	def initUI(self): #РАСПОЛОЖЕНИЕ ВИДЖЕТОВ
		
		self.setGeometry(50,50,650,350 + 55*self.wpt )
		self.setFixedWidth(600)
		self.setMaximumHeight(800)
		

		self.setWindowTitle('Fly Route v.1.0')
		self.setWindowIcon(QIcon('C:\Project\map1.ico'))
		
		#self.adjustSize()
		

		self.objects()
		self.how_many()
		self.show()



	def	how_many(self):
		for waypoint_main in range (self.wpt):
			self.my_grid_move(waypoint_main)



	def my_grid_move(self, waypoint):
		way = waypoint 
		x = 20
		y_label = 225+30*waypoint
		y_edit = 223+30*waypoint
		self.num_label[way].move(x,y_label)
		self.line_data[0][way].move(x+30,y_edit)
		self.line_data[1][way].move(x+90,y_edit)
		self.line_data[2][way].move(x+150,y_edit)
		self.line_data[3][way].move(x+240,y_edit)
		self.line_data[4][way].move(x+300,y_edit)
		self.line_data[5][way].move(x+360,y_edit)
		self.end_label_widget.move(x-10, y_edit+80)

		
	

	def	objects(self):  #СОЗДАНИЕ ВИДЖЕТОВ
		self.w = QWidget()




#============================================РЕЗУЛЬТАТ============
		self.wpt_edit = QSpinBox(self.w)
		self.wpt_edit.move(440,50)
		self.wpt_edit.setFont(QFont('TimesNewRoman', 11))
		self.wpt_edit.resize(50,25)
		self.wpt_edit.setMinimum(1)
		self.wpt_edit.setValue(self.wpt)
		
		
		self.end_label_widget = QWidget(self.w) # Создали виджет, для помещения туда сетки
		self.end_label_widget.resize(470, 100 + 25*self.wpt)

		self.end_label_grid = QGridLayout(self.w) #Создание сетки

		self.end_label = [] # Нумерация точек маршрута (результат)
		self.end_label_top = []
		for i_top in range (4):
			self.end_label_top.append(i_top)
			self.end_label_top[i_top] = QLabel('1', self.w)
			self.end_label_top[i_top].setFont(QFont('TimesNewRoman', 11))
			self.end_label_grid.addWidget(self.end_label_top[i_top], 0, i_top+1)
		self.end_label_top[0].setText('Курс')
		self.end_label_top[0].setToolTip('Азимут на точку маршрута')
		self.end_label_top[1].setText('Пеленг')
		self.end_label_top[1].setToolTip('Азимут на опорную точку')
		self.end_label_top[2].setText('Удаление')
		self.end_label_top[2].setToolTip('Удаление от опорной точки,\nкм')
		self.end_label_top[3].setToolTip('Дистанция отрезка,\nкм')
		self.end_label_top[3].setText('Дистанция')



		for i_label in range (self.wpt):
			self.end_label.append(i_label)
			self.end_label[i_label] = QLabel(str(i_label+1), self.w)
			self.end_label[i_label].setFont(QFont('TimesNewRoman', 11))
			self.end_label_grid.addWidget(self.end_label[i_label], i_label+1, 0)

		self.end_label_widget.setLayout(self.end_label_grid) #Размещение сетки в виджете

		self.home_label = [None,None,None,None] # размещение первой строки таблицы в сетке
		for h_l in range (4):
			self.home_label[h_l] = QLabel('', self.w)
			self.home_label[h_l].setFont(QFont('TimesNewRoman', 11))
			self.end_label_grid.addWidget(self.home_label[h_l], 1, h_l+1)


		self.result_label = [[None for res_x in range(4)] for res_y in range (self.wpt)]
		for  i_res in range (4):
			for j_res in range (self.wpt):	
				self.result_label[j_res][i_res] = QLabel('', self.w)
				self.result_label[j_res][i_res].setFont(QFont('TimesNewRoman', 11))
				self.end_label_grid.addWidget(self.result_label[j_res][i_res], j_res+2, i_res+1)	


#============================================РЕЗУЛЬТАТ============
		
		self.main_label = QLabel(self.w)
		self.main_label.setFont(QFont('TimesNewRoman', 11))
		self.main_label.move(20, 25)
		self.main_label.setText('\
Расчет навигационных данных для отработки полета по\n\
маршруту, с использованием дальномера и радиомаяка.')

		dx, dy = (6,self.wpt) # dx - столбцы, dy - строки
		
		self.line_data = [[0 for i in range (dy)] for j in range (dx)]  #поля ввода координат
		

		for line_y in range (self.wpt):  # Ввод координат (ПОЛЯ ВВОДА)
			for line_x in range(6):
				self.line_data[line_x][line_y] = QLineEdit('', self.w)  # Ввод координат
				self.line_data[line_x][line_y].setFont(QFont('TimesNewRoman', 11))
				self.line_data[line_x][line_y].resize(55,20)
				

		for line_int in range(self.wpt):
			self.line_data[0][line_int].setValidator(QIntValidator())
			self.line_data[0][line_int].setMaxLength(4)
			self.line_data[3][line_int].setValidator(QIntValidator())
			self.line_data[3][line_int].setMaxLength(4)

			self.line_data[1][line_int].setValidator(QIntValidator())
			self.line_data[1][line_int].setMaxLength(2)
			self.line_data[4][line_int].setValidator(QIntValidator())
			self.line_data[4][line_int].setMaxLength(2)	
			
			self.line_data[2][line_int].setValidator(QDoubleValidator())
			self.line_data[2][line_int].setMaxLength(6)
			self.line_data[5][line_int].setValidator(QDoubleValidator())
			self.line_data[5][line_int].setMaxLength(6)



				
		self.num_label = []			  # Нумерация точек маршрута	(ТЕКСТ)			
		for n_l in range (self.wpt):
			self.num_label.append(n_l)
			self.num_label[n_l] = QLabel(str(n_l+1)+'.', self.w)
			self.num_label[n_l].setFont(QFont('TimesNewRoman', 11))  
			

	
		self.degrees_label = []
		for deg_lab in range (8):
			self.degrees_label.append(deg_lab)
			self.degrees_label[deg_lab] = QLabel(self.w)
			self.degrees_label[deg_lab].setFont(QFont('TimesNewRoman', 11))

		#text = 'Количество точек'
		#self.main_label = QLabel(text, self.w)
		#self.main_label.setFont(QFont('TimesNewRoman', 12))
		#self.main_label.move(440,25)

		self.main_point = []

		for m_p in range (6):
			self.main_point.append(m_p)
			self.main_point[m_p] = QLineEdit('', self.w)
			self.main_point[m_p].setFont(QFont('TimesNewRoman', 11))
			self.main_point[m_p].resize(55,20)

		mp_y = 155
		self.main_point[0].move(50,mp_y)
		self.main_point[0].setValidator(QIntValidator())
		self.main_point[0].setMaxLength(4)
		self.main_point[1].move(50+60,mp_y)
		self.main_point[1].setValidator(QIntValidator())
		self.main_point[1].setMaxLength(2)
		self.main_point[2].move(50+60*2,mp_y)
		self.main_point[2].setValidator(QDoubleValidator())
		self.main_point[2].setMaxLength(6)
		self.main_point[3].move(260,mp_y)
		self.main_point[3].setValidator(QIntValidator())
		self.main_point[3].setMaxLength(4)
		self.main_point[4].move(260+60,mp_y)
		self.main_point[4].setValidator(QIntValidator())
		self.main_point[4].setMaxLength(2)
		self.main_point[5].move(260+60*2,mp_y)
		self.main_point[5].setValidator(QDoubleValidator())
		self.main_point[5].setMaxLength(6)
		
		self.degrees_label[0].setText('Широта')	
		self.degrees_label[1].setText('Долгота')
		self.degrees_label[2].setText('Град.')
		self.degrees_label[3].setText('Мин.')
		self.degrees_label[4].setText('Сек.')
		self.degrees_label[5].setText('Град.')
		self.degrees_label[6].setText('Мин.')
		self.degrees_label[7].setText('Сек.')
		# КНОПКИ====================================================		
		self.btn_exit = QPushButton('Выход', self.w)
		self.btn_exit.move(500, 311)
		self.btn_exit.setFont(QFont('TimesNewRoman'))
		self.btn_processed = QPushButton('Расчет',self.w)
		self.btn_processed.move(500,220)
		self.btn_processed.setFont(QFont('TimesNewRoman'))
		self.btn_clear = QPushButton('Очистить', self.w)
		self.btn_clear.move(500,250)
		self.btn_clear.setFont(QFont('TimesNewRoman'))
		self.btn_set = QPushButton('Установить', self.w)
		self.btn_set.move(500,50)
		self.btn_set.setFont(QFont('TimesNewRoman'))
		
		#self.btn_processed.clicked.connect(None)
		# КНОПКИ====================================================
		self.vbox = QVBoxLayout(self.w)
		self.vbox.addWidget(self.wpt_edit)
		self.vbox.addWidget(self.btn_set)


		self.group = QGroupBox('Количество точек', self.w)
		self.group.resize(120,100)
		self.group.setFont(QFont('TimesNewRoman', 10))
		self.group.move(460,25)
		self.group.setLayout(self.vbox)




		self.degrees_label[0].resize(100,50)
		self.degrees_label[0].setFont(QFont('TimesNewRoman', 14))
		self.degrees_label[0].move(101,80)

		self.degrees_label[1].resize(100,50)
		self.degrees_label[1].setFont(QFont('TimesNewRoman', 14))
		self.degrees_label[1].move(310,80)

		self.degrees_label[2].move(60, 125)
		self.degrees_label[5].move(270, 125)
		self.degrees_label[3].move(122, 125)
		self.degrees_label[6].move(332, 125)
		self.degrees_label[4].move(390, 125)
		self.degrees_label[7].move(180, 125)

		self.opornaja_tochka = QLabel('Опорная точка',self.w) 
		self.marshrut = QLabel ('Маршрут', self.w)
		self.opornaja_tochka.setFont(QFont('TimesNewRoman', 11))
		self.marshrut.setFont(QFont('TimesNewRoman', 11))
		self.opornaja_tochka.move(470,155)
		self.marshrut.move(210,190)

		self.w.setGeometry(0,0,580,345+55*self.wpt)
		self.vbox_2 =QVBoxLayout(self)
		self.area = QScrollArea(self)
		self.area.setWidget(self.w)
		self.vbox_2.addWidget(self.area)
		self.vbox_2.setContentsMargins(0,0,0,0)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Test()
	ex.initUI()
	



	sys.exit(app.exec_())
	
