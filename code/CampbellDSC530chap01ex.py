
# Week 3 Assignment 1-2 Campbell, Zachary DSC530

from __future__ import print_function, division

import numpy as np
import sys

import nsfg
import thinkstats2

# reads the data and returns a data frame
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
  
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

# cleans the data
def CleanFemResp(df):
    pass

# program to validate the values that are in the data frame by calling the data frame
def ValidatePregnum(resp):
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True

# calling all functions with the first imput being script
def main(script):
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)

# setting main
if __name__ == '__main__':
    main(*sys.argv)
