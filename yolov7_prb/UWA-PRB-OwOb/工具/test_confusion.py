import numpy as np

# 原始混淆矩阵数据
confusion_matrix = np.array([
    [4434, 2, 2, 8, 748],
    [4, 616, 0, 3, 121],
    [1, 1, 141, 0, 36],
    [5, 0, 0, 1222, 156],
    [478, 122, 50, 151, 0]
])

# 归一化混淆矩阵
normalized_matrix = np.zeros_like(confusion_matrix, dtype=float)
for i in range(len(confusion_matrix)):
    row_sum = np.sum(confusion_matrix[i])
    if row_sum != 0:  # 避免除以0
        normalized_matrix[i] = confusion_matrix[i] / row_sum

# 打印归一化混淆矩阵
print("Normalized Confusion Matrix:")
print(normalized_matrix)

import numpy as np

matrix = np.array([
    [4510, 2, 2, 7, 894],
    [2, 631, 1, 3, 144],
    [1, 1, 144, 0, 44],
    [5, 0, 0, 1241, 185],
    [478, 122, 50, 151, 0]
])

# 进行归一化处理
normalized_matrix = matrix / (matrix.sum(0).reshape(1, matrix.shape[1]) + 1E-6)
np.set_printoptions(formatter={'float': '{:0.5f}'.format})
print("-> Normalized Confusion Matrix:")
print(normalized_matrix)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 混淆矩阵数据
matrix = np.array([
    [4510, 2, 2, 7, 894],
    [2, 631, 1, 3, 144],
    [1, 1, 144, 0, 44],
    [5, 0, 0, 1241, 185],
    [478, 122, 50, 151, 0]
])

# 进行归一化处理
normalized_matrix = matrix / (matrix.sum(0).reshape(1, matrix.shape[1]) + 1E-6)

# 绘制混淆矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(normalized_matrix, annot=True, cmap='Blues', fmt='.5f',
            xticklabels=['echinus', 'holothurian', 'scallop', 'starfish', 'background FP'],
            yticklabels=['echinus', 'holothurian', 'scallop', 'starfish', 'background FN'])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('Normalized Confusion Matrix')
plt.savefig('normalized_confusion_matrix.png')  # 保存归一化混淆矩阵图像

# 绘制未归一化的混淆矩阵（整数表示）
plt.figure(figsize=(10, 8))
sns.heatmap(matrix.astype(int), annot=True, cmap='Blues',
            xticklabels=['echinus', 'holothurian', 'scallop', 'starfish', 'background FP'],
            yticklabels=['echinus', 'holothurian', 'scallop', 'starfish', 'background FN'],
            fmt='d')
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('Confusion Matrix')
plt.show()
