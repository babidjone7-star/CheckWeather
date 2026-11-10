import sys
from PySide6.QtWidgets import QApplication, QDialog, QWidget
from PySide6.QtGui import QPixmap
from weather_app_design import Ui_Dialog
import requests

class App(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Погода")
        self.ui.FindWeather.clicked.connect(self.Find)
    def Find(self):
      try:
         self.inptext = self.ui.Town.text()
         self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.inptext}&appid=__ваш_ключ__"
         if not self.inptext:
            self.ui.TempLbl.setText("Пожалуйста введите город...")
            return
         self.resp = requests.get(self.url)
         self.data = self.resp.json()
         self.ui.TempLbl.setText(f"Temperature: {round(self.data['main']['temp'])}")
         self.decs = self.data['weather'][0]['description'].capitalize()
         self.ui.OpisWeth.setText(f"Описание погоды: {self.decs}")
         self.icn = self.data['weather'][0]['icon']
         self.icnurl = "https://openweathermap.org/img/wn/04n@2x.png"
         self.resp = requests.get(self.icnurl).content
         self.pixm = QPixmap()
         self.pixm.loadFromData(self.resp)
         self.ui.Icn.setPixmap(self.pixm)
      except Exception as e:
         self.ui.TempLbl.setText("Нет интернета(или вы написали не то)")
         return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Windw = App()
    Windw.show()
    sys.exit(app.exec())