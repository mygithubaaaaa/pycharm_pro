def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if exchange is False:
            return


li = [2, 9, 8, 3, 8, 3, 0, 7, 6, 9, 23, 23, -23, 234, -4]
bubble_sort(li)
print(li)
