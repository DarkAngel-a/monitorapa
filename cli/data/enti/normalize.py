#!/usr/bin/env python3

# This file is part of MonitoraPA
#
# Copyright (C) 2022 Giacomo Tesio <giacomo@tesio.it>

import sys
import os.path

def usage():
    print("""
./cli/data/enti/normalize.py ./out/enti/YYYY-MM-YY/enti.tsv

Will create ./out/enti/YYYY-MM-YY/dataset.tsv
""")
    sys.exit(-1)

def outputFileName(inputFileName):
    return os.path.join(os.path.dirname(inputFileName), "dataset.tsv")


def main(argv):
    if len(argv) != 2:
        usage()
    try:
        with open(argv[1], "r") as inf, open(outputFileName(argv[1]), mode="w") as outf:
            i = 0
            for line in inf:
                if i == 0:
                    i += 1 # skip column headers
                    continue
                line = line.strip(" \n")
                fields = line.split('\t');
                outID = fields[1]
                outf.write('\t'.join([outID, 'Web', fields[29]]) + '\n')
                outf.write('\t'.join([outID, 'Email', fields[19]]) + '\n')                
    except IOError as ioe:
        print(f"[ ERR ]: IOError: {ioe}")
        usage()

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("[ ERR ] KeyboardInterrupt, aborting")
        sys.exit(1)
