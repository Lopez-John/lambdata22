'''Testing helper_functions.py from NewLambdata package'''

import unittest
import numpy as np
import pandas as pd
from random import randint, sample
import helper_functions as thehelp


class TestNewDataFrameMethods(unittest.TestCase):
    '''Tests null_count Method'''
    def test_nullcount(self):
        test_df = thehelp.NewDataFrame(
                                        np.random.randint(
                                                        0,
                                                        100,
                                                        size=(100, 5)
                                                        ),
                                        columns=list('ABCDE')
                                        )
        self.assertEqual(test_df.nullcount(), 0)

    def test_split_dates(self):
        '''Tests split_dates method'''
        test_list = [
                    "1994-04-09",
                    "1996-12-16",
                    "1995-01-04",
                    "2012-02-07",
                    "2017-01-06",
                    "2013-01-26"
                    ]
        test_df = thehelp.NewDataFrame(test_list, columns=['date'])
        test_df.split_dates()
        self.assertEqual(test_df.shape, (6, 4))

if __name__ == '__main__':
    unittest.main()
