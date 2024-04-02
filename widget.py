# This Python file uses the following encoding: utf-8


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from ui_form import Ui_Widget
from ui_config import Ui_Form
import sys
import subprocess
import configparser

class ConfigDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.load_settings()

        # Добавляем слот к кнопке "Сохранить"
        self.ui.pushButton.clicked.connect(self.save_settings)

    def load_settings(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Получаем настройки из конфига
        api_key = config.get('API', 'api_key')
        api_key2 = config.get('API', 'api_key2')
        api_key3 = config.get('API', 'api_key3')
        api_key4 = config.get('API', 'api_key4')
        api_key5 = config.get('API', 'api_key5')

        api_key_midjourney = config.get('API', 'api_key_midjourney')
        api_key_midjourney2 = config.get('API', 'api_key_midjourney2')
        api_key_midjourney3 = config.get('API', 'api_key_midjourney3')
        api_key_midjourney4 = config.get('API', 'api_key_midjourney4')
        api_key_midjourney5 = config.get('API', 'api_key_midjourney5')
        api_key_midjourney6 = config.get('API', 'api_key_midjourney6')
        api_key_midjourney7 = config.get('API', 'api_key_midjourney7')
        api_key_midjourney8 = config.get('API', 'api_key_midjourney8')
        api_key_midjourney9 = config.get('API', 'api_key_midjourney9')
        api_key_midjourney10 = config.get('API', 'api_key_midjourney10')

        promt = config.get('API', 'promt')
        max_attempts = config.get('API', 'max_attempts')
        detail = config.get('API', 'detail')
        model = config.get('API', 'model')
        temp = config.get('API', 'temp')
        max_tokens = config.get('API', 'max_tokens')

        # Отображаем настройки в Line Edit
        self.ui.lineEdit.setText(api_key)
        self.ui.lineEdit_2.setText(api_key2)
        self.ui.lineEdit_9.setText(api_key3)
        self.ui.lineEdit_10.setText(api_key4)
        self.ui.lineEdit_11.setText(api_key5)
        self.ui.lineEdit_12.setText(api_key_midjourney)
        self.ui.lineEdit_13.setText(api_key_midjourney2)
        self.ui.lineEdit_14.setText(api_key_midjourney3)
        self.ui.lineEdit_15.setText(api_key_midjourney4)
        self.ui.lineEdit_16.setText(api_key_midjourney5)
        self.ui.lineEdit_17.setText(api_key_midjourney6)
        self.ui.lineEdit_18.setText(api_key_midjourney7)
        self.ui.lineEdit_19.setText(api_key_midjourney8)
        self.ui.lineEdit_20.setText(api_key_midjourney9)
        self.ui.lineEdit_21.setText(api_key_midjourney10)
        self.ui.lineEdit_22.setText(promt)
        self.ui.lineEdit_3.setText(detail)
        self.ui.lineEdit_4.setText(model)
        self.ui.lineEdit_5.setText(temp)
        self.ui.lineEdit_6.setText(max_tokens)
        self.ui.lineEdit_8.setText(max_attempts)

    def save_settings(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Получаем значения из полей Line Edit
        api_key = self.ui.lineEdit.text()
        api_key2 = self.ui.lineEdit_2.text()
        api_key3 = self.ui.lineEdit_9.text()
        api_key4 = self.ui.lineEdit_10.text()
        api_key5 = self.ui.lineEdit_11.text()

        api_key_midjourney = self.ui.lineEdit_12.text()
        api_key_midjourney2 = self.ui.lineEdit_13.text()
        api_key_midjourney3 = self.ui.lineEdit_14.text()
        api_key_midjourney4 = self.ui.lineEdit_15.text()
        api_key_midjourney5 = self.ui.lineEdit_16.text()
        api_key_midjourney6 = self.ui.lineEdit_17.text()
        api_key_midjourney7 = self.ui.lineEdit_18.text()
        api_key_midjourney8 = self.ui.lineEdit_19.text()
        api_key_midjourney9 = self.ui.lineEdit_20.text()
        api_key_midjourney10 = self.ui.lineEdit_21.text()

        promt = self.ui.lineEdit_22.text()

        max_attempts = self.ui.lineEdit_8.text()
        detail = self.ui.lineEdit_3.text()
        model = self.ui.lineEdit_4.text()
        temp = self.ui.lineEdit_5.text()
        max_tokens = self.ui.lineEdit_6.text()

        # Записываем значения в конфиг
        config.set('API', 'api_key', api_key)
        config.set('API', 'api_key2', api_key2)
        config.set('API', 'api_key3', api_key3)
        config.set('API', 'api_key4', api_key4)
        config.set('API', 'api_key5', api_key5)
        config.set('API', 'api_key_midjourney', api_key_midjourney)
        config.set('API', 'api_key_midjourney2', api_key_midjourney2)
        config.set('API', 'api_key_midjourney3', api_key_midjourney3)
        config.set('API', 'api_key_midjourney4', api_key_midjourney4)
        config.set('API', 'api_key_midjourney5', api_key_midjourney5)
        config.set('API', 'api_key_midjourney6', api_key_midjourney6)
        config.set('API', 'api_key_midjourney7', api_key_midjourney7)
        config.set('API', 'api_key_midjourney8', api_key_midjourney8)
        config.set('API', 'api_key_midjourney9', api_key_midjourney9)
        config.set('API', 'api_key_midjourney10', api_key_midjourney10)

        config.set('API', 'promt', promt)
        config.set('API', 'max_attempts', max_attempts)
        config.set('API', 'detail', detail)
        config.set('API', 'model', model)
        config.set('API', 'temp', temp)
        config.set('API', 'max_tokens', max_tokens)

        # Сохраняем изменения в файл
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # Добавляем слоты к кнопкам
        self.ui.pushButton.clicked.connect(self.on_config_button_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_start_button_clicked)
        self.config_dialog = ConfigDialog()  # Создаем экземпляр диалогового окна

    # Слоты для каждой кнопки
    def on_config_button_clicked(self):
        self.config_dialog.setWindowTitle("Настройки")
        self.config_dialog.show()  # Показываем диалоговое окно

    def on_start_button_clicked(self):
        subprocess.Popen(["python", "main.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Главное меню")
    sys.exit(app.exec())
