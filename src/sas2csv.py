#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This code can only be run with python 2, since "pyhcup" only support python 2.
# Usage: python sas2csv.py -d {ASC file} -l {SAS load file} -o {output folder} -y {year}


import logging
import logging.handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]: %(levelname)s: %(message)s')

import pandas as pd
import pyhcup
import numpy as np
import csv
import sys
import os
import json

# Convert raw files to csv
def converter(datafile, loadfile, outputdir, year):

    path = os.path.join(outputdir, os.path.splitext(os.path.basename(datafile))[0] + '.csv')
    logger.info('file path: %s'%path)
    if not os.path.isfile(path):
        meta_df = pyhcup.meta_from_sas(loadfile)
        logger.info('loading dataframe...')
        df = pyhcup.read(datafile, meta_df)
        logger.info('writing dataframe...')
        df.to_csv(path, index = False, quoting = csv.QUOTE_ALL)
        del df
    logger.info('Done!')

if __name__ == '__main__':

    logger.info(sys.version)

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--datafile', help="define the location of the ASCII datafile;", dest = 'df', required=True)
    parser.add_argument(
        '-l', '--loadfile', help="define the location of the corresponding SAS loadfile;", dest = 'lf', required=False)    
    parser.add_argument(
        '-o', '--output', help="define the location of the output dir;", dest = 'output', required=False)
    parser.add_argument(
        '-y', '--year', help="define the year of the hcup data;", dest = 'year', required=False)


    args = parser.parse_args()

    handler = logging.handlers.RotatingFileHandler(
        '../logs/sas2csv_%s.log'%(os.path.split(os.path.basename(args.df))[1][0:-4]), maxBytes=100 * 1024 * 1024, backupCount=10)
    logger.addHandler(handler)

    converter(args.df, args.lf, args.output, args.year)
