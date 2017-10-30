import unittest, schedule


class TestProblem2(unittest.TestCase):
    def test_schedule(self):
        jobs = schedule.ScheduleTool.gethardcodedjobs()
        barbers = schedule.ScheduleTool.gethardcodedbarbers()

        sch = schedule.Scheduler(barbers, 30)

        # sch.schedule_jobs(jobs)
        sch.schedule_jobs2(jobs)

        for b in sch.barbers:
            print(b.income)

        # self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
