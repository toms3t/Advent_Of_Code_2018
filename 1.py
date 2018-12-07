import itertools

frequencies = open('frequencies', 'r')
freq_changes = [x.strip('\n') for x in frequencies.readlines()]


def frequency_total():
	return sum([int(x) for x in freq_changes])


def frequency_finder(resulting_frequency=0):
	freq_seen = {0}
	for f in itertools.cycle(freq_changes):
		resulting_frequency += int(f)
		if resulting_frequency in freq_seen:
			return resulting_frequency
		else:
			freq_seen.add(resulting_frequency)


print('Part 1 answer is: {}'.format(frequency_total()))
print('Part 2 answer is: {}'.format(frequency_finder()))
