import random


class Barber:
    def __init__(self, time, bid):
        self.arrival_time = time
        self.income = 0
        self.bid = bid

    def assign(self, job):
        self.income += job.cost

    def __repr__(self):
        return "{}".format(self.bid)

    def __str__(self):
        return "{}".format(self.bid)


class Scheduler:
    def __init__(self, barbers, threshold):
        self.barbers = barbers
        self.threshold = threshold

    def schedule_jobs(self, jobs):
        self.barbers.sort(key=lambda x: x.arrival_time)

        for j in jobs:
            b = self.get_next_barber()
            b.assign(j)
            self.reassign_order()

    def schedule_jobs2(self, jobs):
        self.barbers.sort(key=lambda x: x.arrival_time)

        while jobs:
            for i in range(5):
                b = self.get_next_barber()
                b.assign(jobs.pop(0))
            self.reassign_order()

    def get_next_barber(self):
        b = self.barbers.pop(0)
        self.barbers.append(b)

        return b

    def reassign_order(self):
        l = self.check_income_threshold()
        if l:
            self.barbers.pop(self.barbers.index(l[1]))

    def check_income_threshold(self):
        m = max(self.barbers, key=lambda x: x.income)
        s = min(self.barbers, key=lambda x: x.income)
        if m.income - s.income > self.threshold:
            return [m, s]
        else:
            return []


class ScheduleTool:
    @staticmethod
    def getrandomjobs(numjobs):
        price_range = [10, 20, 30, 40]
        j = [random.choice(price_range) for i in range(numjobs)]
        return j

    @staticmethod
    def gethardcodedjobs():
        j = [10, 40, 20, 20, 30, 10, 10, 40, 40, 20, 30, 20, 10, 40, 10, 30, 20,
             40, 10, 20, 10, 20, 20, 30, 20, 30, 10, 20, 40]
        return j

    @staticmethod
    def gethardcodedbarbers():
        barbers = []
        barbers.append(Barber(800, 'A'))
        barbers.append(Barber(815, 'B'))
        barbers.append(Barber(810, 'C'))
        barbers.append(Barber(805, 'D'))
        barbers.append(Barber(806, 'E'))

        return barbers
