import os


def read_file(day, transform):
    try:
        with open(os.path.join('..', 'TextFiles', f'day_{day}.txt')) as f:
            return [transform(line.strip()) for line in f]
    except FileNotFoundError as e:
        print(e)
