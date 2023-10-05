from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5.uic import loadUi
from detection_window import DetectionWindow

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow,self).__init__()
        loadUi('UI/settingsWindow.ui',self)
        self.detection_window = DetectionWindow()
        self.pushButton.clicked.connect(self.go_to_detection)
    
    def displayinfo(self):
        self.show()

    def go_to_detection(self):
        if self.detection_window.isVisible():
           print('Detection Window is already open!')
        else:
            self.detection_window.create_detection_instance()
            self.detection_window.start_detection()
    def closeEvent(self,event):
        if self.detection_window.isVisible():
            self.detection_window.detection.running = False
            self.detection_window.close()
            event.accept()

