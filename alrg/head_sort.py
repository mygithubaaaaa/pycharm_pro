def sift(li,low,high):
    '''

    :param li:列表
    :param low:堆的根节点位置
    :param high:堆的最后一个位置
    :return:
    '''
    i = low # i最开始指向根节点
    j = 2 * i + 1   # j开始是左孩子
    temp = li[low]  #把堆顶存起来
    while j <= high:
        if j + 1 <= high and li[j+1] > li[j]: # 右孩子比较大
            j += 1  # j指向右孩子
        if li[j] > temp:
            li[i] = li[j]
            i = j
            j = 2 * i +1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp


def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li ,0 ,i - 1 )

li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)

