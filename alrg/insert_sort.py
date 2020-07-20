def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        temp = li[i]
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


li = [2, 9, 8, 3, 8, 3, 0, 7, 6, 9, 23, 23, -23, 234, -4]
insert_sort(li)
print(li)
