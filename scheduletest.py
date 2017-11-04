import unittest

import schedule


class TestProblem2(unittest.TestCase):
    @staticmethod
    def compute_average(barbers):
        return sum(b.income for b in barbers) / len(barbers)

    def test_schedule_og(self):
        avgs = []
        ranges = []
        for i in range(100):
            jobs = schedule.ScheduleTool.get_random_jobs(50)
            barbers = schedule.ScheduleTool.gethardcodedbarbers()
            sch = schedule.Scheduler(barbers, 30)
            sch.schedule_jobs(jobs)

            ranges.append(sch.getmax().income - sch.getmin().income)
            avgs.append(TestProblem2.compute_average(sch.barbers))

        average = sum(avgs) / len(avgs)
        print("The average of averages for test 1: {}".format(average))
        avg_range = sum(ranges) / len(ranges)
        print("The average range for test 1: {}".format(avg_range))
        print()

    def test_schedule(self):
        avgs = []
        ranges = []
        for i in range(100):
            jobs = schedule.ScheduleTool.get_random_jobs(50)
            barbers = schedule.ScheduleTool.gethardcodedbarbers()
            sch = schedule.Scheduler(barbers, 30)
            sch.schedule_jobs(jobs)

            ranges.append(sch.getmax().income - sch.getmin().income)
            avgs.append(TestProblem2.compute_average(sch.barbers))

        average = sum(avgs) / len(avgs)
        print("The average of averages for test 1: {}".format(average))
        avg_range = sum(ranges) / len(ranges)
        print("The average range for test 1: {}".format(avg_range))
        print()

    def test_schedule_reassign_priority(self):
        avgs = []
        ranges = []
        for i in range(100):
            jobs = schedule.ScheduleTool.get_random_jobs(50)
            barbers = schedule.ScheduleTool.gethardcodedbarbers()

            sch = schedule.Scheduler(barbers, 10)

            sch.schedule_jobs_reassign_priority(jobs)

            m = sch.getmax()
            s = sch.getmin()
            ranges.append(m.income - s.income)
            # print("The range is {}".format(rng))

            avgs.append(TestProblem2.compute_average(sch.barbers))
            # print("The average is {}".format(avg))
            # print()
        average = sum(avgs) / len(avgs)
        print("The average of averages for test 2: {}".format(average))
        avg_range = sum(ranges) / len(ranges)
        print("The average range for test 2: {}".format(avg_range))
        print()

    def test_schedule_reassign_direct_no_threshold(self):
        avgs = []
        ranges = []
        for i in range(100):
            jobs = schedule.ScheduleTool.get_random_jobs(50)
            barbers = schedule.ScheduleTool.gethardcodedbarbers()

            barbers.sort(key=lambda x: x.arrival_time)
            sch = schedule.Scheduler(barbers, 0)

            sch.schedule_jobs_direct_assignment_threshold(jobs)

            m = sch.getmax()
            s = sch.getmin()
            ranges.append(m.income - s.income)
            # print("The range is {}".format(rng))

            avgs.append(TestProblem2.compute_average(sch.barbers))
            # print("The average is {}".format(avg))
            # print()
        average = sum(avgs) / len(avgs)
        print("The average of averages for test 3: {}".format(average))
        avg_range = sum(ranges) / len(ranges)
        print("The average range for test 3: {}".format(avg_range))
        print()

    def test_schedule_reassign_direct_with_threshold(self):
        avgs = []
        ranges = []
        for i in range(100):
            jobs = schedule.ScheduleTool.get_random_jobs(50)
            barbers = schedule.ScheduleTool.gethardcodedbarbers()

            barbers.sort(key=lambda x: x.arrival_time)
            sch = schedule.Scheduler(barbers, 20)

            sch.schedule_jobs_direct_assignment_threshold(jobs)

            m = sch.getmax()
            s = sch.getmin()
            ranges.append(m.income - s.income)
            # print("The range is {}".format(rng))

            avgs.append(TestProblem2.compute_average(sch.barbers))
            # print("The average is {}".format(avg))
            # print()
        average = sum(avgs) / len(avgs)
        print("The average of averages for test 4: {}".format(average))
        avg_range = sum(ranges) / len(ranges)
        print("The average range for test 4: {}".format(avg_range))
        print()

if __name__ == '__main__':
    unittest.main()
