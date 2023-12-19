import sys

hw = [i for i in range(1, 31, 1)]

for k in range(28):
    hw_num = int(sys.stdin.readline())
    hw.remove(hw_num)
hw.sort()
print(hw[0])
print(hw[1])
