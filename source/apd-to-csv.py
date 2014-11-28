#!/usr/bin/env python
'''Description'''
import sys
import re
import csv
import glob
from bs4 import BeautifulSoup

def main():
    for infile in glob.glob('*.txt'):
        data = BeautifulSoup(open(infile), 'lxml')
        html = str(data)
        aa_compositions = re.findall('[A-Z]:\s(\d+)\s,', html)
        other_values = re.findall('=\s+([-+]?[\s+]?[0-9]*\.?[0-9]+)', html)

        writer = csv.writer(sys.stdout, 'excel-tab')
        other_values[-6] = int(other_values[-6])  # total charge
        writer.writerows([aa_compositions + other_values])

if __name__=='__main__':
    main()

