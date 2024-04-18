# https://zhuanlan.zhihu.com/p/431445882 [netron 神经网络可视化教程]

# 先生成一个模型
import torchvision.models as models
import torch

# 定义样例数据+网络
data = torch.randn(2, 3, 256, 256) 
net = models.resnet34()

# 导出为onnx格式
torch.onnx.export(
    net,
    data, # 如果是多输入，形式为（data1,data2）
    'model.onnx',
    export_params=True,
    opset_version=8,
)

# 用netron打开模型即可
