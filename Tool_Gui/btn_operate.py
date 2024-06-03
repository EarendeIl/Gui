import os
import subprocess
import time
from PyQt5.QtCore import QThread, pyqtSignal


#  Btn_Operate类继承自 QThread，用于在后台执行命令
class Btn_Operate(QThread):
    # output_signal 是一个信号，用于传递命令的输出
    output_signal = pyqtSignal(str)
    cmd_signal = pyqtSignal()

    def run_shell(self, cmd1, shell=False):
        # 启动子进程执行命令，并捕获其标准输出和标准错误
        process = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell, text=True,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
        # 等待子进程完成，并读取输出
        stdout, stderr = process.communicate()
        # 如果有标准输出内容，发出信号
        if stdout:
            self.output_signal.emit(stdout)
            # 如果有标准错误内容，发出信号
        if stderr:
            self.output_signal.emit(stderr)
        self.cmd_signal.emit()

    def catch_logcat(self):
        # 开始抓取LOGCAT
        dir_lis = []
        for paths in os.listdir("D:\\"):
            dirs = os.path.join("D:\\", paths)
            if os.path.isdir(dirs):
                dir_lis.append(paths)
        if "logcat" not in dir_lis:
            os.mkdir("D:\\logcat")
        logtime = time.strftime('%Y-%m-%d_%H-%M-%S')
        log_path = os.path.join('D:\\logcat', f"{logtime}.log")
        os.system(f"adb logcat > {log_path}")

    def kill_logcat_pid(self):
        # 找到logcat pid 并kill
        process = subprocess.Popen("adb shell ps|grep logcat", text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        out, err = process.communicate()
        if out:
            self.output_signal.emit(out)
        if err:
            self.output_signal.emit(err)
        for line in out.split('\n'):
            if line.strip():
                pid = line.split()[1]
                kill_pid = subprocess.Popen(f"adb shell kill -9 {pid}", text=True, stdout=subprocess.PIPE
                                            , stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
                pid_stdout, pid_stderr = kill_pid.communicate()
                if pid_stdout:
                    self.output_signal.emit(pid_stdout)
                if pid_stderr:
                    self.output_signal.emit(pid_stderr)


if __name__ == '__main__':
    a = Btn_Operate()
    a.kill_logcat_pid()
