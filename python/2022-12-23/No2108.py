###################################################
# 22-12-23 No.2108 통계학
###################################################

# import sys

# from collections import Counter

# t = int(sys.stdin.readline())

# nl = []
# nd = {}
# modeL = []

# for _ in range(t):
#     kn = int(sys.stdin.readline())
#     nl.append(kn)

# print(f"{round(sum(nl)/t)}")

# sortNL = sorted(nl)

# print(f"{sortNL[t//2]}")

# cntND = (Counter(sortNL))
# cntNL = []

# for i in cntND.keys():
#     if cntND[i] == max(cntND.values()):
#         cntNL.append(i)

# if len(cntNL) == 1:
#     print(f"{cntNL[0]}")
# else:
#     print(f"{cntNL[1]}")

# maxV = max(sortNL)
# minV = min(sortNL)

# print(f"{maxV - minV}")