#!/usr/bin/env python3
# Optixal
import sys

lines = int(sys.stdin.readline().strip())

for i in range(lines):
    entry   = sys.stdin.readline().strip().split(' ')
    name    = entry[0]
    began   = entry[1]
    bday    = entry[2]
    courses = int(entry[3])
   
    # Check 1 or 2 - Matriculate 2010 or ltr || Born 1991 or ltr
    if int(began.split('/')[0]) >= 2010 or int(bday.split('/')[0]) >= 1991:
        print(name, 'eligible')
        continue

    # Check 3 - >8 sems
    if courses >= 41:
        print(name, 'ineligible')
        continue

    # Coach
    print(name, 'coach petitions')
