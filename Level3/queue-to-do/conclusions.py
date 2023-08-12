# Notes
#  - fails.solution1 and fails.solution2 scale similar in terms of speed. O(n^2). Too slow for big lengths.
#    Built-in functools.reduce is better optimized, though.
#  - Using range() in fails.solution1 will use peaks of tenths of GB of RAM for very big lengths.
#    This is because in python 2, range() creates a list instead of get the next value when needed as xrange() does.
#    In Python 3, range() behaves as xrange().
#    Docs:
#        Python 3 Ranges: https://docs.python.org/3/library/stdtypes.html#typesseq-range
#        Python 2 xrange: https://docs.python.org/2/library/functions.html#xrange
#  - solution.solution runs fast enough. O(n).

import timeit


def graph_times((module, func),
                max_length=10000,
                scale=100,
                divisions=10):
    for length in range(0, max_length, max_length / divisions):
        time = timeit.timeit('solution(0, {})'.format(length),
                             'from {} import {} as solution'.format(module, func),
                             number=1)
        print('{} {} {}'.format('%f' % time,
                                str(length).zfill(len(str(max_length)) - 1),
                                '*' * int(time * scale)))


def graph_all(**kwargs):
    funcs = (('solution', 'solution', 'xor pattern'),
             ('fails', 'solution1', 'functools.reduce'),
             ('fails', 'solution2', 'while loops'))
    for module, func, desc in funcs:
        print('{}.{} - {}'.format(module, func, desc))
        graph_times((module, func), **kwargs)
        print('')


graph_all()
graph_times(
    ('solution', 'solution'),
    scale=10000,
    max_length=10000,
    divisions=20
)
