# # import os
# # import time
# # import re
# #
# #
# # def get_cpu(pid):
# #     try:
# #         cmd = 'adb shell "cat /proc/stat | grep ^cpu"'
# #         cmd1 = f'adb shell cat /proc/{pid}/stat'
# #         redcmd = str(os.popen(cmd).readlines()).replace("'", "").replace("\n", " ").replace("]", " ").replace("[", " ")
# #         redcmd = [i for i in redcmd.split(",")[0].split(" ") if i != '']
# #         # 去掉首行CPU
# #         redcmd.remove(redcmd[0])
# #         # 去掉后三行不需要的数据
# #         del redcmd[-3:]
# #         # 将剩余的元素转化为列表并相加
# #         total_cpu = sum(list(map(int, redcmd)))
# #         # 获取cpu空闲时间
# #         idle = redcmd[3]
# #         redcmd1 = str(os.popen(cmd1).readlines()).replace("'", "").replace("\n", " ").replace("]", " ").replace("[",
# #                                                                                                                 " ").split(
# #             " ")[14:18]
# #         pjiff = sum(list(map(int, redcmd1)))
# #         return [total_cpu, idle, pjiff]
# #     except Exception as e:
# #         print(e, "get_s_cpu(),检查adb是否连通……")
# #         # return [-1, -1, -1]
# #
# #
# # def calculate_cpu_usage(pid):
# #     total_cpu1, idle1, pjiff1 = get_cpu(pid)
# #     while True:
# #         time.sleep(2)
# #         total_cpu2, idle2, pjiff2 = get_cpu(pid)
# #         pcpu = 100.0 * (int(pjiff2) - int(pjiff1)) / (int(total_cpu2) - int(total_cpu1))  # process cpu
# #         # system_cpu = 100.0 * ((int(total_cpu2) - int(idle2)) - (int(total_cpu1) - int(idle1))) / (
# #         #         int(total_cpu2) - int(total_cpu1))  # system cpu
# #         total_cpu1, idle1, pjiff1 = total_cpu2, idle2, pjiff2
# #         print(f"Process CPU Usage: {pcpu:.2f}%")
# #         # print(f"System CPU Usage: {system_cpu:.2f}%")
# #
# #
# # if __name__ == '__main__':
# #     pid = 3276
# #     calculate_cpu_usage(pid)
# # print('{:d}'.format(int(1.5059475898742676 % 60)))
# import os
#
# import matplotlib.pyplot as plt
# from datetime import datetime
# import matplotlib.dates as mdates
# import time
#
# # class LiveTimePlot:
# #     def __init__(self):
# #         self.fig, self.ax = plt.subplots()
# #         self.ax.set_title('Live Time Plot')
# #         self.ax.set_xlabel('Time')
# #         self.ax.set_ylabel('Value')
# #
# #         self.times = []
# #         self.values = []
# #
# #         self.line, = self.ax.plot(self.times, self.values, marker='o', linestyle='-', color='b')
# #
# #         self.update_plot()
# #         plt.show()
# #
# #     def update_plot(self):
# #         while True:
# #             # Simulate getting new data
# #             current_time = datetime.now()
# #             self.times.append(current_time)
# #             self.values.append(len(self.times))  # Example: Using the length of times as the value
# #
# #             # Limit number of displayed ticks
# #             if len(self.times) > 5:
# #                 self.times = self.times[-5:]
# #                 self.values = self.values[-5:]
# #
# #             # Update plot
# #             self.line.set_xdata(self.times)
# #             self.line.set_ydata(self.values)
# #
# #             # Format x-axis as time
# #             self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
# #             plt.xticks(rotation=45)
# #
# #             # Update plot
# #             self.fig.canvas.draw()
# #             self.fig.canvas.flush_events()
# #
# #             # Wait for a while before updating again
# #             time.sleep(1)
# #
# #
# # if __name__ == '__main__':
# #     LiveTimePlot()
# # !/user/bin/env python3
# # -*- coding: utf-8 -*-
# import os, re
# import time
# import datetime
# import subprocess
# import logging
#
# if os.path.exists(os.getcwd() + "/test_data"):
#     pass
# else:
#     os.makedirs(os.getcwd() + "/test_data")
# csv = logging.getLogger()
# csv.setLevel(logging.DEBUG)
# fh = logging.FileHandler(
#     os.getcwd() + "/test_data/" + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.csv')
# fh.setLevel(logging.INFO)
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# formatter = logging.Formatter()
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# csv.addHandler(ch)
# csv.addHandler(fh)
#
#
# def get_mem(package):
#     try:
#         cmd = r'adb shell dumpsys meminfo ' + package + ' | findstr "TOTAL"'  # % apk_file
#         total = str((os.popen(cmd).readlines()))
#         return (re.findall(r"\d+\.?\d*", total)[0])
#     except Exception as e:
#         print(str(e), "get_mem(package)，请检查包名是否正确……")
#         return -1
#
#
# def getUid(package_name):  # 获取UID
#     try:
#         p1 = subprocess.Popen('adb shell dumpsys package ' + package_name + ' | grep "userId"',
#                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 用adb获取信息
#         uidLongString = p1.stdout.read()
#         uidLongList = uidLongString.split()
#         uidMap = uidLongList[0]
#         uid = str(uidMap).split("=")[1].replace("'", "")
#
#         return uid
#
#     except Exception as e:
#         print(e, "getUid()，请检查包名是否正确……")
#
#
# def get_cpu(pid):
#     try:
#         cmd = 'adb shell "cat /proc/stat | grep ^cpu"'  # % apk_file
#         cmd1 = 'adb shell cat /proc/%s/stat' % (pid)
#         redcmd = str((os.popen(cmd).readlines())).replace("'", "").replace("\\n", " ").replace("]", " ").replace("[",
#                                                                                                                  " ")
#         redcmd = [i for i in redcmd.split(",")[0].split(" ") if i != '']
#         redcmd.remove(redcmd[0])
#         del redcmd[-3:]
#         total_cpu = sum(list(map(int, redcmd)))
#         idle = redcmd[3]
#         redcmd1 = str((os.popen(cmd1).readlines())).replace("'", "").replace("\\n", " ").replace("]", " ").replace("[",
#                                                                                                                    " ").split(
#             " ")[14:18]
#         pjiff = sum(list(map(int, redcmd1)))
#         return [total_cpu, idle, pjiff]
#     except Exception as e:
#         print(e, "get_s_cpu(),检查adb是否连通……")
#         return [-1, -1, -1, -1, -1, -1, -1]
#
#
# def get_iphoneinfo():
#     try:
#         dics = {}
#         cmd = 'adb shell "getprop | grep product"'
#         redcmd = str((os.popen(cmd).readlines())).replace("'", "").replace("\\n", " ").replace("]", " ").replace("[",
#                                                                                                                  " ").replace(
#             " ", "").split(",")
#         for i in redcmd:
#             if ":" in i:
#                 dic = {i.split(":")[0]: i.split(":")[-1]}
#                 dics.update(dic)
#         cmd1 = 'adb shell cat /proc/meminfo'
#         redcmd1 = str((os.popen(cmd1).readlines())).replace("'", "").replace("\\n", " ").replace("]", " ").replace("[",
#                                                                                                                    " ").replace(
#             " ", "").split(",")[0]
#         pp, cupxh, mmet = (
#             dics["ro.product.manufacturer"].title() + " " + dics['ro.product.model'], dics['ro.product.board'],
#             str(round(int(re.findall(r"\d+\.?\d*", redcmd1)[0]) / 1024 / 1024)) + "G")
#         return ("%s;%s;%s" % (pp, cupxh, mmet))
#     except Exception as e:
#         print(str(e), "get_mem(package)，请检查adb是否连通……")
#         return 'xxxxx'
#
#
# def get_PID(package):
#     if int(str((os.popen("adb shell getprop ro.build.version.release").readlines())).replace("'", "").replace("\\n",
#                                                                                                               " ").replace(
#         "]", " ").replace("[", " ").split('.')[0]) >= 8:
#         cmd = "adb shell ps -A"
#     else:
#         cmd = "adb shell ps"
#     try:
#         pid = []
#         redcmd = str((os.popen(cmd).readlines())).replace("'", "").replace("\\n", " ").replace("]", " ").replace("[",
#                                                                                                                  " ").split(
#             ",")
#         for n in redcmd:
#             if package in n:
#                 list_n = [i for i in n.split(" ") if i != '']  # 删除空元素
#                 if package == list_n[-1]:
#                     pid.append(list_n[1])
#         return pid[0]
#     except Exception as e:
#         print(str(e), "get_mem(package)，请检查adb是否连通……")
#         return 'xxxxx'
#
#
# def SumDic(package):
#     pid = get_PID(package)
#     total_cpu1, idle1, pjiff1 = get_cpu(pid)
#     iphone_info = get_iphoneinfo()
#     bt = "'time','iphone_info', 'package', 'mem', 'cpu', 'systemCpu' ".replace(
#         "'", "").replace(" ", "")
#     csv.info(bt)
#     while True:
#         timestr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#         mem = round(int(get_mem(package)) / 1024, 3)
#         total_cpu2, idle2, pjiff2 = get_cpu(pid)
#         pcpu = 100.0 * (int(pjiff2) - int(pjiff1)) / (int(total_cpu2) - int(total_cpu1))  # process cpu
#         systemCpu = 100.0 * ((int(total_cpu2) - int(idle2)) - (int(total_cpu1) - int(idle1))) / (
#                 int(total_cpu2) - int(total_cpu1))  # system cpu
#         total_cpu1, idle1, pjiff1 = total_cpu2, idle2, pjiff2
#         sumdic = {
#             "time": timestr,
#             "iphone_info": iphone_info,
#             'package': package,
#             "mem": mem,
#             "cpu": round(pcpu, 2),
#             "systemCpu": round(systemCpu, 2),
#         }
#         list_v = str(list(sumdic.values())).replace("[", "").replace("]", "").replace("'", "")
#         csv.info(list_v)
#
#
# if __name__ == '__main__':
#     # os.system('adb connect 192.168.1.98:5555')#连接WiFi连通adb
#     package = 'com.tencent.wecarnavi'  # com.tencent.tmgp.sgame，com.example.helloAR
#     SumDic(package)
import os
import time

# mem_sum = []
# cpu_sum = []
# mem_peak_max = []
# cpu_peak_max = []
# with open('perf_data/20240702155025.csv', 'r') as files:
#     file = files.readlines()[1:]
#     count = len(file)
#     for i in file:
#         mem_sum.append(i.strip("'").split(',')[3].replace(' ', ''))
#         mem_peak_max.append(i.strip("'").split(',')[4].replace(' ', ''))
#         cpu_sum.append(i.strip("'").split(',')[5].replace(' ', ''))
#         cpu_peak_max.append(i.strip("'").split(',')[6].replace(' ', ''))
#
#     mem_average = sum(list(map(float, mem_sum))) / count
#     mem_average_peak = max(list(map(float, mem_peak_max)))
#     cpu_average = sum(list(map(float, cpu_sum))) / count
#     cpu_average_peak = max(list(map(float, cpu_peak_max)))
#     print(mem_average, mem_average_peak, cpu_average, cpu_average_peak)
#     # sumdic = {'Time': 1,
    #           'device info': 1,
    #           'package': 1,
    #           'MEM Usage': '{:.2f}'.format(mem_average),
    #           'MEM Peak': '{:.2f}'.format(mem_average_peak),
    #           'CPU Usage': '{:.2f}'.format(cpu_average),
    #           'CPU Peak': '{:.2f}'.format(cpu_average_peak),
    #           }
# file.info()
# print('{:.2f}'.format(mem_average))

# a = [' 229.44', ' 229.51', ' 229.48', ' 229.51', ' 229.59', ' 229.54', ' 229.55', ' 229.62', ' 229.58', ' 229.61',
#      ' 229.72', ' 229.65', ' 229.65', ' 229.69', ' 229.58', ' 229.50', ' 229.58', ' 229.55', ' 229.55', ' 229.59',
#      ' 229.55', ' 229.55', ' 229.61', ' 229.54', ' 229.52', ' 229.56', ' 229.54', ' 229.56', ' 229.61', ' 229.55',
#      ' 229.45', ' 229.50', ' 229.65', ' 229.75', ' 229.85', ' 229.69', ' 229.70', ' 229.80', ' 229.70', ' 229.70',
#      ' 229.75', ' 229.69', ' 229.68', ' 229.75', ' 229.70', ' 229.69', ' 229.74', ' 229.71', ' 229.71', ' 229.79',
#      ' 229.72', ' 229.73', ' 229.78', ' 229.72', ' 229.72', ' 229.76', ' 229.73', ' 229.71', ' 229.76', ' 229.70',
#      ' 229.49', ' 229.56', ' 229.60', ' 230.05', ' 230.13']
# print()
# a = os.path.dirname(__file__)
# print(os.path.join(a + 'perf123', time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.csv'))\
# sum_average2 = {
#     'MEM average': 12,
#     'MEM Peak': 33,
#     'CPU average': 44,
#     'CPU Peak': 55,
# }
# sum_average = {
#     '': '',
#     '': '',
#     '': '',
#     '': '',
#     'MEM average': '内存均值:{:.2f}'.format(12.123214),
#     'MEM Peak': f'内存峰值:{33.41241}',
#     'CPU average': f'CPU均值:{44.412241}',
#     'CPU Peak': f'CPU峰值:{55.4125453}',
# }
# # print(' '.join(sum_average.values()))
# a = str(list(sum_average.values())).replace("[", "").replace("]", "").replace('"', '')
# print(a.replace("'", ''))
# print(str(list(sum_average2.values())).replace("[", "").replace("]", "").replace('"', ''))
