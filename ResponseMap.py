from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def show_heatmap_3D(response):
    # TODO: 需要定义函数映射关系 直接绘制可以直接返回heatmap
    def fun(X, Y, responese):
        return responese

    # TODO: Set parameters
    # X,Y分别表示了取样点的横纵坐标的可能取值,步长
    X = np.arange(0, response.shape[1], 1)
    Y = np.arange(0, response.shape[0], 1)
    # 用这两个arange对象中的可能取值一一映射去扩充为所有可能的取样点
    X, Y = np.meshgrid(X, Y)
    Z = fun(X, Y, response)  # 用取样点横纵坐标去求取样点Z坐标
    pdf = PdfPages('frame1_R54_C.pdf')
    fig = plt.figure()  # 创建一个绘图对象
    ax = Axes3D(fig)  # 用这个绘图对象创建一个Axes对象(有3D坐标)
    ax.set_axis_off() #关闭3D坐标
    # plt.title("Response Map")  # 总标题
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, shade=False, alpha=1)  # 用取样点(x,y,z)去构建曲面
    # ax.set_xlabel('x label', color='r')
    # ax.set_ylabel('y label', color='g')
    # ax.set_zlabel('response', color='b')  # 给三个坐标轴注明

    pdf.savefig()
    pdf.close()
    plt.show()  # 显示模块中的所有绘图对象
    plt.close()

