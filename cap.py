####
# harrym 2014
#
# Node Capacitance extractor from Spectre Netlist
#
# Input parameters: Node names separated by space
####

import re
import sys

nodes=len(sys.argv)

p=input('Print every single capacitance found? 0/1  ')
print "\n"

for i in range(1,nodes):
    node=sys.argv[i]
    cap=0
    with open('netlist', 'r') as inputFile:
        for index, line in enumerate(inputFile):
            ncap = re.search(re.compile('%s 0\) cmodel c=(.*)'%node), line)
            if ncap:
                if p==1:
                    print ncap.group(1)
                cap = cap + float(ncap.group(1))
    print "Total capacitance at ", node, ": ", cap, "\n"
