import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('趋势变化图表')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.canvas1 = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas1.axes.plot([0, 1, 2, 3], [10, 1, 20, 3])
        self.canvas1.axes.set_title('MEM (MB)')
        self.canvas1.axes.set_xlabel('Time')
        self.canvas1.axes.set_ylabel('MEM (MB)')
        self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas2.axes.plot([0, 1, 2, 3], [30, 40, 50, 60])
        self.canvas2.axes.set_title('CPU (%)')
        self.canvas2.axes.set_xlabel('Time')
        self.canvas2.axes.set_ylabel('CPU (%)')

        layout.addWidget(self.canvas1)
        layout.addWidget(self.canvas2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # self.plot_initial_data()

    # def plot_initial_data(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
