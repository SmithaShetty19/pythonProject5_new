import configparser

config = configparser.RawConfigParser()
path="C:\\Users\\smimp\\PycharmProjects\\pythonProject5\\Configurations\\config.ini"
config.read(path)
#config.read("../Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

