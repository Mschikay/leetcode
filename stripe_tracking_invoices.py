'''
 should be usd
 finalize after create, only once
 pay after finalize, only once
 illegal operate
 illegal currency
 type not ordered
'''

from collections import defaultdict


def tracking(actions):
    ans = 0
    info = defaultdict(list)
    for action in actions:
        action = action.split(":")
        operate = action[0].strip()
        if operate in ("CREATE", "FINALIZE"):
            details = action[1].strip().split("&")
            d = {}
            for detail in details:
                arr = detail.split("=")
                d[arr[0]] = arr[1]
            if "id" not in d or "amount" not in d or "currency" not in d: continue
            id = d["id"]
            try:
                amount = int(d["amount"])
                assert amount >= 0
            except (ValueError, AssertionError) as e:
                continue
            currency = d["currency"]
            if currency != "USD": continue
            if operate == "CREATE":
                if id in info: continue
                info[id] = ["CREATE", amount]
                ans += amount
            else:
                if id not in info: continue
                status = info[id][0]
                if status == "CREATE":
                    before = info[id][1]
                    ans += amount - before
                    info[id] = ["FINALIZE", amount]

        elif operate == "PAY":
            id = action[1].strip().split("=")[1]
            if id not in info: continue
            status = info[id][0]
            if status == "FINALIZE":
                ans -= info[id][1]
                info[id][0] = "PAY"
        print(info)

    print(ans)
    return ans


if __name__ == "__main__":
    input = ["CREATE: id=14&amount=800&currency=USD",
             "FINALIZE:id=14&amount=800&currency=USD",
             "PAY: id=14"]
    tracking(input)

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculate_total_owed' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY actions as parameter.
#
from collections import defaultdict


def process(details):
    d = {}
    for detail in details:
        arr = detail.split("=")
        d[arr[0].strip()] = arr[1].strip()
    if "id" not in d or "amount" not in d or "currency" not in d: return None, None
    # get id, amount and currency
    if d["currency"] != "USD": return None, None
    try:
        assert int(d["amount"]) >= 0
    except (ValueError, AssertionError):
        return None, None
    return d["id"], int(d["amount"])


def calculate_total_owed(actions):
    # Write your code here
    ans = 0
    info = defaultdict(list)
    for action in actions:
        action = action.split(":")
        operate = action[0].strip()
        if operate in ("CREATE", "FINALIZE"):
            details = action[1].strip().split("&")
            aid, amount = process(details)
            if aid is None: continue
            if operate == "CREATE":
                if aid not in info:
                    ans += amount
                    info[aid] = ["CREATE", amount]
            else:
                if aid in info:
                    if info[aid][0] == "CREATE":
                        ans += amount - info[aid][1]
                        info[aid] = ["FINALIZE", amount]

        elif operate == "PAY":
            aid = action[1].strip().split("=")[1].strip()
            if aid in info:
                if info[aid][0] == "FINALIZE":
                    ans -= info[aid][1]
                    info[aid][0] = "PAY"

    return ans


if __name__ == '__main__':

'''
At the beginning, I thought:

1. if the action is USD, skip it

2. The operations strictly follow CREATE, FINALIZE, PAY, and each only be effective for once

3. In case of illegal operations, check if it is one of 3 operations

4. In case of illegal space input, always use "strip" to forbidden extra spaces

5. The action may contain things other than "id", "amount", "currency", use a hashmap to process it

In the 2nd version, I modulized the single function code. It is good for readability, and easier for unit test in the future, and easier for add or removing features. I think this kind of decoupling is friendly for developer.

If I had more time, for the details of this code, we can think more of how to catch the exception where we encounter illegal input errors. And I am thinking of using a set to save the id that has already been paid. if the action is PAY,  I remove it from the "info" dict(hashmap), and add this id into set. Next time if I find the id in the set, I can skip it. By doing this will not cause extra space and time, and the legacy information in info will not be preserved so the info will always be the newest. But of course, it depends on the requirements of users.

The actions can be very large, we may cannot directly put it in memory and start to process it. We can split it into several bulks and process them in order line by line. What's more, we can edit it into multithread program. We can easily classify the operations by checking the first several characters, and use a tag to preserve their order of appearance in the file. Threads keep a global hashmap to simultaneously save the records of "CREATE" and also their tags, and then, only process the "FINALIZE" with same id and tags that bigger than "CREATE", and so on the "PAY".


'''