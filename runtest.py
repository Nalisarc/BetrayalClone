#!/usr/bin/env python3
import sys
import unittest
suite = unittest.TestLoader().discover('tests')
if __name__ == '__main__':
    for test in suite:
        print(test)
    sys.exit()
