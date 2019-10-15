import configparser
import sys


class myconfig(object):
    current_path = sys.path[0]
    configfile_path = current_path.split(
        "\\dsy_Pro")[0] + "\\dsy_Pro\\dsy\\data\\config.conf"
    config = configparser.ConfigParser()
    config.read(configfile_path)

    # print(config.sections()[2])

    def sgFuser(self):
        user = self.config.get("sgF", "user")
        return user

    def sgFpwd(self):
        pwd = self.config.get("sgF", "password")
        return pwd

    def sgZuser(self):
        user = self.config.get("sgZ", "user")
        return user

    def sgZpwd(self):
        pwd = self.config.get("sgZ", "password")
        return pwd

    def JLuser(self):
        user = self.config.get("JL", "user")
        return user

    def JLpwd(self):
        pwd = self.config.get("JL", "password")
        return pwd

    def YZuser(self):
        user = self.config.get("YZ", "user")
        return user

    def YZpwd(self):
        pwd = self.config.get("YZ", "password")
        return pwd

if __name__ == '__main__':
    user = myconfig().sgZuser()
    pwd = myconfig().sgZpwd()
    print(user, pwd)
