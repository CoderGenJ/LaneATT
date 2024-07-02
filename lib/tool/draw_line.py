import matplotlib.pyplot as plt
import numpy as np
import math

# 给定参数
start_x = 0.5
start_y = 1
n_offsets = 72
angle = 60 * math.pi / 180  # 将角度转换为弧度
img_w = 800
img_h = 600

# 生成 anchor_ys
anchor_ys = np.linspace(1, 0, n_offsets, dtype=np.float32)

# 计算 x 坐标
anchor_xs = (start_x + (1 - anchor_ys - 1 + start_y) / np.tan(angle)) * img_w

# 将 y 坐标转换到图像的高度范围
anchor_ys = anchor_ys * img_h

# 绘制曲线
plt.figure(figsize=(10, 6))
plt.plot(anchor_xs, anchor_ys, label='Anchor Curve')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Anchor Curve')
plt.gca().invert_yaxis()  # 反转 y 轴以符合图像坐标系
plt.legend()
plt.grid(True)
plt.show()