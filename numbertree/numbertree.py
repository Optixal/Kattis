#!/usr/bin/env python3
# Optixal

chall = input().strip().split(' ')
height = int(chall[0])
tip = 2 << height
index = 1
if len(chall) == 2:
    for direction in chall[1]:
        if direction == 'L': index <<= 1
        else: index = (index << 1) + 1
print(tip - index)
