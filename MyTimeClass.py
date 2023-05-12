import warnings


class Time:
    def __init__(self, hour, minute, force=False):
        if force:
            self.__hour = hour
            self.__minute = minute
        else:
            self.hour = hour
            self.minute = minute
            
    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if not 0 <= value < 24:
            warnings.warn("Hour should be in the range [0, 24). Correcting by going around the clock.")
            value = value % 24
        self.__hour = value
        
    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if not 0 <= value < 60:
            warnings.warn(f"Minute should be in the range [0, 60), but is equal to {value}. Correcting by increasing hours.")
            self.hour += value // 60
            value = value % 60
            
        self.__minute = value

    def check_time_format_24(self):
        if 0 <= self.__minute < 60 and 0 <= self.__hour < 24:
            print("Format OK")
            return True
        
        if not 0 <= self.__hour < 24:
            print(f"Format invalid - hour: {self.__hour}")
        if not 0 <= self.__minute < 60:
            print(f"Format invalid - minute: {self.__minute}")
            
        return False
    
    def __add__(self, other):
        h = self.hour + other.hour
        m = self.minute + other.minute
        h += m // 60
        m = m % 60
        return Time(h, m)
    
    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
    
    def __gt__(self, other):
        return self.hour > other.hour or (self.hour > other.hour and self.minute > other.minute)
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    import numpy as np
    
    t = Time(12, 73)
    t0 = Time(0, 0)
    
    print(f"{t=}")
    print(f"{t0=}")
    print(f"{t+t0=}\n")
    
    tm = Time(10, 0)
    print(f"{tm=}")
    print("Attempt on setinng 80 minutes in tm:")
    tm.minute = 80
    print(f"{tm=}")
    print("Once again attempt on setinng 80 minutes in tm:")
    tm.minute = 80
    print(f"{tm=}\n")
    
    
    ts = [Time(h, m) for h, m in np.random.randint(24, size=(7, 2))]
    print(ts, "(random times)")
    
    sorted_ts = sorted(ts)
    print(sorted_ts, "(sorted random times)")
    tt = [t1 + t2 for t1, t2 in zip(ts, sorted_ts)]
    print(tt, "(random times added to sorted random times)\n")
    
    print("Checking sums format:")
    for t in tt:
        print(f"{t=}", end='  ')
        t.check_time_format_24()
    
    print("Checking forced wrong format:")
    t_wrong = Time(12, 65, force = True)
    print(f"{t_wrong=}", end = '  ')
    t_wrong.check_time_format_24()
    