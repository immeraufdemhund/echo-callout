import datetime

class TimeService:
    @staticmethod
    def getCurrentSeconds():
            t0 = datetime.datetime(2019, 1, 1)
            return (datetime.datetime.now() - t0).total_seconds()
