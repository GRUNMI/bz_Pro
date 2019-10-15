import logging
import time
import os
import sys
current_filename = os.path.basename(sys.argv[0])
current_path = os.getcwd()
log_path = os.path.join(current_path.replace(current_path.split('\\')[-1], 'logs'))
if not os.path.exists(log_path):
    os.mkdir(log_path)
class Log():
    def __init__(self):
        self.logName = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.level = logging.DEBUG
        self.logger.setLevel(self.level)
        # 日志输出格式
        # self.nativeFormatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        self.nativeFormatter = logging.Formatter('[%(asctime)s ' + current_filename + '] - %(levelname)s - %(message)s')
        # self.consoleFormatter = logging.Formatter('[line:%(lineno)d]' + '%(asctime)s ' + current_filename + ' %(levelname)s %(message)s')
        self.consoleFormatter = logging.Formatter('%(asctime)s ' + current_filename + ' %(levelname)s %(message)s')

    def __console(self, level, message):
        # 创建一个FileHeadler，用于写到本地
        fh = logging.FileHandler(self.logName, mode='a', encoding='utf-8')
        fh.setLevel(self.level)
        fh.setFormatter(self.nativeFormatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHeadler，用于输入控制台
        sh = logging.StreamHandler()
        sh.setLevel(self.level)
        sh.setFormatter(self.consoleFormatter)
        self.logger.addHandler(sh)

        if level == 'info':
            self.logger.info(message)
        if level == 'debug':
            self.logger.debug(message)
        if level == 'warning':
            self.logger.warning(message)
        if level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)
        # 关闭打开的文件
        fh.close()

    def info(self, message):
        self.__console('info', message)

    def debug(self, message):
        self.__console('debug', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == '__main__':
    log = Log()
    log.info("begin")
    log.debug("debug")
    log.warning("warning")
    log.error("error")
