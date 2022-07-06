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



#动态规划
def bag(n,c,w,v):
    start = time.time()
    res=[[-1 for j in range(c+1)] for i in range(n+1)]
    for j in range(c+1):
        res[0][j]=0
    for i in range(1,n+1):
        for j in range(1,c+1):
            res[i][j]=res[i-1][j]
            if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
                res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
    end = time.time()
    return end - start


##图像绘制
x_axis_data = [10, 20, 40, 100, 200, 400, 800, 2000]
y_axis_data1 = [bag(10,200,w1,v1), bag(20,200,w2,v2), bag(40,200,w3,v3), bag(100,200,w4,v4), bag(200,200,w5,v5), bag(400,200,w6,v6), bag(800,200,w7,v7), bag(2000,200,w8,v8)]
y_axis_data2 = [bag(10,400,w1,v1), bag(20,400,w2,v2), bag(40,400,w3,v3), bag(100,400,w4,v4), bag(200,400,w5,v5), bag(400,400,w6,v6), bag(800,400,w7,v7), bag(2000,400,w8,v8)]
y_axis_data3 = [bag(10,800,w1,v1), bag(20,800,w2,v2), bag(40,800,w3,v3), bag(100,800,w4,v4), bag(200,800,w5,v5), bag(400,800,w6,v6), bag(800,800,w7,v7), bag(2000,800,w8,v8)]
y_axis_data4 = [bag(10,2000,w1,v1), bag(20,2000,w2,v2), bag(40,2000,w3,v3), bag(100,2000,w4,v4), bag(200,2000,w5,v5), bag(400,2000,w6,v6), bag(800,2000,w7,v7), bag(2000,2000,w8,v8)]

# 画图
plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='C = 200')
plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='C = 400')
plt.plot(x_axis_data, y_axis_data3, 'go--', alpha=0.5, linewidth=1, label='C = 800')
plt.plot(x_axis_data, y_axis_data4, 'y.--', alpha=0.5, linewidth=1, label='C = 2000')

plt.legend()  # 显示上面的label
plt.xlabel('Number of Items')
plt.ylabel('Execution Time')

# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
