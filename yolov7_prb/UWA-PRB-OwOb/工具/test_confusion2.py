import numpy as np

# 原始混淆矩阵数据
confusion_matrix = np.array([
    [4631,2,0,5,896],
    [3,755,0,2,156],
    [2,3,170,0,67],
    [4,1,0,1412,214],
    [379,138,51,142,0]
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
    [4631,2,0,5,896],
    [3,755,0,2,156],
    [2,3,170,0,67],
    [4,1,0,1412,214],
    [379,138,51,142,0]
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
    [4631,2,0,5,896],
    [3,755,0,2,156],
    [2,3,170,0,67],
    [4,1,0,1412,214],
    [379,138,51,142,0]
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
