#Python获取pid和进程名字
# 1，安装psutil
#
# pip
# install
# psutil
#
# 如果pip不识别，就进入下载的python目录下面执行：。。。Python36\Scripts
#
# 2，获取信息代码


import psutil;
import os;
import signal;

for proc in psutil.process_iter():
    print("pid-%d,name:%s" % (proc.pid, proc.name()))
    if proc.name() == "chrome.exe" or proc.name() == "chromedriver.exe":
        # os.kill(int(proc.pid), signal.pthread_kill())
        os.kill(proc.pid, signal.SIGTERM)
        print("杀死进程：pid-%d,name:%s" % (proc.pid, proc.name()))

# 电脑系统是win10 64位，在使用python的signal模块时报错：“AttributeError: module 'signal' has no attribute 'SIGALRM'”，这是因为signal模块可以在linux下正常使用，但在windows下却有一些限制，在python文档https://docs.python.org/2/library/signal.html#signal.signal找到了如下解释：
#
# "On Windows, signal() can only be called with SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, or SIGTERM. A ValueError will be raised in any other case."
#
# 也就是说在windows下只能使用这几个信号：
#
# SIGABRT
# SIGFPE
# SIGILL
# SIGINT
# SIGSEGV
# SIGTERM















