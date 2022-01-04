import time
import datetime

class Progress(object):
    startTime = time.time()
    left_sign = '█'
    # left_sign = '░'
    # right_sign = '-'
    right_sign = ' '
    lens = 20
    delay = 0.05

    def __init__(self, total):
        self.count = 0
        self.total = total
        self.mutiple = self.lens / self.total

    def update(self, step=1):
        self.count += step
        self.progress = int(self.count*self.mutiple)
        self.percent = self.progress*int(100/self.lens)
        percentChar = str(self.percent) + "%"
        doneSign = self.progress*self.left_sign
        dontSign = (self.lens-self.progress)*self.right_sign
        leftTime = self.getLeftTime()
        print("\rProgress: {:<4} |{}{}| [{}/{}]({})".format(
            percentChar, doneSign, dontSign, self.count, self.total, leftTime), end="", flush=True)

    def done(self):
        print("\rProgress: {:<4} |{}{}| [{}/{}]({})".format(
            '100%', self.lens*self.left_sign, '', self.total, self.total, '00:00:00'), flush=True)

    def getNowTime(self):
        return int(time.time() - self.startTime)

    def getLeftTime(self):
        nowTime = self.getNowTime()
        leftTimeSecs = int(nowTime/(self.percent/100)) - nowTime if self.percent > 0 else 0
        leftTime = str(datetime.timedelta(seconds=leftTimeSecs))
        leftTime = leftTime if len(leftTime) > 7 else '0' + leftTime 
        return leftTime if leftTimeSecs > 0 else '00:00:00'