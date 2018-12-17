from collections import OrderedDict
from string import ascii_lowercase
import sys

sys.setrecursionlimit(3000)


class Polymer:

    ORIG_POLYMER_STR = ''
    ORIG_POLYMER_DICT = OrderedDict()
    WORKING_POLYMER_STR = ''
    WORKING_POLYMER_DICT = {}
    NEW_POLYMER_STR = ''
    SHORTEST_POLYMER_LENGTH = 0

    @classmethod
    def read_poly_str(cls):
        with open('polymers') as f:
            Polymer.ORIG_POLYMER_STR = f.read()

    @classmethod
    def create_dict(cls, poly_str):
        if Polymer.ORIG_POLYMER_DICT:
            Polymer.ORIG_POLYMER_DICT.clear()
        for k, v in enumerate(poly_str):
            Polymer.ORIG_POLYMER_DICT[k] = v
        Polymer.WORKING_POLYMER_DICT = Polymer.ORIG_POLYMER_DICT.copy()

    @classmethod
    def polymer_reducer(cls):
        i = 1
        new_str = ''
        reduced = 0
        add_to_str = False
        skip = False
        for k, v in Polymer.WORKING_POLYMER_DICT.items():
            if skip:
                skip = False
                continue
            chars = ''
            chars += v
            if not Polymer.WORKING_POLYMER_DICT.get(i):
                if not add_to_str:
                    new_str += chars
                break
            chars += Polymer.WORKING_POLYMER_DICT.get(i)
            if chars[0].lower() != chars[1].lower():
                if add_to_str:
                    new_str += chars[-1]
                else:
                    new_str += chars
                i += 1
                add_to_str = True

            elif not (any(char.isupper() for char in chars)):
                if add_to_str:
                    new_str += chars[-1]
                else:
                    new_str += chars
                i += 1
                add_to_str = True

            elif not (any(char.islower() for char in chars)):
                if add_to_str:
                    new_str += chars[-1]
                else:
                    new_str += chars
                i += 1
                add_to_str = True

            elif (any(char.isupper() for char in chars) and any(
                char.islower() for char in chars)) and \
                    chars[0].lower() == chars[1].lower():
                skip = True
                i += 2
                reduced += 1
                if add_to_str:
                    new_str = new_str[:-1]
                add_to_str = False
                continue
            else:
                new_str += chars
                i += 1
        Polymer.NEW_POLYMER_STR = new_str
        if reduced:
            Polymer.create_dict(Polymer.NEW_POLYMER_STR)
            Polymer.polymer_reducer()

    @classmethod
    def unit_remover(cls, char):
        Polymer.WORKING_POLYMER_STR = ''.join([
            x for x in Polymer.ORIG_POLYMER_STR
            if (x != char and x != char.upper())
        ]
        )

    @classmethod
    def problem_unit_finder(cls):
        problem_unit_tracker = []
        for char in ascii_lowercase:
            Polymer.unit_remover(char)
            Polymer.create_dict(Polymer.WORKING_POLYMER_STR)
            Polymer.polymer_reducer()
            problem_unit_tracker.append(len(Polymer.NEW_POLYMER_STR))
        Polymer.SHORTEST_POLYMER_LENGTH = min(problem_unit_tracker)


def main():
    Polymer.read_poly_str()
    Polymer.create_dict(Polymer.ORIG_POLYMER_STR)
    Polymer.polymer_reducer()
    print('Part 1 answer is: {}'.format(len(Polymer.NEW_POLYMER_STR)))

    Polymer.problem_unit_finder()
    print('Part 2 answer is: {}'.format(Polymer.SHORTEST_POLYMER_LENGTH))


if __name__ == '__main__':
    main()






