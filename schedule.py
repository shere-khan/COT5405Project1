import random


class Barber:
    def __init__(self, time, bid):
        self.arrival_time = time
        self.income = 0
        self.bid = bid

    def assign(self, job):
        self.income += job

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

    def schedule_jobs_reassign_priority(self, jobs):
        self.barbers.sort(key=lambda x: x.arrival_time)

        while jobs:
            k = 5 if len(jobs) >= 5 else len(jobs)
            for i in range(k):
                b = self.get_next_barber()
                b.assign(jobs.pop(0))
            self.reassign_order_priority()

    def schedule_jobs_direct_assignment_threshold(self, jobs):
        while jobs:
            k = min(len(jobs), len(self.barbers))
            jobs, kjobs = self.take(k, jobs)
            kjobs.sort(reverse=True)
            self.direct_assignment(self.barbers, kjobs)
            self.reassign_order_priority()

    @staticmethod
    def take(n, l):
        temp = l[:n]
        l = l[n:]

        return l, temp

    def reassign_order(self):
        l = self.check_income_threshold()
        if l:
            b = self.barbers.pop(self.barbers.index(l[1]))
            self.barbers.insert(0, b)

    def reassign_order_priority(self):
        reorder = self.check_income_threshold2()

        while reorder:
            x = reorder.pop(0)
            self.barbers.remove(x)
            self.barbers.insert(0, x)

    @staticmethod
    def direct_assignment(l, jobs):
        for i in range(len(jobs)):
            b = l[i]
            b.assign(jobs[i])

    def check_income_threshold(self):
        m = self.getmax()
        s = self.getmin()
        if m.income - s.income > self.threshold:
            return [m, s]
        else:
            return []

    def check_income_threshold2(self):
        m = self.getmax()
        limit = m.income - self.threshold
        reorder = []
        for b in self.barbers:
            if b.income <= limit:
                reorder.append(b)

        reorder.sort(key=lambda x: x.income, reverse=True)

        return reorder

    def get_next_barber(self):
        b = self.barbers.pop(0)
        self.barbers.append(b)

        return b

    def getmax(self):
        return max(self.barbers, key=lambda x: x.income)

    def getmin(self):
        return min(self.barbers, key=lambda x: x.income)


class ScheduleTool:
    @staticmethod
    def getrandomjobs(numjobs):
        price_range = [10, 20, 30, 40]
        j = [random.choice(price_range) for i in range(numjobs)]
        return j

    @staticmethod
    def gethardcodedjobs():
        j = [40, 40, 20, 20, 30, 10, 10, 40, 40, 20, 30, 20, 10, 40, 10, 30, 20,
             40, 40, 20, 10, 20, 20, 30, 20, 30, 10, 20, 40]
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

    @staticmethod
    def get_random_jobs(n):
        l = [10, 20, 30, 40]
        return [l[random.randint(0, len(l) - 1)] for x in range(n)]
