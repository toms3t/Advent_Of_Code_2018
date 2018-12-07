from fuzzywuzzy import fuzz

with open('box_IDs') as f:
    box_ids = [x.strip('\n') for x in f.readlines()]


def find_box_checksum():
    twos = []
    threes = []
    for _id in box_ids:
        for char in _id:
            if _id.count(char) == 2 and _id not in twos:
                twos.append(_id)
            elif _id.count(char) == 3 and _id not in threes:
                threes.append(_id)

    return len(twos)*len(threes)


def find_box_id_one_char_diff():
    for ida in box_ids:
        for idb in box_ids[1:]:
            if fuzz.ratio(ida, idb) == 96:
                return ida, idb


print('Part 1 answer is: {}'.format(find_box_checksum()))
print('Part 2 answer is: {}'.format(find_box_id_one_char_diff()))
