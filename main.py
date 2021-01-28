# import sys
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication
# # 필요한 모듈들을 불러옵니다. 기본적인 UI 구성요소를 제공하는 위젯 (클래스)들은 PyQt5.QtWidgets 모듈에 포함되어 있습니다.
# # QtWidgets 모듈에 포함된 모든 클래스들과 이에 대한 자세한 설명은 QtWidgets 공식 문서에서 확인할 수 있습니다.
#
# class MyApp(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#
#
#     def initUI(self):
#         # Size controller
#         width = 1300
#         hight = 800
#
#         # Button controller
#
#         # btn quit
#         btn_quit = QPushButton('Quit', self)
#         btn_quit.move(width-150, 800-50)
#         btn_quit.resize(btn_quit.sizeHint())
#         btn_quit.clicked.connect(QCoreApplication.instance().quit)
#
#         # btn search
#         btn_search = QPushButton('search',self)
#         btn_search.move(50,50)
#         btn_search.resize(btn_search.sizeHint())
#
#         # Window controller
#         self.setWindowTitle('HuminTec')
#         self.setWindowIcon(QIcon('H_icon.png'))
#         self.setGeometry(200, 200, width, hight)
#         self.show()
#
#         # StatusBar controller
#         self.statusBar().showMessage('ready')
#
#
# if __name__ == '__main__':
#     # '__name__'은 현재 모듈의 이름이 저장되는 내장 변수입니다.
#     # 만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 __name__ 은 'moduleA'가 됩니다.
#     # 그렇지 않고 코드를 직접 실행한다면 __name__ 은 __main__ 이 됩니다.
#     # 따라서 이 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인합니다.
#
#     # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
#     # QApplication 클래스에 대한 자세한 설명은 QApplication 공식 문서에서 확인할 수 있습니다
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("C:\\Users\\broth\\Desktop\\RecommendationSystemInHumintec\\HuminTec_GUI.ui")
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())


# https://github.com/metalnom/Python_NLPProject
# https://m.blog.naver.com/PostView.nhn?blogId=metalnonn&logNo=221917005927&targetKeyword=&targetRecommendationCode=1
