class Clock(object):
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    def __init__(self, hour, minute):
        self.minutes = (minute + hour * 60) % self.MINUTES_PER_HOUR
        self.hours = ((minute + hour * 60) // self.MINUTES_PER_HOUR) % self.HOURS_PER_DAY

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours

    def __add__(self, minute):
        return self.__class__(self.hours, self.minutes + minute)

    def __sub__(self, minute):
        return self.__class__(self.hours, self.minutes - minute)