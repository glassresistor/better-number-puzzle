import random


def multiply_by():
    multiplier = random.choice(list(range(-9, 0)) + list(range(2, 10)))

    def func(seq):
        return seq[-1] * multiplier
    return func


def add_to():
    adder = random.choice(list(range(-9, 0)) + list(range(1, 10)))

    def func(seq):
        return seq[-1] + adder
    return func


def sum_last_two():
    def func(seq):
        if len(seq) == 1:
            return seq[0] + random.randint(1, 3)
        return seq[-1] + seq[-2]
    return func


def multiply_last_two():
    def func(seq):
        if len(seq) == 1:
            return seq[0] + random.randint(1, 3)
        return seq[-1] * seq[-2]
    return func


def sum_of_all():
    def func(seq):
        return sum(seq)
    return func

transforms = [multiply_by, add_to, sum_last_two, multiply_last_two, sum_of_all]


def build_puzzle():
    first = random.choice(transforms)()
    second = random.choice(transforms)()
    sequence = [random.randint(-10, 10)]
    order = [first, second, first, second, first]
    for step in order:
        new = step(sequence)
        sequence.append(new)
    if sequence[1:] == [0, 0, 0, 0, 0]:
        sequence = build_puzzle()
    return sequence


def test_human():
    puzzle = build_puzzle()
    answer = puzzle[5]
    puzzle = puzzle[0:5]
    print('Whats the next number in the sequence?\n %s, ...' % (
        ', '.join(map(str, puzzle))
    ))
    attempt = input('>>>')
    if answer == int(attempt):
        print('Winner!')

if __name__ == "__main__":
    test_human()
