from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
import Textruffie

font = QFont("Arial", 12)
font.setBold(True)


class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        v_box = QVBoxLayout()

        text1 = QLabel(Textruffie.txt_hello)
        text1.setFont(font)

        text2 = QLabel(Textruffie.txt_instruction)
        text2.setFont(font)

        self.btn_next = QPushButton("Start")
        v_box.addWidget(text1)
        v_box.addWidget(text2)
        v_box.addWidget(self.btn_next)
        self.setLayout(v_box)

    def connects(self):
        self.btn_next.clicked.connect(self.go_to_next_screen)

    def set_appear(self):
        self.setWindowTitle(Textruffie.txt_title)
        self.move(Textruffie.win_x, Textruffie.win_y)
        self.resize(Textruffie.win_width, Textruffie.win_height)

    def go_to_next_screen(self):
        self.hide()
        self.second_screen = SecondScreen()
        self.second_screen.show()


class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.time_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.initUI()
        self.connects()
        self.set_appear()

    def initUI(self):
        v_box = QVBoxLayout()

        label = QLabel(Textruffie.txt_name)
        label.setFont(font)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText(Textruffie.txt_hintname)

        label_age = QLabel(Textruffie.txt_age)
        label_age.setFont(font)
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Вік")

        instruction1 = QLabel(Textruffie.txt_test1)
        instruction1.setFont(font)

        self.btn_test1 = QPushButton(Textruffie.txt_starttest1)
        self.btn_test1.setFont(font)

        self.result_text1 = QLineEdit()
        self.result_text1.setPlaceholderText(Textruffie.txt_hinttest1)
        
        instruction2 = QLabel(Textruffie.txt_test2)
        instruction2.setFont(font)

        self.btn_test2 = QPushButton(Textruffie.txt_starttest2)
        self.btn_test2.setFont(font)

        self.result_text2 = QLineEdit()
        self.result_text2.setPlaceholderText(Textruffie.txt_hinttest2)

        instruction3 = QLabel(Textruffie.txt_test3)
        instruction3.setFont(font)

        self.btn_test3 = QPushButton(Textruffie.txt_starttest3)
        self.btn_test3.setFont(font)
        
        self.result_text3 = QLineEdit()
        self.result_text3.setPlaceholderText(Textruffie.txt_hinttest3)

        self.timer_label = QLabel("00:00:00")
        self.timer_label.setFont(QFont("Arial", 32))
        self.timer_label.setAlignment(Qt.AlignCenter)

        self.btn_next = QPushButton(Textruffie.txt_sendresults)

        v_box.addWidget(label)
        v_box.addWidget(self.name_input)

        v_box.addWidget(label_age)
        v_box.addWidget(self.age_input)

        v_box.addWidget(instruction1)
        v_box.addWidget(self.btn_test1)
        v_box.addWidget(self.result_text1)

        v_box.addWidget(instruction2)
        v_box.addWidget(self.btn_test2)
        v_box.addWidget(self.result_text2)

        v_box.addWidget(instruction3)
        v_box.addWidget(self.btn_test3)
        v_box.addWidget(self.result_text3)

        v_box.addWidget(self.timer_label)   

        v_box.addWidget(self.btn_next)

        self.setLayout(v_box)

    def connects(self):
        self.btn_test1.clicked.connect(self.start_first_test)
        self.btn_test2.clicked.connect(self.start_squats)
        self.btn_test3.clicked.connect(self.start_final_test)
        self.btn_next.clicked.connect(self.go_to_next_screen)

    def set_appear(self):
        self.setWindowTitle(Textruffie.txt_title)
        self.move(Textruffie.win_x, Textruffie.win_y)
        self.resize(Textruffie.win_width, Textruffie.win_height)

    def start_first_test(self):
        self.start_timer(15)

    def start_squats(self):
        self.start_timer(45)

    def start_final_test(self):
        self.start_timer(15)

    def start_timer(self, seconds):
        self.time_left = seconds
        self.update_timer_label()
        self.timer.start(1000)

    def update_timer(self):
        self.time_left -= 1
        self.update_timer_label()

        if self.time_left <= 0:
            self.timer.stop()

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.timer_label.setText(
            f"00:{minutes:02d}:{seconds:02d}"
        )
    def go_to_next_screen(self):
        self.hide()
        self.index = (4*(int(self.result_text1.text())+int(self.result_text2.text())+int(self.result_text3.text()))-200)/10
        self.third_screen = ThirdScreen(self.index, self.age_input)
        self.third_screen.show()

class ThirdScreen(QWidget):
    def __init__(self, index, age_input):
        super().__init__()

        self.index = index
        self.age_input = age_input

        self.initUI()

        self.set_appear()

    def initUI(self):
        v_box = QVBoxLayout()

        label = QLabel(Textruffie.txt_index + str(self.index))
        label.setFont(font)

        label2 = QLabel(Textruffie.txt_workheart + self.get_workheart())
        label2.setFont(font)

        v_box.addWidget(label)
        v_box.addWidget(label2)

        self.setLayout(v_box)

    def get_workheart(self):
        age = int(self.age_input.text())
        index = self.index

        if age >= 15:
            if index >= 15:
                return Textruffie.txt_res1
            elif index >= 11:
                return Textruffie.txt_res2
            elif index >= 6:
                return Textruffie.txt_res3
            elif index >= 0.5:
                return Textruffie.txt_res4
            else:
                return Textruffie.txt_res5

        elif age >= 13:
            if index >= 16.5:
                return Textruffie.txt_res1
            elif index >= 12.5:
                return Textruffie.txt_res2
            elif index >= 7.5:
                return Textruffie.txt_res3
            elif index >= 2:
                return Textruffie.txt_res4
            else:
                return Textruffie.txt_res5

        elif age >= 11:
            if index >= 18:
                return Textruffie.txt_res1
            elif index >= 14:
                return Textruffie.txt_res2
            elif index >= 9:
                return Textruffie.txt_res3
            elif index >= 3.5:
                return Textruffie.txt_res4
            else:
                return Textruffie.txt_res5

        elif age >= 9:
            if index >= 19.5:
                return Textruffie.txt_res1
            elif index >= 15.5:
                return Textruffie.txt_res2
            elif index >= 10.5:
                return Textruffie.txt_res3
            elif index >= 5:
                return Textruffie.txt_res4
            else:
                return Textruffie.txt_res5

        else:
            if index >= 21:
                return Textruffie.txt_res1
            elif index >= 17:
                return Textruffie.txt_res2
            elif index >= 12:
                return Textruffie.txt_res3
            elif index >= 6.5:
                return Textruffie.txt_res4
            else:
                return Textruffie.txt_res5

    def set_appear(self):    
        self.setWindowTitle(Textruffie.txt_title)
        self.move(Textruffie.win_x, Textruffie.win_y)
        self.resize(Textruffie.win_width, Textruffie.win_height)

app = QApplication([])
fs = FirstScreen()
app.exec()