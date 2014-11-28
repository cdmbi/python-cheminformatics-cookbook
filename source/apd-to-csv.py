#!/usr/bin/env python
'''Description'''
import sys
import re
import csv
import glob

def main():
    for infile in glob.glob('*.txt'):
        html = open(infile).read()

        # use regular expression to parse all values
        aa_compositions = re.findall('[A-Z]:\s(\d+)\s,', html)
        other_values = re.findall('=\s+([-+]?[\s+]?[0-9]*\.?[0-9]+)', html)

        # write values in CSV format
        writer = csv.writer(sys.stdout, 'excel-tab')
        other_values[-6] = int(other_values[-6])  # total charge
        writer.writerows([aa_compositions + other_values])

if __name__=='__main__':
    main()

