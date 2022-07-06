import time
import matplotlib.pyplot as plt
import numpy.random as npr

w1 = npr.randint(100, size=10)
w2 = npr.randint(100, size=20)
w3 = npr.randint(100, size=40)
w4 = npr.randint(100, size=100)
w5 = npr.randint(100, size=200)
w6 = npr.randint(100, size=400)
w7 = npr.randint(100, size=800)
w8 = npr.randint(100, size=2000)
v1 = npr.randint(100, size=10)
v2 = npr.randint(100, size=20)
v3 = npr.randint(100, size=40)
v4 = npr.randint(100, size=100)
v5 = npr.randint(100, size=200)
v6 = npr.randint(100, size=400)
v7 = npr.randint(100, size=800)
v8 = npr.randint(100, size=2000)



##归并排序
def MergeSort(l=list):
    def merge(li, low, mid, high):
        # 列表，最开始的值，中间值(第一个有序列表的最后一位),最后面的值

        # 将两个有序列表的开头标记出来
        i = low
        j = mid + 1  # 第二段有序数列的开头
        list_1 = []
        while i <= mid and j <= high:  # 限制条件(开头小于结尾)两边都有数
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
        # 终止条件 只有一个元素
        if low < high:  # 至少有两个，递归终止条件(只剩一个的时候)
            mid = (low + high) // 2  # 二分查找中间值
            merge_sort(li, low, mid)  # 递归左边,左边排序
            # print(li[low:high+1])
            merge_sort(li, mid + 1, high)  # 递归右边，右边排序
            # print(li[low:high+1])
            merge(li, low, mid, high)
            # print(li[low:high+1])

    merge_sort(l, 0, len(l) - 1)


##贪心算法
def Package(Item_Weight, Item_Value, Bag_Size):
    start = time.perf_counter()
    MergeSort(Item_Weight)
    MergeSort(Item_Value)
    n = len(Item_Weight)
    status = [0] * n
    total_weight = 0
    total_value = 0
    for i in range(n):
        if Item_Weight[i] <= Bag_Size:
            total_weight += Item_Weight[i]
            total_value += Item_Value[i]
            status[i] = 1
            Bag_Size -= Item_Weight[i]
        else:
            continue

    end = time.perf_counter()
    return end - start


##图像绘制
x_axis_data = [10, 20, 40, 100, 200, 400, 800, 2000]
y_axis_data1 = [Package(w1,v1,1000), Package(w2,v2,1000), Package(w3,v3,1000), Package(w4,v4,1000), Package(w5,v5,1000), Package(w6,v6,1000), Package(w7,v7,1000), Package(w8,v8,1000)]

# 画图
plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='Greedy Algorithm')

plt.legend()  # 显示上面的label
plt.xlabel('Number of Items')
plt.ylabel('Execution Time')

# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
