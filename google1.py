

# def plantflower(plants, capacity):
#     return 0 if not plants or not capacity
#     i = 0
#     remain = capacity
#     step = 0
#     while i < len(plants):
#         print(i)
#         while i < len(plants) and remain > 0:
#             remain -= plants[i]
#             step += 1
#             i += 1
#         if i == len(plants) and remain >= 0: break
#         if not remain:
#             step += i * 2
#         else:
#             i -= 1
#             plants[i] = -remain
#             step += i + 1 + i
#         remain = capacity
#         print(step)
#     return step

def plantflower(plants, capacity):
    if not plants or not capacity: return 0
    i = 0
    remain = capacity
    step = 0
    while i < len(plants):
        while i < len(plants) and remain >= plants[i]:
            remain -= plants[i]
            step += 1
            i += 1
        if i == len(plants): break
        step += i * 2
        remain = capacity
    return step


print(plantflower([2, 2, 1, 1, 2], 3))