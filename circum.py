#!/usr/bin/env python3

import math

PI = math.pi


MAX_VALUE = int(input("Enter the max value of counter: "))
counter = 0
while counter <= MAX_VALUE:
    area = ((counter)**2)*PI
    print(f"Area of circle with radius {counter} = {area: .2f}")
    counter += 1


