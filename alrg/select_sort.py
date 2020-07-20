def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):    # 找到最小值的下标
            if li[j]<li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]


li = [3, 2, 1, 8, 4, 7, ]
select_sort(li)
print(li)
