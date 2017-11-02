import unittest, schedule


class TestProblem2(unittest.TestCase):
    def test_schedule(self):
        jobs = schedule.ScheduleTool.gethardcodedjobs()
        barbers = schedule.ScheduleTool.gethardcodedbarbers()

        sch = schedule.Scheduler(barbers, 30)

        sch.schedule_jobs2(jobs)

        for b in sch.barbers:
            print("{}, {}".format(b.bid, b.income))

        m = sch.getmax()
        s = sch.getmin()
        rng = m.income - s.income
        print("The range is {}".format(rng))

if __name__ == '__main__':
    unittest.main()
