import torch

# 查看版本
print(torch.__version__)
#查看gpu是否可用
print(torch.cuda.is_available())
#返回设备gpu个数
print(torch.cuda.device_count())
# 查看对应CUDA的版本号
print(torch.backends.cudnn.version())
print(torch.version.cuda)
#退出python
quit()