###################################################
# 22-12-18 No.25304 영수증
###################################################

# import sys

# def receipt(total, num, vlist, alist):
#     sum = 0

#     for i in range(num):
#         sum += (vlist[i] * alist[i])

#     if total == sum:
#         print("Yes")
#     else:
#         print("No")


# total = int(sys.stdin.readline())
# n = int(sys.stdin.readline())

# valueList = []
# amountList = []

# for i in range(n):
#     value, amount = map(int, sys.stdin.readline().split())
#     valueList.append(value)
#     amountList.append(amount)

# receipt(total, n, valueList, amountList)