
# ada lovelace day

def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365

def beforeOct(year):
    if leap(year) == 366:
        return 274
    else:
        return 273

# 1970 1/1 4
def ald(year):
    days = 0
    firstOct = 0
    if year > 1970:
        for yr in range(1970, year):
            days += leap(yr)
        days += beforeOct(year)
        firstOct = (days % 7 + 4) % 7
    else:
        for yr in range(1970, year, -1):
            days += leap(yr)
        days += 92
        m = days % 7
        firstOct = 5 - m if m <= 4 else 12 - m
    rest = 9 - firstOct + 1 if firstOct > 2 else 2 - firstOct + 1
    return 7 + rest


print(ald(1950))

# !/bin/python3

import math
import os
import random
import re
import sys

# The Alerter is a simple monitoring tool, intended to help detect increases in response time for some process. It does that
# by computing a few statistics about the process across a 'window' of a certain number of runs, and alerting (returning true)
# if certain thresholds are met.
#
# It takes the following parameters:
#  - inputs: A list of integer times for the process. This list may be very long
#  - window size: how many runs long a window is, as an integer
#  - allowedIncrease: how far over 'average' a window or value is allowed to be, as a percent. This is represented as a decimal value based on one, so a 50% allowable increase would be represented as 1.5
#
# Your Alerter should return true if either of the following conditions are met:
#  * Any value is more than the allowed increase above the window average in ALL windows in which it appears.
#      For example:
#          alert({1, 2, 100, 2, 2}, 3, 1.5) should alert: the value 100 appears in three windows ({1,2,100}, {2,100,2}, and {100,2,2}), and in all cases is more than 50% over the average value (34 1/3, 34 2/3, and 34 2/3, respectively).
#          alert({1, 2, 4, 2, 2}, 3, 2) should not alert: the largest outlier is 4, and that value appears in a window with average value 2.6 (The window {2,4,2}), less than 200% of that average
#  * Any window's average is more than the acceptable increase over any previous window's average value
#      For example:
#          alert({1,2,100,2,2}, 2, 2.5) should alert: Even though no individual value causes an alert, there is a window with average 1.5 (The window {1,2}) and a later window with an average more than 2.5 times larger (the window {2, 100}, average 51)
# Otherwise, you should return false.
# Complete the alert function below.


# leetcode 239. Sliding Window Maximum



def getWindow(size, idx, window):
    if idx <= window - 1:
        return idx + 1
    elif idx >= size - window:
        return size - idx
    return window


def alert(inputs, windowSize, allowedIncrease):
    if not inputs or not windowSize: return False
    i, j = 0, windowSize - 1
    preSum = [0]
    for val in inputs:
        preSum.append(preSum[-1] + val)

    preAverage = float("inf")
    maxVal, maxIdx, maxCnt = float("-inf"), -1, 0
    windowCnt = 0
    while j < len(inputs):
        if j - windowSize + 1 > maxIdx:
            maxVal, maxIdx = float("-inf"), -1
            for z in range(i, j + 1):
                if inputs[z] > maxVal:
                    maxVal = inputs[z]
                    maxIdx = z
                    maxCnt = 0
                    windowCnt = getWindow(len(inputs), z, windowSize)
        elif inputs[j] > maxVal:
            maxVal = inputs[j]
            maxIdx = j
            maxCnt = 0
            windowCnt = getWindow(len(inputs), j, windowSize)

        # condition 2
        average = (preSum[j + 1] - preSum[i]) / windowSize
        if not preAverage or average / preAverage > allowedIncrease: return True
        preAverage = min(preAverage, average)

        # condition 1
        if not average or maxVal / average > allowedIncrease:
            maxCnt += 1
            if maxCnt == windowCnt: return True

        j += 1
        i += 1
    return False


if __name__ == '__main__':