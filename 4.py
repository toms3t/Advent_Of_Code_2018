import re
import datetime
from collections import Counter, OrderedDict

with open('sleep_schedule') as f:
    ss = [x.strip('\n') for x in f.readlines()]
    ss.sort()

print(ss)
for x in ss:
    if "2417" in x:
        print(x)


class GuardTrack:
    def __init__(self, gid):
        self.gid = gid
        # self.

    SLEEPIEST_GID = 0
    MAX_SLEEP_TIME = 0
    SLEEPIEST_MINUTE = 0


guard_dict = OrderedDict()
pattern = re.compile('\[(\d+)-(\d+)-(\d+) (\d+:\d+)\] (.*$)')
gid = 0
for guard_str in ss:
    year, month, day, time, action = pattern.match(guard_str).group(1,2,3,4,5)
    if 'Guard' in action:
        gid_pattern = re.search('Guard #(\d+) ', action)
        gid = gid_pattern.group(1)
        if gid not in guard_dict:
            guard_dict[gid] = []
        continue
    guard_dict[gid].append([year, month, day, time, action])

# for guard in guard_dict:
total_sleep_time = 0
sleep_times = []
sleep_minutes = []
sleep_start = ''
sleep_end = ''
for s in guard_dict['3271']:
    try:
        if s[4] == 'wakes up':
            sleep_end = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), 0, int(s[3][-2:])-1, 0)
            sleep_time = sleep_end - sleep_start
            sleep_times.append((sleep_time.seconds//60)+1)
            sleep_minutes.extend([str(x) for x in range(sleep_start.minute, sleep_end.minute+1)])

        if s[4] == 'falls asleep':
            sleep_start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), 0, int(s[3][-2:]), 0)
    except IndexError:
        continue
# print(guard)
print('s', sleep_minutes)
a = Counter(sleep_minutes)
print(a)
total_sleep_time = sum(sleep_times)
# if total_sleep_time > GuardTrack.MAX_SLEEP_TIME:
#     GuardTrack.SLEEPIEST_GID = guard

print(GuardTrack.SLEEPIEST_GID)
# print(guard_dict['73'])

# print(guard_dict['73'])
# print('asdf', sleep_minutes)
# a = Counter(sleep_minutes)
# print(a)
# # print(guard_dict['73'])
# print(GuardTrack.SLEEPIEST_GID)
print(73*29)








