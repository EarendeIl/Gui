import sys
import subprocess
import re
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory Usage Trend')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.canvas1 = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas1.axes.set_title('MEM (MB)')
        self.canvas1.axes.set_xlabel('Time (m:ss)')
        self.canvas1.axes.set_ylabel('MEM (MB)')
        layout.addWidget(self.canvas1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.data = []
        self.timestamps = []
        self.start_time = time.time()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update every 1 second (1000 ms)

    def update_plot(self):
        mem_usage = self.get_memory_usage()
        if mem_usage is not None:
            self.data.append(mem_usage)
            print(self.data)

            self.timestamps.append(time.time() - self.start_time)

            if len(self.data) > 1:
                # Skip the first data point
                plot_data = self.data[1:]
                plot_timestamps = self.timestamps[1:]
            else:
                plot_data = self.data
                plot_timestamps = self.timestamps

            self.canvas1.axes.clear()  # Clear the previous plot and axis settings

            self.canvas1.axes.plot(plot_timestamps, plot_data, label='Memory Usage')
            self.canvas1.axes.legend()

            # Limit the number of ticks to 5
            max_ticks = 5
            if len(plot_timestamps) > max_ticks:
                step = len(plot_timestamps) // max_ticks
                x_ticks = plot_timestamps[::step]
                x_labels = ['{:d}:{:02}'.format(int(t // 60), int(t % 60)) for t in x_ticks]
            else:
                x_ticks = plot_timestamps
                x_labels = ['{:d}:{:02}'.format(int(t // 60), int(t % 60)) for t in plot_timestamps]

            self.canvas1.axes.set_xticks(x_ticks)  # Set limited tick positions
            self.canvas1.axes.set_xticklabels(x_labels)  # Set limited tick labels

            self.canvas1.axes.set_title('MEM (MB)')
            self.canvas1.axes.set_xlabel('Time (m:ss)')
            self.canvas1.axes.set_ylabel('MEM (MB)')
            self.canvas1.draw()

    def get_memory_usage(self):
        try:
            result = subprocess.run(['adb', 'shell', 'dumpsys', 'meminfo', 'com.tencent.wecarnavi'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                match = re.search(r'TOTAL\s+(\d+)', result.stdout)
                if match:
                    return int(match.group(1)) / 1024  # Convert to MB
            return None
        except Exception as e:
            print(f"Error fetching memory usage: {e}")
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
