import re
import datetime
from collections import Counter


class GuardSchedule:
    SLEEP_SCHEDULE = ''
    SLEEP_SCHEDULE_DICT = {}
    AGGREGATE_SLEEP_TIMES = {}
    GUARD_SLEEP_MINUTES = {}
    SLEEPIEST_GUARD = 0
    SLEEPIEST_GUARD_TOTAL_SLEEP_TIME = 0
    SLEEPIEST_MINUTE = 0


    @classmethod
    def create_ordered_sleep_schedule(cls, f):
        with open(f) as f:
            GuardSchedule.SLEEP_SCHEDULE = [
                x.strip('\n') for x in f.readlines()
            ]
            GuardSchedule.SLEEP_SCHEDULE.sort()

    @classmethod
    def create_sleep_schedule_dict(cls):
        pattern = re.compile('\[(\d+)-(\d+)-(\d+) (\d+:\d+)\] (.*$)')
        guard_id = 0
        for guard_str in GuardSchedule.SLEEP_SCHEDULE:
            year, month, day, time, action = pattern.match(
                guard_str).group(1,2,3,4,5)

            if 'Guard' in action:
                guard_id_pattern = re.search('Guard #(\d+) ', action)
                guard_id = guard_id_pattern.group(1)
                if guard_id not in GuardSchedule.SLEEP_SCHEDULE_DICT:
                    GuardSchedule.SLEEP_SCHEDULE_DICT[guard_id] = []
                continue
            GuardSchedule.SLEEP_SCHEDULE_DICT[guard_id].append(
                [year, month, day, time, action]
            )

    @classmethod
    def find_sleepiest_guard(cls):
        for guard in GuardSchedule.SLEEP_SCHEDULE_DICT:
            GuardSchedule.AGGREGATE_SLEEP_TIMES[guard] = []
            GuardSchedule.GUARD_SLEEP_MINUTES[guard] = []
            sleep_start = ''
            for s in GuardSchedule.SLEEP_SCHEDULE_DICT[guard]:
                try:
                    if s[4] == 'falls asleep':
                        sleep_start = datetime.datetime(
                            int(s[0]),
                            int(s[1]),
                            int(s[2]),
                            0,
                            int(s[3][-2:]),
                            0
                        )

                    if s[4] == 'wakes up':
                        sleep_end = datetime.datetime(
                            int(s[0]),
                            int(s[1]),
                            int(s[2]), 0,
                            int(s[3][-2:])-1,
                            0
                        )
                        sleep_time = sleep_end - sleep_start
                        GuardSchedule.AGGREGATE_SLEEP_TIMES[guard].append(
                            (sleep_time.seconds//60)+1
                        )

                        GuardSchedule.GUARD_SLEEP_MINUTES[
                            guard].extend(
                            [str(x) for x in range(
                                sleep_start.minute, sleep_end.minute + 1)]
                        )

                except IndexError:
                    continue
        d = {k: sum(v) for k, v in GuardSchedule.AGGREGATE_SLEEP_TIMES.items()}
        GuardSchedule.SLEEPIEST_GUARD = max(d, key=lambda x: d.get(x))

    @classmethod
    def find_sleepiest_minute(cls, g):
        all_min_dict = Counter(GuardSchedule.GUARD_SLEEP_MINUTES[g])
        print('aaa',all_min_dict)
        # print(GuardSchedule.GUARD_SLEEP_MINUTES)
        GuardSchedule.SLEEPIEST_MINUTE = max(
            all_min_dict, key=lambda x: all_min_dict.get(x)
        )
        # GuardSchedule.SLEEPIEST_MINUTE_COUNT = all_min_dict.get(x)





GuardSchedule.create_ordered_sleep_schedule('sleep_schedule')
GuardSchedule.create_sleep_schedule_dict()
most_asleep_minute = 0
GuardSchedule.find_sleepiest_guard()
for guard in GuardSchedule.GUARD_SLEEP_MINUTES:
    if not GuardSchedule.GUARD_SLEEP_MINUTES[guard]:
        continue
    GuardSchedule.find_sleepiest_minute(guard)
    if int(GuardSchedule.SLEEPIEST_MINUTE) > most_asleep_minute:
        most_asleep_minute = int(GuardSchedule.SLEEPIEST_MINUTE)
        GuardSchedule.SLEEPIEST_GUARD = guard
print(GuardSchedule.SLEEPIEST_GUARD, most_asleep_minute)
# GuardSchedule.find_sleepiest_minute()
# print('Part 1 answer is: {}'.format(
#     int(GuardSchedule.SLEEPIEST_GUARD) * int(GuardSchedule.SLEEPIEST_MINUTE))
# )









