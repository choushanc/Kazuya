from XActivity import XActivity
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

from threading import Thread

from xtask.XTask import taskmanage


class XGui(QWidget, XActivity):
    def __init__(self):
        super().__init__()
        XActivity.__init__(self)
        self.god = False
        self.setFixedSize(400, 300)
        self.play = QPushButton("开始")
        self.stop = QPushButton("结束")
        self.play.setEnabled(not self.god)
        self.stop.setEnabled(self.god)
        layout = QVBoxLayout()
        layout.addWidget(self.play)
        layout.addWidget(self.stop)
        self.setLayout(layout)
        self.play.clicked.connect(self.on_play_click)
        self.stop.clicked.connect(self.on_stop_click)

    def __clicked_before(self):
        self.god = not self.god
        self.play.setEnabled(False)
        self.stop.setEnabled(False)

    def __clicked_after(self):
        self.play.setEnabled(not self.god)
        self.stop.setEnabled(self.god)

    def on_play_click(self):
        self.__clicked_before()
        Thread(target=self.register_thead).start()
        self.__clicked_after()

    def on_stop_click(self):
        self.__clicked_before()
        Thread(target=taskmanage.safe_out, args=(self.__clicked_after,)).start()

    def get_god(self) -> bool:
        return self.god

    def register_thead(self):
        pass
