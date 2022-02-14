# -*- coding: utf-8 -*-
"""Main module.

To start execution, use:

$ python main.py

"""

from src.functions import input_to_sha, loop_random_print

MAX_PAUSE = 5
TEXT_LIST = ('Name\n', 'Vacancy\n', 'Salary\n')


if __name__ == '__main__':
    loop_random_print(TEXT_LIST, MAX_PAUSE)
    input_to_sha()
