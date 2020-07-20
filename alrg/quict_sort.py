import random
import time


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:  # 从左边找比tmp大的数
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

li = list(range(1000))
random.shuffle(li)
# li = [2, 9, 8, 3, 8, 3, 0, 7, 6, 9, 23, 23, -23, 234, -4]
time1 = time.time()
quick_sort(li, 0, len(li) - 1)
time2 = time.time()
print(time2 - time1)


# print(li)
