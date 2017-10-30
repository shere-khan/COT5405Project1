if __name__ == '__main__':
    x = [2, 3, 6, 10, 1]
    print(max(x))


class Barber:
    def __init__(self, time):
        self.arrival_time = time
        self.income = 0

    def assign(self, job):
        self.income += job.cost


class Scheduler:
    def __init__(self, barbers, threshold):
        self.barbers = barbers
        self.threshold = threshold

    def schedule_jobs(self, jobs):
        self.barbers.sort(key=lambda x: x.arrival_time)

        for j in jobs:
            b = self.get_next_barber()
            b.assign(j)

    def get_next_barber(self):
        b = self.barbers.pop(0)
        self.barbers.append(b)

        return b

    def reassign_order(self, barbers):
        pass

    def check_income_threshold(self):
        m = max(self.barbers, key=lambda x: x.income)
        s = min(self.barbers, key=lambda x: x.income)
        if m.income - s.income > self.threshold:
            return [m, s]
        else:
            return []
