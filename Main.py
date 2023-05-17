from XGui import XGui
from PySide6.QtWidgets import QApplication

from kant.OneKant import OneKant


class OneBis(OneKant):
    def __init__(self):
        OneKant.__init__(self)

    def register_func(self,job_id, js):
        print(job_id, js)

class Main(XGui):
    def __init__(self):
        XGui.__init__(self)

    def base(self):
        pass

    def utils(self):
        pass

    def bis(self):
        self.onebis = OneBis()

    def register_thead(self):
        self.onebis.run(self.get_god)


if __name__ == '__main__':
    app = QApplication()
    widget = Main()
    widget.show()
    app.exec()
