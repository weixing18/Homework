# 数据初始化
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(100000)

sum = 0
l1 = np.random.randint(1000, size=10)
l2 = np.random.randint(1000, size=100)
l3 = np.random.randint(1000, size=1000)
l4 = np.random.randint(1000, size=2000)
l5 = np.random.randint(1000, size=5000)
l6 = np.random.randint(1000, size=10000)  # 初始化整数列表


##冒泡排序
def BubbleSort(l):
    global Bcount
    Bcount = 0
    n = len(l)
    for i in range(n - 1):  # 第几轮
        for j in range(n - i - 1):
            if l[j + 1] < l[j]:
                l[j], l[j + 1] = l[j + 1], l[j]
            Bcount += 1
    return Bcount


##快速排序
quick_compare_count = 0


def quick_sort(l):
    global quick_compare_count
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        quick_compare_count += len(less)
        greater = [i for i in l[1:] if i > pivot]
        quick_compare_count += len(greater)
        return quick_sort(less) + [pivot] + quick_sort(greater)


def QuickSort(l):  # 封装一下排序和输出性能指标
    global quick_compare_count
    quick_compare_count = 0  # 重置全局变量
    result = quick_sort(l)
    return quick_compare_count


##归并排序
merge_compare_count = 0


def merge(li, low, mid, high):
    global merge_compare_count
    # 列表，最开始的值，中间值(第一个有序列表的最后一位),最后面的值

    # 将两个有序列表的开头标记出来
    i = low
    j = mid + 1  # 第二段有序数列的开头
    list_1 = []
    while i <= mid and j <= high:  # 限制条件(开头小于结尾)两边都有数
        merge_compare_count+=1
        if li[i] < li[j]:
            list_1.append(li[i])
            i += 1
        else:
            list_1.append(li[j])
            j += 1
    # while执行完成，，肯定有一部分没数了
    while i <= mid:  # 左列表还有数
        list_1.append(li[i])
        i += 1
    while j <= high:  # 右列表还有数
        list_1.append(li[j])
        j += 1
    # 再将list_1里的数放回li中
    li[low:high + 1] = list_1


def merge_sort(li, low, high):
    global merge_compare_count
    # 终止条件 只有一个元素
    if low < high:  # 至少有两个，递归终止条件(只剩一个的时候)
        mid = (low + high) // 2  # 二分查找中间值
        merge_sort(li, low, mid)  # 递归左边,左边排序

        merge_sort(li, mid + 1, high)  # 递归右边，右边排序

        merge(li, low, mid, high)



def MergeSort(l=list):
    global merge_compare_count
    merge_compare_count = 0
    result = merge_sort(l,0,len(l)-1)
    return merge_compare_count



##图像绘制
x_axis_data = [10, 100, 1000, 2000, 5000, 10000]
y_axis_data1 = [BubbleSort(l1), BubbleSort(l2), BubbleSort(l3), BubbleSort(l4), BubbleSort(l5), BubbleSort(l6)]
y_axis_data2 = [MergeSort(l1), MergeSort(l2), MergeSort(l3), MergeSort(l4), MergeSort(l5), MergeSort(l6)]
y_axis_data3 = [QuickSort(l1), QuickSort(l2), QuickSort(l3), QuickSort(l4), QuickSort(l5), QuickSort(l6)]

# 画图
plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='BubbleSort')
plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='MergeSort')
plt.plot(x_axis_data, y_axis_data3, 'go--', alpha=0.5, linewidth=1, label='QuickSort')

plt.legend()  # 显示上面的label
plt.xlabel('Data Size')
plt.ylabel('Number of Comparisons')

# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
