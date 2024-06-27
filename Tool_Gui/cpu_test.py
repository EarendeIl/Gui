# import os
# import time
# import re
#
#
# def get_cpu(pid):
#     try:
#         cmd = 'adb shell "cat /proc/stat | grep ^cpu"'
#         cmd1 = f'adb shell cat /proc/{pid}/stat'
#         redcmd = str(os.popen(cmd).readlines()).replace("'", "").replace("\n", " ").replace("]", " ").replace("[", " ")
#         redcmd = [i for i in redcmd.split(",")[0].split(" ") if i != '']
#         # 去掉首行CPU
#         redcmd.remove(redcmd[0])
#         # 去掉后三行不需要的数据
#         del redcmd[-3:]
#         # 将剩余的元素转化为列表并相加
#         total_cpu = sum(list(map(int, redcmd)))
#         # 获取cpu空闲时间
#         idle = redcmd[3]
#         redcmd1 = str(os.popen(cmd1).readlines()).replace("'", "").replace("\n", " ").replace("]", " ").replace("[",
#                                                                                                                 " ").split(
#             " ")[14:18]
#         pjiff = sum(list(map(int, redcmd1)))
#         return [total_cpu, idle, pjiff]
#     except Exception as e:
#         print(e, "get_s_cpu(),检查adb是否连通……")
#         # return [-1, -1, -1]
#
#
# def calculate_cpu_usage(pid):
#     total_cpu1, idle1, pjiff1 = get_cpu(pid)
#     while True:
#         time.sleep(2)
#         total_cpu2, idle2, pjiff2 = get_cpu(pid)
#         pcpu = 100.0 * (int(pjiff2) - int(pjiff1)) / (int(total_cpu2) - int(total_cpu1))  # process cpu
#         # system_cpu = 100.0 * ((int(total_cpu2) - int(idle2)) - (int(total_cpu1) - int(idle1))) / (
#         #         int(total_cpu2) - int(total_cpu1))  # system cpu
#         total_cpu1, idle1, pjiff1 = total_cpu2, idle2, pjiff2
#         print(f"Process CPU Usage: {pcpu:.2f}%")
#         # print(f"System CPU Usage: {system_cpu:.2f}%")
#
#
# if __name__ == '__main__':
#     pid = 3276
#     calculate_cpu_usage(pid)
# print('{:d}'.format(int(1.5059475898742676 % 60)))
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import time


class LiveTimePlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Live Time Plot')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')

        self.times = []
        self.values = []

        self.line, = self.ax.plot(self.times, self.values, marker='o', linestyle='-', color='b')

        self.update_plot()
        plt.show()

    def update_plot(self):
        while True:
            # Simulate getting new data
            current_time = datetime.now()
            self.times.append(current_time)
            self.values.append(len(self.times))  # Example: Using the length of times as the value

            # Limit number of displayed ticks
            if len(self.times) > 5:
                self.times = self.times[-5:]
                self.values = self.values[-5:]

            # Update plot
            self.line.set_xdata(self.times)
            self.line.set_ydata(self.values)

            # Format x-axis as time
            self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            plt.xticks(rotation=45)

            # Update plot
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            # Wait for a while before updating again
            time.sleep(1)


if __name__ == '__main__':
    LiveTimePlot()
