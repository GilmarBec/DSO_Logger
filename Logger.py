import datetime


class Logger:
    LOG_LEVEL_DEBUG = 10
    LOG_LEVEL_INFO = 20
    LOG_LEVEL_WARNING = 30
    LOG_LEVEL_ERROR = 40
    LOG_LEVEL_CRITICAL = 50
    LOG_LEVEL_DEFAULT = LOG_LEVEL_DEBUG

    logs = []

    def __init__(self, log_level=LOG_LEVEL_DEFAULT, file_prefix=None, file_path=None):
        self.log_level = log_level
        self.file_prefix = file_prefix
        self.file_path = file_path

    def debug(self, message):
        self.saveLog(self.LOG_LEVEL_DEBUG, message)

    def info(self, message):
        self.saveLog(self.LOG_LEVEL_INFO, message)

    def warning(self, message):
        self.saveLog(self.LOG_LEVEL_WARNING, message)

    def error(self, message):
        self.saveLog(self.LOG_LEVEL_ERROR, message)

    def info(self, message):
        self.saveLog(self.LOG_LEVEL_CRITICAL, message)

    def saveLog(self, log_level, message):
        if log_level < self.log_level:
            return

        date = datetime.date.today()
        file_name = self.file_path + date.strftime("%Y_%m_%b") + "_" + self.file_prefix + ".log"
        file = open(file_name, "a")

        file.write("[{date}]{level}:\n{message}".format(**{
            "date": date.strftime("%Y_%m_%b %H:%M%S %z"),
            "level": self.log_level,
            message: message
        }))

        file.close()
